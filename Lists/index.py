List = [1, 2, 3, 4, 5, 6]
Dictionary1 = {1:"One", 2:"Two", 3:"Three"}
Dictionary2 = {"Ikr":"I know right.", "Wtf":"What the fuck?", "ASL":"Age, sex, language"}
Tuple = (1, 2, 3)

if 1 in Dictionary1:
    print("Actief")
    print(Dictionary1.get(1, "Er klopt iets niet."))
else:
    print("Inactief")

print(List[0:2:1]) #Array_naam[Startpunt:Eindpunt:Stappen], dit sliced arrays
print(List[:2:]) #Sliced begin tot aangegeven eindpunt
print(List[2::]) #Sliced vanaf aangegeven startpunt tot eindpunt
print(List[::2]) #Sliced van begin tot eind, en springt met aangegeven stappen

""" NOTATIE:
    Als je de van de stap bij het slicen een negatief getal maakt,
    sliced hij reverse (Van eind tot begin). Ook moet je het eindpunt
    en begin punt omdraaien bij waardes. [0:2] wordt [2:0]
"""
