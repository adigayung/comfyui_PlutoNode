from . import image_info_nodes
from . import image_latent_nodes
from . import image_save_nodes
from . import image_preview_pluto
from . import auto_crop_face_node
from . import text_append_node
from . import text_replace_node
from . import float_arithmetic_node
from . import float_to_int_node
from . import int_arithmetic_node
from . import text_to_image_node
from .composite_image_node import CompositeImageNode


NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(image_info_nodes.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(image_info_nodes.NODE_DISPLAY_NAME_MAPPINGS)


NODE_CLASS_MAPPINGS.update(image_latent_nodes.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(image_latent_nodes.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(image_save_nodes.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(image_save_nodes.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(image_preview_pluto.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(image_preview_pluto.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(auto_crop_face_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(auto_crop_face_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(text_append_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(text_append_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(text_replace_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(text_replace_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(composite_image_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(composite_image_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(float_arithmetic_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(float_arithmetic_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(float_to_int_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(float_to_int_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(int_arithmetic_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(int_arithmetic_node.NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(text_to_image_node.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(text_to_image_node.NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
