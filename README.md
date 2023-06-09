# Image-Metadata-Remover
Image Metadata Remover swiftly removes metadata from JPEG, PNG, GIF, and TIFF images

# Usage
Image Metadata Remover is a simple, user-friendly application that allows users to remove metadata from images. This application accepts JPEG, PNG, GIF, and TIFF formats, and is equipped with a drag-and-drop feature for ease of use. The application uses Python's PIL and piexif libraries to handle image processing.

A window will open, presenting a simple GUI. Drag and drop an image file (JPEG, PNG, GIF, or TIFF) onto the window. The application will then process the image, removing the metadata. The processed image will be saved in the same directory as the program, with '_no_metadata' added to the original filename. A dialog box will confirm the completion of the process.

# Features

    Simple GUI: A straightforward, drag-and-drop interface makes this application easy to use for anyone.

    Support for multiple formats: This application can process JPEG, PNG, GIF, and TIFF image formats.

    Metadata removal: The primary function of this application is to strip images of their metadata, enhancing user privacy.

# For Users of the python Version

1. Clone this repository to your local machine
2. Install Python packages: 
* Kivy
* KivyMD 
* Pillow 
* piexif 
3. run the script from the console. (script is found in source code file)

# License

This project is licensed under the MIT License. For more details, see the LICENSE file.
