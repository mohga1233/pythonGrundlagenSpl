import random
zufallszahl = random.randint(1,101)

print("Zahlenerraten")
print("Errate meine Zahl zwischen 1 und 100")
versuche = 0

gewonnen = False

while gewonnen == False:
  zahl = int(input("Welche Zahl? "))
  versuche = versuche + 1
  if(zahl == zufallszahl):
    print("Du hast die Zahl erraten.")
    gewonnen = True
  elif (zahl < zufallszahl):
    print("Die gesuchte Zahl ist größer. Bitte versuchen Sie es erneut.")
    
  elif (zahl > zufallszahl):
    print("Die gesuchte Zahl ist kleiner. Bitte versuchen Sie es erneut.")
    
print("Anzahl der Versuche: ", versuche)