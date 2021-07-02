def main():
    ask_string = input("Give a string:")
    ask_int = int(input("Give an integer:"))
    ask_float = float(input("Give a float:"))
    ask_boolean = bool(input("Give a boolean:"))#write your code below this line

    print("You gave the string " + ask_string)
    print("You gave the integer " + str(ask_int))
    print("You gave the float " + str(ask_float))
    print("You gave the boolean " + str(ask_boolean))
if __name__ == '__main__':
    main()
