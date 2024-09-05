import os

def ps1run(payload):
    a = "powershell -e " + base64.b64encode(payload.encode("utf-16")[2:]).decode()
    os.system(a)
