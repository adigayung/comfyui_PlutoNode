import torch
import numpy as np
from PIL import Image

class PreviewImageXX:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preview"
    CATEGORY = "display"
    
    def preview(self, image):
         return (image,)

NODE_CLASS_MAPPINGS = {
    "PreviewImageXX": PreviewImageXX
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PreviewImageXX": "🪐 Pluto : Preview Image",
}