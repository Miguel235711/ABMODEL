from cx_Freeze import setup, Executable
import sys
sys.path.append('../Menu')
import menuMain
sys.path.append('../Registration')
import registrationMain
sys.path.append('../Log-In')
import LogInMain
sys.path.append('../UserMenu')
import userMenu
sys.path.append('../Grapher')
import state
import container
sys.path.append('../Data/Reader')
import file

build_exe_options = {"packages": ["os"], "includes": ["PyQt5"], "excludes": ["tkinter","ibopenblas.TXA6YQSD3GCQQC22GEQ54J2UDCXDXHWN.gfortran-win_amd64.dll"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = 'appname',
    version = '1',
    description = '.',
    executables=[Executable('main.py', base=base)],
    options={"build_exe":build_exe_options},
)