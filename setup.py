# Check what os is this running under and run the appropriate setup script for that os
# for getting the operating system name (and other system info)
import platform as pl
import subprocess       # for executing a shell command
import sys              # for getting the python version
import os               # for getting the current working directory

# Get the current working directory
cwd = os.getcwd()

# Get the operating system name
os_name = pl.system()

# Get the operating system release
os_release = pl.release()

# Get the operating system architecture
os_arch = pl.machine()

# Get the operating system version
os_version = pl.version()

# Get shell details
shell_details = subprocess.run(
    ["echo $SHELL"], shell=True, capture_output=True, text=True)

# find out if we are running shell, powershell or cmd
if shell_details.stdout == "/bin/bash\n":
    shell = "bash"
elif shell_details.stdout == "/bin/zsh\n":
    shell = "zsh"
elif shell_details.stdout == "/bin/fish\n":
    shell = "fish"
elif shell_details.stdout == "/bin/csh\n":
    shell = "csh"
elif shell_details.stdout == "/bin/ksh\n":
    shell = "ksh"

# find out what the shell is
if shell == "bash":
    shell_details = subprocess.run(
        ["bash --version"], shell=True, capture_output=True, text=True)
elif shell == "zsh":
    shell_details = subprocess.run(
        ["zsh --version"], shell=True, capture_output=True, text=True)
elif shell == "fish":
    shell_details = subprocess.run(
        ["fish --version"], shell=True, capture_output=True, text=True)
elif shell == "csh":
    shell_details = subprocess.run(
        ["csh --version"], shell=True, capture_output=True, text=True)
elif shell == "ksh":
    shell_details = subprocess.run(
        ["ksh --version"], shell=True, capture_output=True, text=True)

# Find out if we are running on a mac or windows
if os_name == "Darwin":
    # Run the macos setup script
    exec(open("setup_macos.py").read())
elif os_name == "Windows":
    # Run the windows setup script
    exec(open("setup_windows.py").read())
elif os_name == "Linux":
    # Run the linux setup script
    exec(open("setup_linux.py").read())


# Get the python version
py_version = sys.version

# Get the python executable path
py_exec = sys.executable

# Get the python path
py_path = sys.path

# Get the python version info
py_version_info = sys.version_info

# Get the python prefix
py_prefix = sys.prefix

# Get the python platform
py_platform = sys.platform

# Get the python implementation
py_implementation = sys.implementation


# Print the system info
print()
print("System Info")
print("-----------")
print("Current Working Directory: ", cwd)
print("Operating System: ", os_name)
print("Operating System Release: ", os_release)
print("Operating System Architecture: ", os_arch)
print("Operating System Version: ", os_version)
print("Shell: ", shell)
print("Shell Details: ", shell_details.stdout.strip())
print("-----------")
print("Python Info")
print("-----------")
print("Python Version: ", py_version)
print("Python Executable: ", py_exec)
print("Python Path: ", py_path)
print("Python Version Info: ", py_version_info)
print("Python Prefix: ", py_prefix)
print("Python Platform: ", py_platform)
print("Python Implementation: ", py_implementation)
print()
