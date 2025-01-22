from RSA_Encryption import generate_keys, encrypt, decrypt
from Steganography import encode_image, decode_image

#______________________Events_______________________#
def createKey():
    # Generate the public and private keys
    public_key, private_key = generate_keys()
    print("Public Key: SHARE TO LET PEOPLE SEND YOU SECRET MESSAGES")
    print("")
    print(f"n: {public_key['n']}  \ne: {public_key['e']}")
    print("")
    print("Private Key: DO NOT SHARE")
    print(f"d: { private_key['d']}")
    print("")
    with open("private_key.txt", "w") as file:
        file.write(f"n: {private_key['n']}\n")
        file.write(f"d: {private_key['d']}\n")
    with open("public_key.txt", "w") as file:
        file.write(f"n: {public_key['n']}\n")
        file.write(f"e: {public_key['e']}\n")

def encodeImage():
    # Get the image path and message
    image_path = input("Enter the image path: ")
    message = input("Enter a message to encrypt: ")

    # Read the public key from the file
    with open("public_key.txt", "r") as file:
        lines = file.readlines()
        n = int(lines[0].strip().split(": ")[1])
        e = int(lines[1].strip().split(": ")[1])
    public_key = {'n': n, 'e': e}

    # Encrypt the message
    encrypted_data = encrypt(message, public_key)
    output_path = input("Enter the output path: ")
    # Embed the encrypted data into the image
    encode_image(image_path, encrypted_data, output_path)

def decodeImage():
    # Get the image path
    image_path = input("Enter the image path: ")
    decoded_encrypted_data = decode_image(image_path)
    
    # Read the private key from the file
    with open("private_key.txt", "r") as file:
        lines = file.readlines()
        n = int(lines[0].strip().split(": ")[1])
        d = int(lines[1].strip().split(": ")[1])
    private_key = {'n': n, 'd': d}
    
    # Decrypt the message
    decrypted_message = decrypt(decoded_encrypted_data, private_key)
    print("Decrypted message:", decrypted_message)
def addKeys():
    n = int(input("Enter n: "))
    d = int(input("Enter d: "))
    e = int(input("Enter e: "))
    with open("private_key.txt", "w") as file:
        file.write(f"n: {n}\n")
        file.write(f"d: {d}\n")
    with open("public_key.txt", "w") as file:
        file.write(f"n: {n}\n")
        file.write(f"e: {e}\n")
#____________________End Events_____________________#


#_______________________MAIN _______________________#

while True:
    # Display the menu
    print("Image Encryption and Decryption")
    print("\n Please Update private_key.txt and public_key.txt with the keys generated if you already have them")
    print("____________________________")
    print("Menu")
    print("1. Create Key")
    print("2. Add Keys")
    print("3. Encode Image")
    print("4. Decode Image")
    print("5. Exit")
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    # Perform the user's desired action
    if choice == 1:
        createKey()
    elif choice == 2:
        addKeys()
    elif choice == 3:
        encodeImage()
    elif choice == 4:
        decodeImage()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")


#____________________End MAIN ______________________#
