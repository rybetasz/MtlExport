import sys
from cx_Freeze import setup, Executable

# Uygulamanın ana dosyasının adını ve yolu (MTLExport.py'yi kendi dosyanızın adıyla değiştirin)
main_file = 'MTLExport.py'

# cx_Freeze yapısında kullanılacak Executable nesnesini oluşturuyoruz
executable = Executable(script=main_file, base='Win32GUI', icon='mtlexport.ico')

# cx_Freeze setup fonksiyonunu çağırıyoruz
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
