import os
import shutil

shortcut_name = "Habit Hero Game.lnk"
shortcut_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "main.exe")
shortcut_location = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

shutil.copy(shortcut_target, os.path.join(shortcut_location, shortcut_name))
