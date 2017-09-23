message = input('ASCII message: ')

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
encode_message = ''
zeros = 0
ones = 0
bin_str = ''

for letter in message:
    letter_in_ascii = ord(letter)
    if ascii_letters.find(letter) == -1:
        ascii_in_bin = bin(int(letter_in_ascii)).replace('b', '')
    else:
        ascii_in_bin = bin(int(letter_in_ascii)).replace('0b', '')
    bin_str = bin_str + str(ascii_in_bin)

for number in bin_str:
    if number == '0':
        if ones != 0:
            encode_message = encode_message + '0' + ' ' + '0' * ones + ' '
            ones = 0
        zeros += 1
    elif number == '1':
        if zeros != 0:
            encode_message = encode_message + '00' + ' ' + '0' * zeros + ' '
            zeros = 0
        ones += 1

if ones != 0:
    encode_message = encode_message + '0' + ' ' + '0' * ones + ' '
if zeros != 0:
    encode_message = encode_message + '00' + ' ' + '0' * zeros + ' '

print('Encode: ', encode_message[:-1])
