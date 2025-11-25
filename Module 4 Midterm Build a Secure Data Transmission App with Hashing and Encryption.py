#Lana Hendrickson
#Module 4 Midterm: Build a Secure Data Transmission App with Hashing and Encryption

#imports
import hashlib
from cryptography.fernet import Fernet

#input
#256 code
fileTXT = open("message.txt")
string = fileTXT.read()

result = hashlib.sha256(string.encode())
shaCode = result.hexdigest()

#Symmetric encryption Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(string.encode())

#decripting
newCode = f.decrypt(token)
newMessage = newCode.decode('utf-8')

resultNew = hashlib.sha256(newMessage.encode())
checkCode = resultNew.hexdigest()


#output
if checkCode == shaCode:
    print(newMessage)
else:
    print("A error has occured")


