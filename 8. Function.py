def main():
    primary = []
    leng = []

    #Main function
    num_color = int(input("number of colors: "))
    for i in range(num_color):
            input_color = input("Input Primary Color: ")
            primary.append(input_color)
            leng.append(len(input_color))

    print("List of primary color: ", primary)
    print("length of every color: ", leng)

    primary.sort()
    print("Sorted Color: ", primary)

    primary.sort(reverse=True)
    print("Reverse: ", primary)

    for i in range(len(primary)):
       if i % 2 != 0:
            del primary[0:1]

    print("display last half: ", primary)

    restart=input ("\nTry Again?[y/n]: ")
    if restart=='Y' or restart=='y':
        main()
    else:
        exit()
main()
