from PIL import Image
from RSA_Encryption import *
import numpy as np
def encode_image(image_path, encrypted_data, output_path):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size
    
    # Convert encrypted data into a binary string
    binary_data = ''.join(format(num, '064b') for num in encrypted_data)  # 64 bits per number
    data_length = len(binary_data)
    max_capacity = width * height * 3  # Total bits the image can store (3 bits per pixel)

    if data_length > max_capacity:
        raise ValueError("The encrypted data is too large to fit in the image.")
    
    # Encode the length of the data in the first 64 bits (for decoding later)
    binary_data = format(len(encrypted_data), '064b') + binary_data

    # Embed the binary data into the image
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_data):
                break
            r, g, b = pixels[x, y]
            
            # Modify the LSBs of R, G, and B channels
            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1
            
            pixels[x, y] = (r, g, b)
        if data_index >= len(binary_data):
            break

    # Save the modified image
    image.save(output_path)
    print(f"Encrypted data embedded into the image and saved to {output_path}")
def decode_image(image_path):
    # Open the image and convert to a numpy array
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image).flatten()  # Flatten the 3D array (width, height, channels) to 1D
    
    # Extract LSBs
    binary_data = ''.join(str(pixel & 1) for pixel in pixels)
    
    # Extract the length of the data (first 64 bits)
    num_numbers = int(binary_data[:64], 2)
    binary_data = binary_data[64:]  # Remove the length prefix
    
    # Group binary data into 64-bit integers
    encrypted_data = [int(binary_data[i:i+64], 2) for i in range(0, num_numbers * 64, 64)]
    return encrypted_data
