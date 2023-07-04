# office-automation
Image Combine Tool
This is a Python script that allows you to combine multiple images into a single image by specifying the number of rows and columns.

Prerequisites
Python 3.x
Pillow library (pip install pillow)
natsort library (pip install natsort)
tkinter library (usually included with Python installation)
Usage
Clone the repository or download the script image_combine.py.

Open the terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command:

Copy code
python image_combine.py
The program will launch a graphical user interface (GUI) window.

Click on the "选择文件夹并生成大图" (Select Folder and Generate Image) button.

A file dialog will open. Choose a folder containing the images you want to combine. Please make sure that the images have the ".jpg" file extension.

A new window will appear, asking you to input the number of rows and columns for the image grid.

Enter the desired number of rows and columns in the input fields and click the "确定" (OK) button.

The program will combine the images and save the resulting image as "combined.jpg" in the selected folder.

The program will display a message indicating the completion of the image combining process, along with the details of the row and column numbers.

You can close the program by clicking the "关闭程序" (Close Program) button.

Notes
The script assumes that all the images in the selected folder have the same dimensions.

The images will be combined in natural sort order based on their filenames.

The resulting image will be saved in JPEG format as "combined.jpg" in the selected folder.

If you encounter any issues or errors, make sure you have the necessary libraries installed and check that the selected folder contains the desired images.

For more information or help, please refer to the documentation of the libraries used in the script: Pillow, natsort, tkinter.

Feel free to customize and modify the code according to your specific requirements.

License
This project is licensed under the MIT License.
