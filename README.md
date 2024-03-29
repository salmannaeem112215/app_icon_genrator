# Mobile App Icon Generator

## Overview

This project provides a solution for generating mobile app icons in a specific format, including ratios, folders, and names. The project offers two methods for creating app icons: using the www.appicon.co website or utilizing a Python script.

### Method 1: www.appicon.co

- **Issue:**
  1. No API is available, making it challenging to automate the icon generation process.
  2. Generating 40 app icons manually on the website can be time-consuming.

### Method 2: Python Code

The Python code is designed to automate the app icon generation process. It includes the following components:

1. **App Icon Generator:**

   - Usage: `python app_icon_generator.py image_path folder_path`
   - Description: This script generates a single app icon based on the provided image and folder path.

2. **Multi App Icon Generator:**

   - Usage: `python multi_app_icon_generator.py data.json`
   - Description: This script generates multiple app icons specified in a JSON file (`data.json`). The JSON file should contain an array of app icon configurations.

3. **Dependencies Installation Script:**
   - File: `import_dependencies.bat`
   - Usage: Run this script to install the necessary Python packages. Ensure that Python is installed on your system before running this script.

## Instructions

### Method 1: www.appicon.co

1. Manually visit the website [www.appicon.co](www.appicon.co).
2. Generate each app icon by uploading the image to the website and configuring the desired settings.
3. Download each generated app icon and organize them into the specified folders.

### Method 2: Python Code

1. Ensure that Python is installed on your system.
2. Run `import_dependencies.bat` to install the required packages.

#### Single App Icon Generation:

3. Run `python app_icon_generator.py image_path folder_path` by replacing `image_path` with the path to your image and `folder_path` with the desired output folder path.

#### Multiple App Icons Generation:

4. Prepare a JSON file (`data.json`) with an array of app icon configurations, where each configuration includes the image path and folder path.
5. Run `python multi_app_icon_generator.py data.json` to generate multiple app icons based on the configurations in the JSON file.

## Notes

- The Python scripts are designed to automate the app icon generation process, providing a faster and more scalable solution compared to the manual method.
- Ensure that all dependencies are installed before running the Python scripts.

Feel free to reach out if you encounter any issues or have questions!
