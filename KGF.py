import os, sys
os.system("git pull")
try:
    __import__("Enc").XYZ()
except Exception as e:
    exit(str(e))
