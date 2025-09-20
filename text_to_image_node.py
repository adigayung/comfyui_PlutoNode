import os
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

FONTS_DIR = os.path.join(os.path.dirname(__file__), "fonts")

# Ambil semua font di folder ./fonts
def list_fonts():
    if not os.path.exists(FONTS_DIR):
        os.makedirs(FONTS_DIR)
    fonts = [f for f in os.listdir(FONTS_DIR) if f.lower().endswith((".ttf", ".otf"))]
    return fonts if fonts else ["default"]

class TextToImageNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "width": ("INT", {"default": 800, "min": 100, "max": 4000}),
                "height": ("INT", {"default": 200, "min": 50, "max": 2000}),
                "font_size": ("INT", {"default": 64, "min": 8, "max": 256}),
                "font_name": (list_fonts(),),
                "color": ("STRING", {"default": "#FFFFFF"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "render_text"
    CATEGORY = "Pluto/Text"

    def render_text(self, text, width, height, font_size, font_name, color):
        # Buat canvas transparan
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Cari font
        font_path = os.path.join(FONTS_DIR, font_name) if font_name != "default" else None
        try:
            if font_path and os.path.exists(font_path):
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default()
        except Exception as e:
            print("⚠️ Font load failed:", e)
            font = ImageFont.load_default()

        # Hitung posisi teks biar center
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pos = ((width - text_w) // 2, (height - text_h) // 2)

        # Render teks
        draw.text(pos, text, font=font, fill=color)

        # PIL → numpy → torch tensor
        np_img = np.array(img).astype(np.float32) / 255.0
        tensor_img = torch.from_numpy(np_img)[None, ...]

        return (tensor_img,)


NODE_CLASS_MAPPINGS = {
    "TextToImageNode": TextToImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextToImageNode": "🪐 Pluto : Text To Image"
}
