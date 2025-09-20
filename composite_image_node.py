import torch
import numpy as np
from PIL import Image

class CompositeImageNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "front": ("IMAGE",),
                "behind": ("IMAGE",)
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "composite"
    CATEGORY = "pluto/image"

    def tensor_to_pil(self, tensor, label="image"):
        if tensor.ndim == 3 and tensor.shape[0] in [1, 3, 4]:  # (C, H, W)
            tensor = tensor.permute(1, 2, 0)  # -> (H, W, C)
        elif tensor.ndim == 3 and tensor.shape[2] in [1, 3, 4]:  # already (H, W, C)
            pass
        else:
            raise ValueError(f"[ERROR] {label}: Unexpected tensor shape: {tensor.shape}")

        channel_count = tensor.shape[2]
        if channel_count not in [1, 3, 4]:
            raise ValueError(f"[ERROR] {label}: Unsupported number of channels: {channel_count}")

        np_img = tensor.cpu().numpy()
        np_img = (np_img * 255).clip(0, 255).astype("uint8")
        return Image.fromarray(np_img)


    def composite(self, front, behind):
        print("[DEBUG] front input type:", type(front), " len:", len(front))
        print("[DEBUG] behind input type:", type(behind), " len:", len(behind))

        front_img = self.tensor_to_pil(front[0], label="front").convert("RGBA")
        behind_img = self.tensor_to_pil(behind[0], label="behind").convert("RGB")

        # Resize behind to match front if needed
        if behind_img.size != front_img.size:
            behind_img = behind_img.resize(front_img.size)

        composed = Image.alpha_composite(behind_img.convert("RGBA"), front_img)
        composed = composed.convert("RGB")

        # Convert back to tensor
        composed_np = np.array(composed).astype(np.float32) / 255.0
        composed_np = np.transpose(composed_np, (2, 0, 1))  # [C, H, W]
        composed_tensor = torch.from_numpy(composed_np)

        return ([composed_tensor],)


NODE_CLASS_MAPPINGS = {
    "CompositeImageNode": CompositeImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CompositeImageNode": "🪐 Pluto : Composite Image"
}
