## Create a screenshot by clicking the edges of the area you want to capture.

### Background
This project is a prerequisite to another I'm currently working on that deals with text recognition from images. I have an app on my phone (FooView) that allows me draw a boundary box around an image/video/anything really, and then extracts text from the resulting image [almost] immediately. I usually do this a lot for links, so I'll just paste the generated text in my browser and go. A demo can be seen [here](https://twitter.com/_Olums/status/1066411959950692353) 
I have no app that does that on my laptop so I'm creating one for my use. The steps are simple: select an area with text I want to extract, create an image, then extract the text using ML. This repo is just stage one.

## Requirements
  - Python 3.3+
  - PyAutoGUI
  - Pynput
  
## How to Use
  1. After installing the requirements, simply run the script in the folder you want the screenshot to be saved.
  2. Once the script starts, your terminal will minimize automatically, so as to allow you select the area you want to screenshoot.
  3. Click the edges of the area in the following order: top-left, top-right, bottom-left, bottom-right. (Note that it's not a bounding box--there's no dragging, only clicking of the edges)
  4. Your terminal returns with a message confirming the successful creation of the screenshot.
  
  


