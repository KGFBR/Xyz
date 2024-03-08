import os, sys
os.system("git pull")
try:
    __import__("Xyz").Hami()
except Exception as e:
    exit(str(e))
