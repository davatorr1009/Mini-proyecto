from PIL import Image
import numpy as np

file_path = 'src/dog.bmp'
# Cargar la imagen usando PIL
image = Image.open(file_path)

# Convertir la imagen a blanco y negro
image = image.convert('1')  # 1 bit per pixel

# Convertir la imagen a un array de bits
bitmap_array = np.array(image)

# Convertir el array en formato hexadecimal para C++
bitmap_hex = np.packbits(bitmap_array, axis=1)

# Formatear el array en estilo C++
bitmap_hex_formatted = ", ".join(f"0x{byte:02X}" for byte in bitmap_hex.flatten())

print(bitmap_hex_formatted)