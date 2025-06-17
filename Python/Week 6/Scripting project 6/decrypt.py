def caesar_decipher(encrypted_text, distance):
    decrypted_text = ""
    for char in encrypted_text:
        char_code = ord(char)
        if 32 <= char_code <= 126:
            shifted_code = (char_code - 32 - distance + 95) % 95 + 32
            decrypted_text += chr(shifted_code)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    encrypted_text = input("Enter a line of encrypted text: ")
    while True:
        try:
            distance = int(input("Enter the distance value used for encryption: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the distance.")

    decrypted_message = caesar_decipher(encrypted_text, distance)
    print("Decrypted text:", decrypted_message)
