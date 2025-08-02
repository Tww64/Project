def caesar_cipher(plaintext, distance):
    encrypted_text = ""
    for char in plaintext:
        char_code = ord(char)
        if 32 <= char_code <= 126:
            shifted_code = (char_code - 32 + distance) % 95 + 32
            encrypted_text += chr(shifted_code)
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    plaintext = input("Enter a line of plaintext: ")
    while True:
        try:
            distance = int(input("Enter a distance value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the distance.")

    encrypted_message = caesar_cipher(plaintext, distance)
    print("Encrypted text:", encrypted_message)
