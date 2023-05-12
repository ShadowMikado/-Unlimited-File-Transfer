import os
from utils.Config import Config


config = Config()
def start_ngrok(port:int):
    os.system(f"ngrok.exe http {port}")

    return
start_ngrok(config.get("Port"))
