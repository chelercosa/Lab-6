# alyss santiago

def encoded(password):
    encoded_password = []
    for i in range(len(password)):
        encoded_number = int(password)
        encoded_password.append(str(encoded_number)) + 3
        encoded_password = ''.join(encoded_password)
    return encoded_password

# def decoded(password):
#     decoded_password = []
#     for i in range(len(password)):
#         decoded_password.append(str(int(password[i] - 3)))
#     return decoded_password

def main():
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = int(input("Please enter your password to encode: "))
            # print(encoded_password)
            encoded_password = encoded(password)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            #decode
            print(f"The encoded password is ", decoded, ", and the original password is ", password, ".")
        elif user_input == 3:
            break


if __name__ == '__main__':
    main()
