#Práctica de algoritmo RSA

#Cifrado de mensaje

#2024-02-14 - Anáhuac Mayab

#Imports
import Crypto.Util.number

#Número de bits
bits = 1024

#Obtener los primos para Alice y Bob

pA = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Alice", pA, "\n")

qA = Crypto.Util.number.getPrime(bits, randfunc =  Crypto.Random.get_random_bytes)
print("Primo de Alice", qA, "\n")
