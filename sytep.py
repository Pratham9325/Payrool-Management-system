import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('employee.py', base=base, shortcutName='Employee Management System', shortcutDir='DesktopFolder')
]

setup(
    name="EmployeeManagementSystem",
    version="1.0",
    description="Employee Management System",
    executables=executables
)