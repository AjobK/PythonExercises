while True:
    x = int(input("Tot de macht van?\n"))
   
    lijst = [i**x for i in range(20) if i%5 == 0]
    
    print(lijst)
