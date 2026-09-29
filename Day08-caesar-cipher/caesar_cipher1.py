alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
original_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)                              #range 0-25
        cipher_text += alphabet[shifted_position]


    print(f"Here's the encoded result: {cipher_text}")

encrypt(original_text, shift_amount)




#print("Here's the encoded result: {encode}")