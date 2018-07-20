# Recognising and Translating Text from Sign-Board using OCR and Machine Learning

## Done as the part of Mini Project for computer Graphics Course

### AIM Of the Project
* The Aim of project is to Recognize  the text in Sign Board and translate to Native languages.
* The user has to take the pic of the sign board and upload to the Device
* The device processes the image and creates the text output .
* The output text is then translated to native  
* The sign board can be of any colour any fonts or photo taken from any angle  

### Steps In PreProcessing
* Input Image in rgb
* Do contrast changes
* Do angle correction for the image
* Convert image to binary
* Thresholding of the image 
* Segment the image and classify the character
* Save the text to file
* Translate the text from file to native language

### Usage
* Download the project and go to the project directory
* Run the following commands python process_image.py <inputfilename> <outputfilename>
* For translation run the following commands python extract_text.py
