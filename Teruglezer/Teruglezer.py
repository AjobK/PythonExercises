#Importatie
import math
import random

#Geeft "HalloHalloHallo"
print("\n1. Strings & Numbers\n")
print(3 * "Hallo")

""" Operator notatie:
    // is delen en naar beneden afronden.
    ** is tot de macht
    % is modulo
    * is multiply
    / is divide
    + is add
    - is subtract

    Bitwise Operators
    https://wiki.python.org/moin/BitwiseOperators
"""

#Str, Float, Int
print("\n2. String, Float en Integer converters\n")
voorbeeld = 10

voorbeeld = str(voorbeeld)
print("String: " , voorbeeld)

voorbeeld = float(voorbeeld)
print("Float: " , voorbeeld)

voorbeeld = int(voorbeeld)
print("Integer: " , voorbeeld)

#If, Elif, Else
print("\n3. If, Elif & Else\n")
voorbeeld2 = 5

if voorbeeld2 > 5:
    print("Leuke sjit")
elif voorbeeld2 < 5:
    print("Leukere sjit")
else:
    print("Leukste sjit")

voorbeeld3 = "Leuks" #input("\n" + "Voer iets in \n")
print(voorbeeld3 + " is een leuke input")

voorbeeld3 *= 3
print(voorbeeld3 + " is een leukere input")

#If, Elif, Else (not, or, and)
print("\n4. If, Elif & Else (not, or, and)\n")
voorbeeld4 = 5

if voorbeeld4 > 6 or voorbeeld4 == 5:
    print("Leuke sjit")
elif voorbeeld4 > 4 and voorbeeld4 < 6:
    print("Leukere sjit")
elif not voorbeeld4 == 10:
    print("Niet tien")
else:
    print("Leukste sjit")

""" Opdracht 1
opdracht1 = input("\n" + "Grammatica maker, voer iets in \n")
print(opdracht1 , opdracht1 + "er", opdracht1 + "st")
"""

#Loops (While, for)
print("\n5. Loops \n")

teller = 1
while teller <= 3:
    print(teller, ", is leuk")
    teller += 1

teller = 1
while teller <= 3:
    print(str(teller) + " + is ook leuk")
    teller += 1

woorden = ["Leuk", "Intens", "Spannend"]
for woord in woorden:
    print(woord, ", inderdaad")

for i in range(1,4):
  print(str(i) + ". Zo kan het ook!")

#Arrays
print("\n6. Arrays \n")
lijst1 = [10, "Hallo", True]
print("Lijst 1:", lijst1)
print("Element[1] in lijst1:", lijst1[1])

print("Hallo in lijst1?:", "Hallo" in lijst1)
print("Doei in lijst1?:", "Doei" in lijst1)

lijst1.append("Leuk")
print("New Lijst 1:", lijst1)
print("Lijst length:", len(lijst1))

index = 1
lijst1.insert(index, "insertindex")
lijst1.insert(2, "insert2")
print(lijst1)
print("Position of Hallo =", lijst1.index("Hallo"))

lijst2 = list(range(1,6,1)) #list(range(startpunt, eindpunt-1, spronggrootte))
print(lijst2)
print("range(20) is het zelfde als range(0,20):", range(20) == range(0,20))

#Functions
print("\n7. Functions \n")
print("F1. my_Func \n")
def my_Func(fInput):
    lijst = range(9)
    emptyvar = ""
    for word in lijst:
        emptyvar += str(word) + str(fInput) + "\n"
    print(emptyvar)

variableFunc = my_Func

print(variableFunc(10))

def my_Func2(func, idk):
    return func(idk)

print(my_Func2(my_Func, "Hello"))

#Errors
print("\n8. Errors \n")
try:
   num1 = 7
   num2 = 0
   print(num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")
finally:
    print("Laatste statement")

print("\n1. Krijg een error door 'raise ValueError' bijv. te gebruiken")
print("2. Check correct gebruik door 'assert (1 == 3), \"Foutmelding!\"' bijv. te gebruiken")
#raise ValueError

#Opening Files
print("\n9. Opening files \n")
""" open("filename.txt", "w") is Write mode
    open("filename.txt", "r") is Read mode
    open("filename.txt", "a") is Append mode

    Als je een "b" toevoegt bij de mode dan wordt het binary mode.
    (Gebruikt voor bijv. images and sound files, moeten ook .bin files
    zijn).

    file_name.close() om file te sluiten

    enevariabele = open("filename.txt", w)
    print(enevariabele.write())
    ^ Dit geeft lengte van de text. (1 teken is 1 byte)
"""
txtContent = "Rozen zijn rood, Violen zijn blauw, Koelkast"
mijnBestand = open("test.txt", "w")
mijnBestand.write(txtContent)
mijnBestand.close()

mijnBestand = open("test.txt")
print(mijnBestand.read())
mijnBestand.close()

print("\n10. String formatting, String & Numeric & List Functions \n")
"""
    Theorie 1
    
    BELANGRIJKE STRING FUNCTIONS
    "what".join(what) # "what" kan bijvoorbeeld "," zijn. Dan word elk element in de array gesplitst met ","
    sample.replace(what, with)
    sample.split(",")
    sample.startswith("Element waarmee iets hoort te starten.") #Wordt true or false
    sample.endswith("Element waarmee iets hoort te eindigen.") #Wordt true or false
    sample.upper() #uppercase
    sample.lower() #lowercase
    print("test"[2:3]) #Slice

    BELANGRIJKE NUMERIC FUNCTIONS
    min([1,2,3,4,5]) #Geeft 1
    max([1,2,3,4,5]) #Geeft 4
    abs(-99) #Geeft 99, aantal stappen tot 0
    sum([1,2,3,4,5]) #Geeft 15, totaal van een lijst
    round(1.5) #Rond het getal af

    BELANGRIJKE LIST FUNCTIONS
    all(i > 5 for i in [2,3,4,5,6]) #False, omdat niet alles groter is dan 5
    any(i > 5 for i in [2,3,4,5,6]) #True, omdat er minstens één element groter is dan 5
    enumerate([1,2,3,4])
"""

arraysf = [1,2,3,4,5]
msg = "Ik vind {0}{0}{0} een heel mooi getal, maar {1} en {2} zijn ook vrij leuk.".format(arraysf[1],arraysf[0],arraysf[3])
msg2 = "Ik vind {x}{y}{x} een heel mooi getal, maar {y} en {z} zijn ook vrij leuk.".format(x = arraysf[1],y = arraysf[0],z = arraysf[3])
print(msg)
print(msg2)

if all(i > 5 for i in [2,3,4,5,6]):
    print("\nAlle elementen zijn groter dan 5") #False, omdat niet alles groter is dan 5

if any(i > 5 for i in [2,3,4,5,6]):
    print("\nMinstens één element is groter dan 5") #True, omdat er minstens één element groter is dan 5

for v in enumerate([2,3,4,5,6]):
    print(v) #Drukt alle elementen met indexnummer van elementen af.

#ending = input("_________________________________\nDruk een knop in op af te sluiten \n")
