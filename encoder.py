encoded_password = ''

def encode_password():
    global encoded_password
    original_password = input('Please enter your password to encode: ')
    encoded_password = ''
    for digit in original_password:
        shifted_digit = int(digit) + 3
        encoded_password += str(shifted_digit)
    print('Your password has been encoded and stored!')

def main_menu():
    choice = None
    while choice != 3:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            encode_password()
        elif choice == 2:
            #Nico's decoding function
            pass
        elif choice == 3:
            print('Exiting...')
            break
        else:
            print('Invalid option, please try again.')

if __name__ == '__main__':
    main_menu()

