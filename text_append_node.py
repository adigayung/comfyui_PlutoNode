class TextAppendNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": True}),
                "extra_text": ("STRING", {"multiline": True, "default": " - Appended!"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "append_text"
    CATEGORY = "Pluto/Text"

    def append_text(self, input_text, extra_text):
        return (input_text + extra_text,)


NODE_CLASS_MAPPINGS = {
    "TextAppendNode": TextAppendNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextAppendNode": "🪐 Pluto : Text Append"
}
