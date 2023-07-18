from base64 import b64encode

# Use to encrypt connection settings.

# This is a simple method of storing credentials in a "safe" way that should 
# be replaced by a more powerful one. It is recommended to delete this file 
# and replace security mechanism.

server = "111.11.111.11:111" 
user = "username"
password = "password"
encoded_server = b64encode(server.encode("utf-8")).decode("utf-8")
encoded_user = b64encode(user.encode("utf-8")).decode("utf-8")
encoded_password = b64encode(password.encode("utf-8")).decode("utf-8")

print("server:", encoded_server)
print("user:", encoded_user)
print("passw:", encoded_password)