while True:
    toplam = 0
    girdi = input('Please enter a positive number to see if the number you entered is an Armstrong number : ')
    if ("," in girdi) or ("." in girdi):
        print(" Please enter an integer number")
    elif ("-" in girdi):
        print(" Please enter a positive number")
    elif not girdi.isdigit():
        print("Do not use any entries other than numeric values")
    else:
        for i in range(len(girdi)):
            toplam += int(girdi[i]) ** (len(girdi))
        if int(girdi) == int(toplam):
            print(girdi+" is an Armstrong number")
        else:
            print(girdi+" is not an Armstrong number")
        break
       

            
        