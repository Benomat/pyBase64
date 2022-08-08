import base64
from pyperclip import copy

message = open("hash.py", "r",encoding='utf-8').read()
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)
copy(base64_message)
print("Code has been copied")
