# comfyui_PlutoNode/image_latent_nodes.py

import torch

class PlutoEmptyLatentByInput:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT",),
                "height": ("INT",),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "generate_latent"

    CATEGORY = "Pluto/Latent"

    def generate_latent(self, width, height):
        latent = torch.zeros([1, 4, height // 8, width // 8])
        return ({"samples": latent},)


NODE_CLASS_MAPPINGS = {
    "PlutoEmptyLatentByInput": PlutoEmptyLatentByInput
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PlutoEmptyLatentByInput": "🪐 Pluto : Empty Latent By Input"
}
