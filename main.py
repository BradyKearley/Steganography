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

def encodeImage():
    # Get the image path, message, and public key
    image_path = input("Enter the image path: ")
    message = input("Enter a message to encrypt: ")
    n = int(input("Enter the value of n: "))
    e = int(input("Enter the value of e: "))
    public_key = {'n':n, 'e':e}
    # Encrypt the message
    encrypted_data = encrypt(message, public_key)
    output_path = input("Enter the output path: ")
    # Embed the encrypted data into the image
    encode_image(image_path, encrypted_data, output_path)

def decodeImage():
    # Get the image path, private key, and decrypt the message
    image_path = input("Enter the image path: ")
    decoded_encrypted_data = decode_image(image_path)
    # Decrypt the message
    n = int(input("Enter the value of n: "))
    d = int(input("Enter the value of d: "))
    private_key = {'n':n, 'd':d}
    # Decrypt the message
    decrypted_message = decrypt(decoded_encrypted_data, private_key)
    print("Decoded Encrypted Data: ", decrypted_message)

#____________________End Events_____________________#


#_______________________MAIN _______________________#

while True:
    # Display the menu
    print("1. Create Key")
    print("2. Encode Image")
    print("3. Decode Image")
    print("4. Exit")
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    # Perform the user's desired action
    if choice == 1:
        createKey()
    elif choice == 2:
        encodeImage()
    elif choice == 3:
        decodeImage()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")


#____________________End MAIN ______________________#
