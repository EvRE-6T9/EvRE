import os, sys
os.system("git pull")
try:
    __import__("EVRE").menu()
except Exception as e:
    exit(str(e))
