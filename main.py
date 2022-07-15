from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     encrypted_text = ""
#     for letter in plain_text:
#         new_index = alphabet.index(letter) + shift_amount
#         if new_index > len(alphabet) - 1:
#             new_index = new_index - len(alphabet)
#         encrypted_text += alphabet[new_index]
#     print(f"The encoded text is {encrypted_text}")
#
# def decrypt(cypher_text, shift_amount):
#     decrypted_text = ""
#     for letter in cypher_text:
#         new_index = alphabet.index(letter) - shift_amount
#         if new_index < 0:
#             new_index = new_index + len(alphabet)
#         decrypted_text += alphabet[new_index]
#     print(f"The decrypted text is {decrypted_text}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cypher_text=text, shift_amount=shift)


def caesar(text_entered, text_movement, decrypt_method):
    encrypted_text = ""
    if decrypt_method == "encode":
        for letter in text_entered:
            new_index = alphabet.index(letter) + text_movement
            if new_index > len(alphabet) - 1:
                new_index = new_index - len(alphabet)
            encrypted_text += alphabet[new_index]
        print(f"The encoded text is {encrypted_text}")
    elif decrypt_method == "decode":
        for letter in text_entered:
            new_index = alphabet.index(letter) - text_movement
            if new_index < 0:
                new_index = new_index + len(alphabet)
            encrypted_text += alphabet[new_index]
        print(f"The decrypted text is {encrypted_text}")


caesar(text_entered=text, text_movement=shift, decrypt_method=direction)

# TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).

# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
