encoded_password = ''

def encode_password():
    global encoded_password
    original_password = input('Please enter your password to encode: ')
    encoded_password = ''
    for digit in original_password:
        shifted_digit = int(digit) + 3
        encoded_password += str(shifted_digit)
    print('Your password has been encoded and stored!')

def decode():
	decoded_password = ''
	global encoded_password
	for digit in encoded_password:
		new_digit = int(digit) - 3
		decoded_password += str(new_digit)
	return decoded_password
	

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
            new_pword = decode()
            print(f'The encoded password is {encoded_password}, and the original password is {new_pword}.')
        elif choice == 3:
            print('Exiting...')
            break
        else:
            print('Invalid option, please try again.')

if __name__ == '__main__':
    main_menu()

