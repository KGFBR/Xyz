import os, sys
os.system("git pull")
try:
    __import__("Xyz").Xyz()
    
except Exception as e:
    exit(str(e))
