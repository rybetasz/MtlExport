import sys
from cx_Freeze import setup, Executable

main_file = 'MTLExport.py'

executable = Executable(script=main_file, base='Win32GUI', icon='mtlexport.ico')


setup(
    name='MTLExport',
    version='1.0',
    description='MTL Export Tool',
    executables=[executable],
    options={
        'build_exe': {
            'packages': ['tkinter'],
            'include_files': ['mtlexport.ico']
        }
    }
)
