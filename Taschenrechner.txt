print("Taschenrechner")

zahl1 = input("Bitte geben Sie die erste Zahl ein: ")

zahl2 = input("Bitte geben Sie die zweite Zahl ein: ")

operation = input("+ oder - oder * oder / rechnen? ")

if (operation == "/" and zahl2 == "0"):
  print("Rechnen mit 0 ist nicht möglich",)
  exit()
  


  
if (operation == "+"):
  summe = float(zahl1) + float(zahl2)
  print("Summe = ",summe)
  
if (operation == "-"):  
  differenz = float(zahl1) - float(zahl2)
  print("Differenz =",differenz)
  
if (operation == "*"):
  multipikation = float(zahl1) * float(zahl2)
  print("Multipikation = ", multipikation)
  
if (operation == "/"):
  dividsion = float(zahl1) / float(zahl2)
  print("Dividsion = ", dividsion)
