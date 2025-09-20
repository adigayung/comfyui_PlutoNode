# comfyui_PlutoNode/image_save_nodes.py

import os
import numpy as np
import torch
from PIL import Image

class PlutoAutoSaveImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "format": (["PNG", "JPG"],),
                "folder_path": ("STRING", {"default": "L:/ComfyUI/outputs"}),
                "prefix": ("STRING", {"default": "output_"}),
                "padding": ("INT", {"default": 8, "min": 1, "max": 16}),
            }
        }

    # Agar tidak punya output port yang bisa dihubungkan
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "auto_save"
    CATEGORY = "Pluto/IO"
    OUTPUT_NODE = True  # agar UI menampilkan preview

    def auto_save(self, image, format, folder_path, prefix, padding):
        # Konversi ke numpy untuk disimpan ke disk
        np_image = image[0].cpu().numpy()
        np_image = (np_image * 255).clip(0, 255).astype(np.uint8)

        # Konversi ke PIL
        if np_image.shape[2] == 1:
            pil_image = Image.fromarray(np_image[:, :, 0], mode="L")
        else:
            pil_image = Image.fromarray(np_image, mode="RGB")

        # Buat folder jika belum ada
        os.makedirs(folder_path, exist_ok=True)

        # Generate filename yang unik
        index = 1
        while True:
            filename = f"{prefix}{str(index).zfill(padding)}.{format.lower()}"
            output_path = os.path.join(folder_path, filename)
            if not os.path.exists(output_path):
                break
            index += 1

        # Simpan ke disk
        pil_format = "JPEG" if format.upper() == "JPG" else format.upper()
        pil_image.save(output_path, format=pil_format)

        print(f"[PlutoAutoSaveImage] Saved to: {output_path}")

        # ✅ Kembalikan image untuk preview saja (tidak untuk chaining)
        return (image,)


NODE_CLASS_MAPPINGS = {
    "PlutoAutoSaveImage": PlutoAutoSaveImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PlutoAutoSaveImage": "🪐 Pluto : Auto Save Image"
}
