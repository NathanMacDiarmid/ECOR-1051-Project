BuggingMeFilters 
Version 1.1 
Price: Free 

04/07/2020

CONTACT INFORMATION:
____________________

Nathan MacDiarmid
Cell-Phone: (506)251-3433
Email: nathanmacdiarmid@cmail.carleton.ca

DESCRIPTION:
____________

	BuggingMeFilters is a filter software that applies different filters to pictures and then is saved to a directory with applied filters.

	This software contains both a batch user interface and an interactive user interface. Through selection on the interface or input to a batch file, a user can pick which filter they would like to apply to their desired photo. Filter options from the attached filter library include: Sepia Tint, Extreme Contrast, Posterize, Edge Detection, Improved Edge Detection, Two-Tone, Three-Tone, a Vertical Flip, and a Horizontal Flip. Upon selection, a copy of the new filtered image will then be saved to a specified directory.

	This project is made up of 3 files:

	- T28_batch_ui.py
	- T28_image_filters.py
	- T28_interactive_ui.py

INSTALLATION:
_____________

Python 3.8.2 and Pillow 7.1.1 must be installed.

Download the following modules:

- Cimpl 
- simple_Cimple_filters
- test_greyscale

They can be found at https://culearn.carleton.ca/moodle/mod/folder/view.php?id=1600897
The rest of the program must be installed in the same directory as all three modules above.

USAGE:
______


 ** CHANGE THE DIRECTORY TO WHEREVER THE FILE IS SAVED BEFORE EXECUTING THESE COMMANDS **


> python3 T28_interactive_ui.py

L)oad Image S)ave as
2)-tone 3)-tone X)treme Contrast T)int Sepia P)osterize
E)age Detection I)mproved Edge Detection V)ertical Flip H)orizontal Flip
Q)uit

:

	To begin, an image can be loaded by entering the letter "L" or "l".
	Note: if the user interface doesn't show up immediately after, double check that an image window is not open in the background.
When prompted, after loading the image, enter the corresponding letter or number of the filter desired. This will apply the filter. Again, make sure the window showing the picture is closed. The image which has a filter can be saved by entering the letter "S" or "s". Enter the letter "Q" or "q" to end the program.

L)oad Image S)ave as
2)-tone 3)-tone X)treme Contrast T)int Sepia P)osterize
E)age Detection I)mproved Edge Detection V)ertical Flip H)orizontal Flip
Q)uit

: L

Loads a selected image.

L)oad Image S)ave as
2)-tone 3)-tone X)treme Contrast T)int Sepia P)osterize
E)age Detection I)mproved Edge Detection V)ertical Flip H)orizontal Flip
Q)uit

: V

Flips the image on a vertical line down the centre.

> python3 T28_batch_ui.py
Please input the name of a batch file: 

	A .txt file should be created containing the filename of the image which requires the application of filters, the filename that you wish the image to be saved as, and the filters that you wish applied. When the program is run, the new image will be saved in the same directory as the .txt file.

Each line in the batch file should look like this: 

test_image.jpg save_name.jpg 2 X H 
test_image2.jpg save_name2.jpg 3 E V

		** MAKE SURE TO PUT AN EXTRA SPACE AFTER THE LAST FILTER **

Please input the name of a batch file: example_batch_file.txt

Open your directory after running this program and there should be as many photos as there are lines in the batch file.

CREDITS:
________

Nathan MacDiarmid 101098993: 

FILTERS: 

- Adjust Component - Green Channel - Horizontal Test - Interactive User Interface - 		Posertize - Sepia Test - Vertical Flip -

README FILE: 

- Credits - Contact - Information - Date - Formatting - License -

Anita Ntomchukwu 101138391: 

FILTERS: 

- Combine - Improved Edge Detection - Two-Tone - Three-Tone -

README FILE: 

- Usage -

Sam Hurd 101146639:

FILTERS: 

- Batch User Interface - Edge Detection - Red Channel - Sepia -

README FILE: 

- Description - Name -

Yahya Shah 101169280: 

FILTERS: 

- Batch User Interface - Blue Channel - Extreme Contrast - Horizontal Flip -

README FILE: 

- Installation -

LICENSE:
________

MIT License

Copyright (c) [2020] [Nathan MacDiarmid, Anita Ntomchukwu, Sam Hurd, Yayha Shah]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
