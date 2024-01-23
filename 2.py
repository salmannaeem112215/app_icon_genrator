import os
import shutil
from PIL import Image,ImageOps

def create_folder_if_not_exist(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def generate_app_icons(icon_path, folder_path):
    # Ensure the folder path has a proper format
    folder_path = os.path.join(folder_path, '')
    create_folder_if_not_exist(folder_path)
    # Open the image
    img = get_image(icon_path)

    # Define the resolutions for different Android icon sizes
    android_sizes = {
        "mipmap-hdpi": (72, 72),
        "mipmap-mdpi": (48, 48),
        "mipmap-xhdpi": (96, 96),
        "mipmap-xxhdpi": (144, 144),
        "mipmap-xxxhdpi": (192, 192)
    }

   


    # Generate the Play Store icon (512x512)
    playstore_icon_path = os.path.join(folder_path, "playstore.png")
    img.resize((512, 512)).save(playstore_icon_path, format='PNG')
   
    # Generate Android icons for different resolutions
    android_folder_path = os.path.join(folder_path, "android")
    create_folder_if_not_exist(android_folder_path)

    for size_folder, size in android_sizes.items():
        size_folder_path = os.path.join(folder_path, "android", size_folder)
        create_folder_if_not_exist(size_folder_path)
     
        android_icon_path = os.path.join(folder_path, "android", size_folder, "ic_launcher.png")
        img.resize(size).save(android_icon_path, format='PNG')

def get_image(path):
    img = Image.open(path)

    # Resize the image to 512x512
    img = img.copy()

    # Get the current width and height
    width, height = img.size

    # Check if the image is not in a 1:1 ratio
    if width == height:
        return img.resize((512,512))
    print("NEW TO RESIZE")
    # Find the minimum dimension and create a square canvas
    size = max(width, height)
    new_img = Image.new("RGBA", (size, size), (0,0, 0,0))
    
    # Calculate the position to paste the original image (center it)
    left = (size - width) // 2
    top = (size - height) // 2
    # Paste the  original image onto the square canvas
    new_img.paste(img, (left,top))
    # return   ImageOps.fit(img,(512,512), method = 0,
                #    bleed = 0.0, centering =(0.5, 0.5))

    # Use Image.ANTIALIAS for high-quality downsampling
    return  new_img.resize((512, 512), Image.Resampling.LANCZOS)

if __name__ == "__main__":
    # Example usage:
    icon_path = r"C:\Users\PMLS\Downloads\1.png"
    folder_path = r"C:\Users\PMLS\Downloads\1"

    generate_app_icons(icon_path, folder_path)

