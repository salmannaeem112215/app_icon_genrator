import sys
from PIL import Image

def resize_and_save_icon(input_path, output_path,x=512,y=512):
    # Open the image
    img = Image.open(input_path)

    # Resize the image to 512x512
    img = img.resize((x, y))

    # Get the current width and height
    width, height = img.size

    # Check if the image is not in a 1:1 ratio
    if width != height:
        # Find the minimum dimension and create a square canvas
        size = min(width, height)
        new_img = Image.new("RGB", (size, size), (255, 255, 255))
        
        # Calculate the position to paste the original image (center it)
        left = (size - width) // 2
        top = (size - height) // 2

        # Paste the original image onto the square canvas
        new_img.paste(img, (left, top))

        # Use Image.ANTIALIAS for high-quality downsampling
        img = new_img.resize((x, y), Image.ANTIALIAS)

    # Save the resized and fitted image to the output path in PNG format
    img.save(output_path, format='PNG')

def read_parameters():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        print("Usage: python script.py input_path output_path [x] [y]")
        sys.exit(1)

    # Extract input and output paths from command-line arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Extract optional x and y values if provided
    x = int(sys.argv[3]) if len(sys.argv) > 3 else 512
    y = int(sys.argv[4]) if len(sys.argv) > 4 else 512

    return input_path, output_path, x, y

if __name__ == "__main__":
    input_path, output_path, x, y = read_parameters()

    print("Input Path:", input_path)
    print("Output Path:", output_path)
    print("x:", x)
    print("y:", y)
    resize_and_save_icon(input_path, output_path)


folder/playstore.png   (512*512)
folder/android/mipmap-hdpi/ic_launcher.png (72*72)
folder/android/mipmap-mdpi/ic_launcher.png (48*48)
folder/android/mipmap-xhdpi/ic_launcher.png (96*96)
folder/android/mipmap-xxhdpi/ic_launcher.png (144*144)
folder/android/mipmap-xxxhdpi/ic_launcher.png (1922*192)
