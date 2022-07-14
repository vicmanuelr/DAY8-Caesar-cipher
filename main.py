alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

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
