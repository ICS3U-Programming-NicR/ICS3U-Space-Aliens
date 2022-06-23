import storage
import ugame

keys = ugame.buttons.get_pressed()
if keys & ugame.K_X:
    storage.remount("/", True)
else:

    storage.remount("/", False)
