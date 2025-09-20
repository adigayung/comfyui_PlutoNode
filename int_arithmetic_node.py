import math
import builtins

class IntArithmeticNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("INT", {"default": 1}),
                "b": ("INT", {"default": 1}),
                "expression": ("STRING", {
                    "multiline": False,
                    "default": "(a * b) / 2"
                }),
            },
        }

    RETURN_TYPES = ("INT",)
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
            return (int(result),)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {e}")

NODE_CLASS_MAPPINGS = {
    "IntArithmeticNode": IntArithmeticNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IntArithmeticNode": "🪐 Pluto : Int Math"
}
