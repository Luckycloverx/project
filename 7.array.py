from array import *
def main():
    value = array('i', [])
    even_count, odd_count = 0, 0

    number = int(input("Size of integer array: "))
    for i in range(number):
        try:
            nilagay = int(input('Input number: '))
            value.append(nilagay)
        except ValueError:
            print("*********************************************")
            print("please input integer only..")
            print("*********************************************")
    #getting the sum of all elements
    add = sum(value)

    #printing of all input numbers in array
    print("Input elements: ", *value)

    # print all the sum of input numbers
    print("the sum of elements: ", add)

    #slice the array into half
    slice_arr = value[::2]
    for num in slice_arr:
       #even numbers
       if num % 2 == 0:
          even_count += 1
       #odd numbers
       else:
          odd_count += 1
    print("The half element slice in array:", *slice_arr )
    print("even in slice array:", even_count )
    print("odd in slice array:", odd_count )

    #reversing array
    value.reverse()
    print("Reverse Array: ", *value)

    #Display the element of the array by two's
    arr_1 = value[1::2]
    arr_2 = value[::2]
    avg_1 = sum(arr_1)/len(arr_1)
    avg_2 = sum(arr_2)/len(arr_2)
    print("display the element of the array by two's= ", *arr_1 , "and" , *arr_2)
    print("the 1st : ", round(avg_1))
    print("the second: ", round(avg_2))

    restart = input("\nTry Again?[y/n]: ")
    if restart == 'Y' or restart == 'y':
        main()
    else:
        exit()


main()