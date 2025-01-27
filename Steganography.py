from PIL import Image
from RSA_Encryption import *
import numpy as np
import time
def encode_image(image_path, encrypted_data, output_path):
    start_time = time.time()
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
    end_time = time.time()
    print(f"Time taken to encode the image: {end_time - start_time} seconds")
def decode_image(image_path):
    start_time = time.time()
    # Open the image and convert to a numpy array
    image_open_start = time.time()
    image = Image.open(image_path)
    image = image.convert("RGB")
    image_open_end = time.time()
    print(f"Time taken to open and convert the image: {image_open_end - image_open_start} seconds")
    
    pixels_flatten_start = time.time()
    pixels = np.array(image).flatten()  # Flatten the 3D array (width, height, channels) to 1D
    pixels_flatten_end = time.time()
    print(f"Time taken to flatten the image: {pixels_flatten_end - pixels_flatten_start} seconds")
    
    # Extract LSBs
    extract_lsb_start = time.time()
    binary_data = ''.join(format(byte, '08b') for byte in np.packbits(pixels & 1))
    extract_lsb_end = time.time()
    print(f"Time taken to extract LSBs: {extract_lsb_end - extract_lsb_start} seconds")
    
    # Extract the length of the data (first 64 bits)
    extract_length_start = time.time()
    num_numbers = int(binary_data[:64], 2)
    binary_data = binary_data[64:]  # Remove the length prefix
    extract_length_end = time.time()
    print(f"Time taken to extract the length of the data: {extract_length_end - extract_length_start} seconds")
    
    # Group binary data into 64-bit integers
    group_data_start = time.time()
    encrypted_data = [int(binary_data[i:i+64], 2) for i in range(0, num_numbers * 64, 64)]
    group_data_end = time.time()
    print(f"Time taken to group binary data into 64-bit integers: {group_data_end - group_data_start} seconds")
    
    end_time = time.time()
    print(f"Total time taken to decode the image: {end_time - start_time} seconds")
    return encrypted_data
