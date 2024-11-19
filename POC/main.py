import base64
import os
from datetime import datetime
from os.path import dirname, join

# Construct the file path
file_path = os.path.expandvars(r"%AppData%\..\Local\s1941\save.dat")

# Read the base64 string from the file
with open(file_path, "r") as file:
    base64_str = file.read().strip()

# Decode the base64 string
decoded_bytes = base64.b64decode(base64_str)
print(f"Size of decoded data: {len(decoded_bytes)} bytes")
print(f"Decoded data: {decoded_bytes}")

# Convert to hex and format
hex_str = decoded_bytes.hex()
separated_hex_str = " ".join(hex_str[i : i + 2] for i in range(0, len(hex_str), 2))
print(f"Decoded data in hex: {separated_hex_str}")

# Write the decoded bytes to a file
with open(join(dirname(__file__), "decoded_save.hex"), "wb") as file:
    file.write(decoded_bytes)
    # Get the current time
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct the new file name with the current time
    new_file_name = f"decoded_save_{current_time}.hex"

    # Write the decoded bytes to a file with the new file name
    with open(join(dirname(__file__), new_file_name), "wb") as file:
        file.write(decoded_bytes)
