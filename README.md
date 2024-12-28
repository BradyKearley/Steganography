# Image-Based Password Encryption and Steganography

## Project Overview

The goal of this project is to allow users to securely encrypt passwords and other sensitive information using RSA encryption and then embed the encrypted data into images using steganography. This ensures that users can store information such as passwords or secret notes within images and decrypt them only with a special key.

## Features

- **RSA Encryption**: Generate public and private keys, encrypt messages with the public key, and decrypt messages with the private key.
- **Steganography**: Embed encrypted data into images and extract encrypted data from images.

## Usage

1. **Create Key**: Generate a pair of RSA keys (public and private).
2. **Encode Image**: Encrypt a message using the public key and embed the encrypted data into an image.
3. **Decode Image**: Extract the encrypted data from an image and decrypt it using the private key.

## Files

- `main.py`: Main script to interact with the user and perform key generation, encoding, and decoding.
- `RSA_Encryption.py`: Contains functions for RSA key generation, encryption, and decryption.
- `Steganography.py`: Contains functions for embedding and extracting encrypted data into/from images.

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
- Pillow
- NumPy
