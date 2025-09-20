import math

class FloatToIntNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 1.0}),
                "rounding": (["int", "round", "floor", "ceil"],),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int_value",)
    FUNCTION = "convert"
    CATEGORY = "Custom/Math"

    def convert(self, value, rounding="int"):
        if rounding == "int":
            result = int(value)
        elif rounding == "round":
            result = round(value)
        elif rounding == "floor":
            result = math.floor(value)
        elif rounding == "ceil":
            result = math.ceil(value)
        else:
            raise ValueError(f"Unknown rounding method: {rounding}")
        return (result,)

NODE_CLASS_MAPPINGS = {
    "FloatToIntNode": FloatToIntNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FloatToIntNode": "🪐 Pluto : Float To Int"
}
