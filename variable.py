#Variabe
'''
a =10
b = 20
summe = a+b

print(" Summe von " , a , "+" ,b , " = " ,summe)

aktion = input("Welche aktion willst du ? (+/-/*/:)")
print("Aktion ", aktion, "wird ausgeführt")

if (aktion == "*")
    print("Mutliplikation ausgewählt")
zahl = input("Welche Zahl wählst du ?")
zahl = int(zahl)

zahl2 = int("23")
zahlA = "123"
zahlB="456"
print(zahlA + zahlB)
'''
zahl1 = input("Geben sie eine zahl ein")
aktion = input("Geben sie eine aktion ein(+/-/*/:)")
zahl2 = input("Geben sie noch eine zahl ein")

zahl1=int(zahl1)
zahl2=int(zahl2)


if (aktion == "+"):
    ergebnis = zahl1+zahl2
if (aktion == "-"):
    ergebnis = zahl1-zahl2
if (aktion == "*"):
    ergebnis = zahl1*zahl2
if( aktion == ":"):
    ergebnis = zahl1/zahl2

print(ergebnis)
