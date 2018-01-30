def characterCounter(textfile, letter):
    counter = 0
    for i in text:
        if i == letter:
            counter += 1
    print("\n'{0}' was found {1} times in: \n{2}.".format(letter, counter, text))

while True:
    try:
        choices = input("\nOpen a file like this: (filename,letter)\nFile: ").split(",") #Case sensitive
        textf = str(choices[0]) + ".txt" #Type is automatically added
        with open(textf) as file:
            text = file.read()
        try:
            characterCounter(textf, choices[1])
        except IndexError:
            print("ERROR: You forgot to choose a character :(")
            continue
    except FileNotFoundError:
        print("ERROR: File not found :(")
        continue

#Opdracht 1 door A. Kustra