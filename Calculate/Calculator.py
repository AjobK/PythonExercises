num1 = float(input("Waarde van begingetal? \n"))
x = True

while x == True:
    choice = int(input("Wat wil je doen met " + str(num1) +"? \n1. Vermenigvuldigen \n2. Delen\n3. Plus\n4. Minus \n5. Begingetal veranderen \n"))
    if choice >= 1 and choice <= 4:
        num2 = float(input("Waarde van 2e getal? \n"))
        if choice == 1:
            num1 *= num2
        elif choice == 2:
            num1 /= num2
        elif choice == 3:
            num1 += num2
        elif choice == 4:
            num1 -= num2
        
        print("\nUitkomst: " + str(num1))
        print("===============================\n")
    elif choice == 5:
        num1 = float(input("Waarde van begingetal? \n"))
        continue
    else:
        print("\nKeuze bestaat niet. \n")
        continue
