#primzahlen
#Funktion: check if given number is prime

def isPrime(n):
    #logik einbauen
    if (n<=1):
        return False
    for p in range(2,n):
        if(n % p == 0):
            return False

    return True

print("Primzahlen-Checker")
z = input("Bitte die zahl eingeben: ")
z = int(z)
if(isPrime(z)):
    print(z , "ist eine Primzahl")
else:
    print(z , "Ist KEINE Primzahl")
