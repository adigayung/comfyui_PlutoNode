from typing import Tuple
import re

class TextReplaceNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "find_list": ("STRING", {"multiline": True, "default": "men, fat"}),
                "replace_list": ("STRING", {"multiline": True, "default": "girl, slim"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "replace_text"
    CATEGORY = "Custom/Text"

    def replace_text(self, text: str, find_list: str, replace_list: str) -> Tuple[str]:
        find_items = [f.strip() for f in find_list.split(",") if f.strip()]
        replace_items = [r.strip() for r in replace_list.split(",")] if replace_list.strip() else []

        # Samakan panjang list
        if len(replace_items) < len(find_items):
            replace_items.extend([""] * (len(find_items) - len(replace_items)))
        elif len(replace_items) > len(find_items):
            replace_items = replace_items[:len(find_items)]

        output_text = text
        for f, r in zip(find_items, replace_items):
            output_text = output_text.replace(f, r)

        # Bersihkan koma ganda tanpa spasi
        output_text = self._clean_commas(output_text)

        return (output_text,)

    def _clean_commas(self, text: str) -> str:
        # Ganti koma ganda dengan spasi opsional di antara → satu koma saja
        text = re.sub(r',\s*,+', ',', text)
        # Bersihkan koma di awal/akhir
        text = text.strip(',')
        return text

# Daftarkan ke ComfyUI
NODE_CLASS_MAPPINGS = {
    "TextReplaceNode": TextReplaceNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextReplaceNode": "🪐 Pluto : Text Replace"
}
