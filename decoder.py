import base64
import json

try:
    pas = input("decode password: ")
    if pas == "":
        raise ValueError("Password cannot be empty")
    pas = pas.encode('ascii')
    base = base64.b64decode(pas)
    bas = base.decode('ascii')
    print(json.dumps({"password": bas}))

except Exception as e:
    print(f"Error: {e}")
