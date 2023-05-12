import os
from utils.Config import Config


config = Config()
def create_server(port:int,path:str = None):
    if path:
        os.system(f"python -m http.server --directory {path} {port}")
    else:
        os.system(f"python -m http.server {port}")
    return

try:
    create_server(config.get("Port"), config.get("Directory"))
except Exception:
    print('There is an ERROR')
