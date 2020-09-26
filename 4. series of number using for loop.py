print ("*********************************************")
count = 1
while count == 1:
    try:
        number = int (input("Input positive number: "))
        if number <= 0:
            print ("*********************************************")
            print("terminated")
            break
    except ValueError:
        print("please input integer only..")
        continue

