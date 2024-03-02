from PIL import Image

# Array of ASCII characters
ASCII_CHARS = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]


# Resize image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width 
    new_height = int(new_width * ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Convert pixels to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def main(new_width=100):
    # Attempt to open image
    try:
        path = input("Enter a valid pathname to an image:\n")
        image = Image.open(path)
    except Exception as e:
        print(e)
        return

    # Convert image to ASCII
    image = resize_image(image)
    image = grayify(image)

    # Convert pixels to ASCII
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    # Print ASCII image
    print(ascii_img)

    # Save ASCII image to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

if __name__ == "__main__":
    main()
