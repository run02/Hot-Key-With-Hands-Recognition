from abstract_layer import ShortcutLayerInterface
from file_resource_management import FileResources
import keyboard


class ShortcutLayer(ShortcutLayerInterface):
    def trigger_shortcut(self, key):
        if key is not None and (key in FileResources.gestures2shortcuts.keys()):
            value=FileResources.gestures2shortcuts[key]
            if not (value == '' or value == 'nothing'):
                keyboard.press_and_release(value)
                print(value)


shortcut = ShortcutLayer()
