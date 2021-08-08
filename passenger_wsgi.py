import sys, os
INTERP = "/home/brumey3/fpproject.dreamhosters.com/venv/bin/python"
#INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())
from app import app as application
