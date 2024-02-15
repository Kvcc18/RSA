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
