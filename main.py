# alyss santiago

def encoded(password):
<<<<<<< HEAD
    encoded_password = []
    for i in range(len(password)):
        encoded_number = int(password)
        encoded_password.append(str(encoded_number)) + 3
        encoded_password = ''.join(encoded_password)
    return encoded_password
=======
    encoded1_password = []
    acc_encoded_pass = []
    for i in range(len(password)):
        encoded_number = int(password[i]) + 3
        encoded1_password.append(str(encoded_number))
        acc_encoded_pass = ''.join((encoded1_password))
    return acc_encoded_pass
>>>>>>> da6b9f9 (i fixed your code and did decoded function, everything is working!)

# def decoded(password):
#     decoded_password = []
#     for i in range(len(password)):
#         decoded_password.append(str(int(password[i] - 3)))
#     return decoded_password
<<<<<<< HEAD

def main():
    while True:
=======
def decoder(password):
    decoded_password = []
    acc_decoded_pass = []
    for i in range(len(password)):
        decoded_num = int(password[i])-3
        decoded_password.append(str(decoded_num))
        acc_decoded_pass = ''.join((decoded_password))
    return acc_decoded_pass


def main():
    while True:
        global encoded_password

>>>>>>> da6b9f9 (i fixed your code and did decoded function, everything is working!)
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = int(input("Please enter your password to encode: "))
            # print(encoded_password)
<<<<<<< HEAD
            encoded_password = encoded(password)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            #decode
            print(f"The encoded password is ", decoded, ", and the original password is ", password, ".")
        elif user_input == 3:
=======

            encoded_password = encoded(str(password))
            print("Your password has been encoded and stored!")
        if user_input == 2:
            print(encoded_password)
            decoded = decoder(str(encoded_password))


            print(f"The encoded password is ", encoded_password, ", and the original password is ", decoded, ".")
        if user_input == 3:
>>>>>>> da6b9f9 (i fixed your code and did decoded function, everything is working!)
            break


if __name__ == '__main__':
    main()
