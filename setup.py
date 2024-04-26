import cx_Freeze
import os

desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

icon_path = 'icon.ico'

executables = [
    cx_Freeze.Executable('main.py', base="Win32GUI", icon=icon_path)
]

cx_Freeze.setup(
    name="Habbit Hero Game",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                'Player',
                'assets',
                'assets\\images',
                'assets\\audio\\',
                'assets\\images\\quit.jpeg',
                'assets\\images\\loading.jpeg',
                'assets\\images\\zero_to_hero.jpeg',
                'assets\\audio\\superhero-trailer-110450.mp3',
                'assets\\images\\icon.jpeg',
                'assets\\hangman\\hangman0.png',
                'assets\\hangman\\hangman1.png',
                'assets\\hangman\\hangman2.png',
                'assets\\hangman\\hangman3.png',
                'assets\\hangman\\hangman4.png',
                'assets\\hangman\\hangman5.png',
                'assets\\hangman\\hangman6.png',
                'assets\\lines\\line.png',
                'BLANKA Font\\Blanka-Regular.otf',
                'Player\\players.txt'
            ]
        },
        "bdist_msi": {
            "install_icon": icon_path,  # Icon for the installer
            "initial_target_dir": desktop_dir,  # The user's desktop as the target directory
            "target_name": "HabbitHeroGameInstaller"  # Name of the installer file
        }
    },
    executables=executables,
    install_requires=['cx_Freeze']
)
