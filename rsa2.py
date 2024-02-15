#Práctica de algoritmo RSA

#Cifrado de mensaje

#2024-02-14 - Anáhuac Mayab

#Imports
import Crypto.Util.number
import hashlib

#Número de bits
bits = 1024

#Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Alice", pA, "\n")

qA = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Alice", qA, "\n")

pB = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Bob", pB, "\n")

qB = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Bob", qB, "\n")

#Obtener la primera parte de la llave pública de Alice y Bob
nA = pA * qA
print("nA: ", nA, "\n")

nB = pB * qB
print("nB: ", nB, "\n")

#Calculamos el Indicador de Euler Phi
phiA = (pA - 1) * (qA - 1)
print("phiA: ", phiA, "\n")

phiB = (pB - 1) * (qB - 1)
print("phiB: ", phiB, "\n")

#Por razones de eficiencia usaremos el número 4 de Fernat: 65537, debido a que es 
#un primo largo y no es potencia de 2, y como forma parte de la clave pública, no es 
#necesario calcularlo
e = 65537

#Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(e, phiA)
print("dA: ", dA, "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dB: ", dB, "\n")

#Ciframos el mensaje
msg = 'hola mundo'
print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes: ", len(msg.encode('utf-8')))

#Convertir el mensaje a número
m = int.from_bytes(msg.encode('utf-8'), byteorder = 'big')
print("Mensaje convertido en entero: ", m, "\n")

#Ciframos el mensaje 
c = pow(m, e, nB)
print("Mensaje cifrado: ", c, "\n")

#Desciframos el mensaje 
des = pow(c, dB, nB)
print("Mensaje descifrado: ", des, "\n")

#Convertimos el mensaje de número a texto
msg_final = int.to_bytes(des, len(msg), byteorder = 'big').decode('utf-8')
print("Mensaje final: ", msg_final, "\n")

#Crear un hash del mensaje usando SHA-256
hash_object = hashlib.sha256(msg.encode())
hex_dig = hash_object.hexdigest()
print("Hash del mensaje: ", hex_dig, "\n")

#Convertir el hash a un número
m = int(hex_dig,  16)
print("Hash convertido en entero: ", m, "\n")

# Ciframos el hash con la clave privada de Alice
signature = pow(m, dA, nA)
print("Firma: ", signature, "\n")

#Descifrar firma
decrypted_signature = pow(signature, e, nA)
print("Firma descifrada: ", decrypted_signature, "\n")

#Convertimos la firma descifrada de número a texto (hash)
decrypted_hash = format(decrypted_signature, 'x')
print("Hash descifrado: ", decrypted_hash, "\n")

#Verificamos si el hash descifrado coincide con el hash original del mensaje
original_hash = hashlib.sha256(msg.encode()).hexdigest()
print("Hash original del mensaje: ", original_hash, "\n")

#Comparar el hash descifrado con el hash original
if decrypted_signature == m:
    print("La firma es válida.")
else:
    print("La firma no es válida.")


