#Name: Arthur Gigot

def decode(code):
    pass

def encode(initial):
    global code = ""
    for i in range(0,len(initial)):
        code += str((int(initial[i])+3)%10)
    print("Your password has been encoded and stored!")        

def main():
    while True:
	print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        option = input("Please enter an option: ")
        if option=="1":
	    initial = ("Please enter your password to encode: ")
            encode(initial)
	if option=="2":
	    print(f"The encoded password is {decode(code)}, and the original password is {initial}"
	if option=="3":
	    break

if __name__ == "__main__":
    main()

