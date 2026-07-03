import bcrypt

try:
    passcode = input("Password: ")
    encrypt = bcrypt.hashpw(passcode.encode('utf-8'), bcrypt.gensalt())
    print(f"Encrypted Password: {encrypt.decode('utf-8')} and passcode: {passcode}")
    
except Exception as e:
    print(f"Error: {e}")
