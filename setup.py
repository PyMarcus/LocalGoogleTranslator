from cx_Freeze import setup, Executable
from platform import system


"""Constroí executavel, para linux ou windows"
base = None
if system() == "Windows":
    base = "Win32Gui"

setup(
    name="MarcusTranslator_kkk",
    version="1.0.0",
    description="Tradutor que traduz",
    options={
        'build_exe':{
            'includes':['tkinter', 'ttkbootstrap']
        }
    },
    executables=[
        Executable('translator.py', base=base)
    ]

)