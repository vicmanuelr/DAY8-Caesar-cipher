from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)

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
        print(f"The encoded text is {encrypted_text}")
    elif decrypt_method == "decode":
        for char in text_entered:
            if char in alphabet:
                new_index = alphabet.index(char) - text_movement
                if new_index < 0:
                    new_index = new_index + len(alphabet)
                encrypted_text += alphabet[new_index]
            else:
                encrypted_text += char
        print(f"The decrypted text is {encrypted_text}")


caesar(text_entered=text, text_movement=shift, decrypt_method=direction)


# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
