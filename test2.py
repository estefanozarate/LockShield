import json

with open('encrypted_message.json') as f:
    data = json.load(f)

name = data["google"]
print(f"google password{name}")  
