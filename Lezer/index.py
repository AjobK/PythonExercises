condition = True

while True:
    Content = str(input("Wat wilt U in het text element zetten?\n"))

    Bestand1 = open("index.txt", "w")
    Bestand1.write(Content)
    Bestand1.close()

    Bestand1 = open("index.txt")
    Bestand1.close()

    print("========================")
    print("Bestand succesvol gevuld")
    print("========================")

    vraag = int(input("Wat wilt U doen?\n1. Verandering aanbrengen\n2. Lezen\n3. Sluiten\n"))

    if vraag == 1:
        continue
    elif vraag == 2:
        Bestand1 = open("index.txt")
        print("Content:", Bestand1.read())
        Bestand1.close()
        continue
    else:
        print("\nU koos niet 1. Start het programma opnieuw op om verandering aan te brengen")
        break
