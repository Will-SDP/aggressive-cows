import sys
# from aggressive_cows_method1 import aggressive_cows
from aggressive_cows_method2 import aggressive_cows
from error_codes import Error

## 1 4 6 7 10


if __name__ == "__main__":
    e = Error()
    print("###### Aggressive Cow Problem ######")
    print("------------------------------------")
    input_str = input("Enter stalll coordinates seperated by a space: ")
    input_cows = input("Enter number of cows: ")

    try:
        input_cows = int(input_cows)
    except:
        print("Please enter a number!")
        sys.exit(0)    

    try:
        input_arr = [] 
        for c in input_str.split(' '):
            input_arr.append(int(c))
    except:
        print("List of coordinates should be seperated by a space.")        

    res = aggressive_cows(input_arr, input_cows)
    if res < 0:
        print(f"Error: {e.get_error(res)}")
    else:    
        print(f"The maximum spacing for {input_cows} cows is {res}")