# alyss santiago

def encoded(password):
    encoded1_password = []
    acc_encoded_pass = []
    for char in password:
        encoded_number = int(char) + 3
        if encoded_number < 10:
            encoded1_number = encoded_number
        if encoded_number > 9:
            encoded1_number = encoded_number - 10
            print(encoded1_number)
        encoded1_password.append(str(encoded1_number))
    acc_encoded_pass = ''.join((encoded1_password))
    return acc_encoded_pass



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

        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = int(input("Please enter your password to encode: "))
            # print(encoded_password)
            encoded_password = encoded(str(password))
            print(encoded(str(password)))
            print("Your password has been encoded and stored!")
        if user_input == 2:
            # everything is working here!
            # (this was just to test) print(encoded_password)
            decoded = decoder(str(encoded_password))
            print(f"The encoded password is ", encoded_password, ", and the original password is ", decoded, ".")
        if user_input == 3:
            break


if __name__ == '__main__':
    main()
