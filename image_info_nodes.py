# comfyui-PatchNodes/image_info_nodes.py

class PlutoGetSizeFromImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"

    CATEGORY = "Pluto/Image"

    def get_size(self, image):
        if hasattr(image, "shape"):
            height, width = image.shape[1], image.shape[2]
            return (width, height)
        else:
            raise ValueError("Unsupported image format: missing shape attribute")


NODE_CLASS_MAPPINGS = {
    "PlutoGetSizeFromImage": PlutoGetSizeFromImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PlutoGetSizeFromImage": "🪐 Pluto : GetSizeFromImage"
}
