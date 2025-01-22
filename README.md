# Image Encryption and Decryption

## Project Overview

The goal of this project is to allow users to securely encrypt passwords and other sensitive information using RSA encryption and then embed the encrypted data into images using steganography. This ensures that users can store information such as passwords or secret notes within images and decrypt them only with a special key.

## Features

- **RSA Encryption**: Generate public and private keys, encrypt messages with the public key, and decrypt messages with the private key.
- **Steganography**: Embed encrypted data into images and extract encrypted data from images.

## Usage

1. **Create Key**: Generate a pair of RSA keys (public and private) and save them to `public_key.txt` and `private_key.txt` respectively.
2. **Encode Image**: Encrypt a message using the public key from `public_key.txt` and embed the encrypted data into a PNG image.
3. **Decode Image**: Extract the encrypted data from a PNG image and decrypt it using the private key from `private_key.txt`.

## User Interface

A graphical user interface (GUI) is provided to make it easier to generate keys, encrypt messages, and embed/extract data from images.

### Steps to Use the UI

1. **Generate Keys**: Click the "Generate Keys" button to generate a new pair of RSA keys. The keys will be displayed in the text boxes and saved to `public_key.txt` and `private_key.txt`.
2. **Load Keys**: Click the "Load Keys" button to load the keys from `public_key.txt` and `private_key.txt` into the text boxes.
3. **Save Keys**: Click the "Save Keys" button to save the keys from the text boxes to `public_key.txt` and `private_key.txt`.
4. **Encrypt Image**: Enter a message, select an image (PNG format), and click the "Encrypt Image" button to encrypt the message and embed it into the image.
5. **Decrypt Image**: Select an image (PNG format) and click the "Decrypt Image" button to extract and decrypt the message from the image.

## Files

- `main.py`: Main script to interact with the user and perform key generation, encoding, and decoding.
- `RSA_Encryption.py`: Contains functions for RSA key generation, encryption, and decryption.
- `Steganography.py`: Contains functions for embedding and extracting encrypted data into/from images.
- `image_encryption_ui.py`: Contains the code for the graphical user interface.
- `public_key.txt`: File to store the public key.
- `private_key.txt`: File to store the private key.

## How to Run

1. Install the required dependencies:

   ```sh
   pip install pillow numpy
   ```

2. Run the main script:
   ```sh
   python main.py
   ```

## Example

1. Generate RSA keys.
2. Encrypt a message and embed it into an image.
3. Extract the encrypted message from the image and decrypt it.

## Dependencies

- Python 3.x
- Tkinter
- Pillow
- NumPy

## Notes

- This application works only with PNG images for embedding and extracting encrypted data.
- Ensure that `public_key.txt` and `private_key.txt` are in the same directory as the scripts when loading or saving keys.
