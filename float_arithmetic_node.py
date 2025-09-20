import math
import builtins

class FloatArithmeticNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 1.0}),
                "b": ("FLOAT", {"default": 1.0}),
                "expression": ("STRING", {
                    "multiline": False,
                    "default": "(a * b) / 1.5"
                }),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "evaluate"
    CATEGORY = "Custom/Math"

    def evaluate(self, a, b, expression):
        safe_globals = {
            "__builtins__": {},
            "a": a,
            "b": b,
            "math": math,
            **{k: getattr(math, k) for k in dir(math) if not k.startswith("_")},
            **{k: getattr(builtins, k) for k in ("abs", "min", "max", "round")}
        }

        try:
            result = eval(expression, safe_globals)
            if not isinstance(result, (int, float)):
                raise ValueError("Expression must return a number.")
            return (float(result),)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {e}")

NODE_CLASS_MAPPINGS = {
    "FloatArithmeticNode": FloatArithmeticNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FloatArithmeticNode": "🪐 Pluto : Float Math"
}