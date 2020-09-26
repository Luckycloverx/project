def main():
    print ("\n||   Letter Grade    ||      Remarks      ||")
    print ("||         A         ||     Excellent     ||")
    print ("||         B         ||     Very Good     ||")
    print ("||         C         || Very Satisfactory ||")
    print ("||         D         ||   Satisfactory    ||")
    print ("||         E         ||       Fair        ||")
    print ("||         F         ||     Incomplete    ||")
    print ("||         G         ||     Conditional   ||")
    print ("||         H         ||       Failed      ||")
    letter = input ("\nType the letter of your grade: ")

    if letter == 'A' or letter== 'a':
        print("------------------------------")
        print("     [REMARKS = EXCELLENT]    ")
        print("------------------------------")
    elif letter == 'B' or letter== 'b':
        print("------------------------------")
        print("     [REMARKS = VERY GOOD]    ")
        print("------------------------------")
    elif letter == 'C' or letter== 'c':
        print("------------------------------")
        print("[REMARKS = Very Satisfactory] ")
        print("------------------------------")
    elif letter == 'D' or letter== 'd':
        print("------------------------------")
        print("    [REMARKS = Satisfactory]  ")
        print("------------------------------")
    elif letter == 'E' or letter== 'e':
        print("------------------------------")
        print("      [REMARKS = Fair]        ")
        print("------------------------------")
    elif letter == 'F' or letter== 'f':
        print("------------------------------")
        print("   [REMARKS = Incomplete]     ")
        print("------------------------------")
    elif letter == 'G' or letter== 'g':
        print("------------------------------")
        print("    [REMARKS = Conditional]   ")
        print("------------------------------")
    elif letter == 'H' or letter== 'h':
        print("------------------------------")
        print("      [REMARKS = Failed]      ")
        print("------------------------------")
    else:
        print("------------------------------")
        print("[Letter grade are A to H only]")
        print("------------------------------")

    restart=input ("\nTry Again?[y/n]: ")
    if restart=='Y' or restart=='y':
        main()
    else:  
        exit()
main()        
    
