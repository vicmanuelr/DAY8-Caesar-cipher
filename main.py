from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)

user_continue = True
while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)


    def caesar(text_entered, text_movement, decrypt_method):
        encrypted_text = ""
        if decrypt_method == "encode":
            for char in text_entered:
                if char in alphabet:
                    new_index = alphabet.index(char) + text_movement
                    if new_index > len(alphabet) - 1:
                        new_index = new_index - len(alphabet)
                    encrypted_text += alphabet[new_index]
                else:
                    encrypted_text += char
            print(f"The encoded text is -->{encrypted_text}<--")
        elif decrypt_method == "decode":
            for char in text_entered:
                if char in alphabet:
                    new_index = alphabet.index(char) - text_movement
                    if new_index < 0:
                        new_index = new_index + len(alphabet)
                    encrypted_text += alphabet[new_index]
                else:
                    encrypted_text += char
            print(f"The decrypted text is -->{encrypted_text}<--")


    caesar(text_entered=text, text_movement=shift, decrypt_method=direction)
    choice_wrong = True
    while choice_wrong:
        user_choice = input("Would you like to use program again? Type 'y' or 'n'? ")
        if user_choice == "n":
            user_continue = False
            choice_wrong = False
        elif user_choice == "y":
            choice_wrong = False
        else:
            print("Please select 'y' or 'n' ")