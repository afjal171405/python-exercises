# Write a Python program to find out what version of Python you are using.

# using sys
import sys
print("python version check with sys")
print(sys.version)
print("python version info with sys")
print(sys.version_info)

# using platform
import platform
print("python version check with platform")
print(platform.python_version())
# Python version as tuple (major, minor, patchlevel) of strings:
print(platform.python_version_tuple())