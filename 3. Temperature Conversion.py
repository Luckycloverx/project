def main():
    print("------------------------------")
    print("[1]Celsius to Fahrenheit")
    print("[2]Celsius to Kelvin")
    print("[3]Fahrenheit to Celsius")
    print("[4]Fahrenheit to Kelvin")
    print("[5]kelvin to Fahrenheit")
    print("[6]Kelvin to Celsius")
    print("------------------------------")
    while True:
        try:
            pili = int (input("Conversion number: "))
            print("------------------------------")
            if pili == 1:
               print("******************************")
               print("[1]Celsius to Fahrenheit")
               while True:
                   try:
                       number = int(input("Enter number in Celsius: "))
                       break
                   except ValueError:
                       print("please input integer only..")
                       continue
               output = ((number/5)*9)+32
               print("------------------------------")
               print("Fahrenheit Equivalent",output)
               print("******************************")
            elif pili == 2:
                print("******************************")
                print("[2]Celsius to Kelvin")
                while True:
                    try:
                        number = int(input("Enter number in Celsius: "))
                        break
                    except ValueError:
                        print("please input integer only..")
                        continue
                output = number + 273.15
                print("------------------------------")
                print("Kelvin Equivalent",output)
                print("******************************")
            elif pili == 3:
                print("******************************")
                print("[3]Fahrenheit to Celsius")
                while True:
                    try:
                        number = int(input("Enter number in Fahrenheit: "))
                        break
                    except ValueError:
                        print("please input integer only..")
                        continue
                output = (number - 32)*5/9
                print("------------------------------")
                print("Celsius Equivalent",output)
                print("******************************")
            elif pili == 4:
                print("******************************")
                print("[4]Fahrenheit to Kelvin")
                while True:
                    try:
                        number = int(input("Enter number in Fahrenheit: "))
                        break
                    except ValueError:
                        print("please input integer only..")
                        continue
                output = (number - 32)*5/9+273.15
                print("------------------------------")
                print("Kelvin Equivalent",output)
                print("******************************")
            elif pili == 5:
                print("******************************")
                print("[5]Kelvin to Fahrenheit")
                while True:
                    try:
                        number = int(input("Enter number in Kelvin: "))
                        break
                    except ValueError:
                        print("please input integer only..")
                        continue
                output = (number - 273.15)*9/5+32
                print("------------------------------")
                print("Fahrenheit Equivalent",output)
                print("******************************")
            elif pili == 6:
                print("******************************")
                print("[6]Kelvin to Celsius")
                while True:
                    try:
                        number = int(input("Enter number in Kelvin: "))
                        break
                    except ValueError:
                        print("please input integer only..")
                        continue
                output = number - 273.15
                print("------------------------------")
                print("Celsius Equivalent",output)
                print("******************************")
            else:
                print("Please choose 1-6 only")
            break
        except ValueError:
            print("please input integer only..")
            continue
    restart=input ("\nTry Again?[y/n]: ")
    if restart=='Y' or restart=='y':
        main()
    else:  
        exit()        
main()
