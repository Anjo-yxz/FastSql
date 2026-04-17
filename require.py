import sys
import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir(pasta_atual)

try:

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Esta entrando\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python DARK_URUMA_PAINEL.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Esta entrando\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 DARK_URUMA_PAINEL.py")

except Exception as e:
    input(e)