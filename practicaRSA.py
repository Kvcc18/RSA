from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import hashlib

# Generar una clave RSA de   1024 bits
bits=1024

msg = 'A message'

print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes: ", len(msg.encode('utf-8')))

#Convertir el mensaje a número
m = int.from_bytes(msg.encode('utf-8'), byteorder = 'big')
print("Mensaje convertido en entero: ", m, "\n")

hash_object = hashlib.sha256(msg.encode())
hex_dig = hash_object.hexdigest()
print("Hash del mensaje: ", hex_dig, "\n")

m = int(hex_dig,  16)
print("Hash convertido en entero: ", m, "\n")

with open('hash.pdf', 'rb') as pdf_file:
    pdf_content = pdf_file.read()

hash_obj = hashlib.sha256(pdf_content)
digest = hash_obj.digest()

signature = pow(digest, pdf_content)
print("Firma: ", signature, "\n")