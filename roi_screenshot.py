
from pynput.mouse import Listener
import pyautogui as gui
import os

num = 0 # counter for mapping mouse clicks to positions

save_location = os.path.abspath(os.path.dirname(__file__))

coordinates = {'top_left': None, 'top_right': None,
               'bottom_left': None, 'bottom_right': None }

def on_click(x, y, button, pressed):
    """Mouse click callback from listener object"""

    global num
    if pressed:
        num += 1
        if num == 1:
            coordinates['top_left'] = (x, y)
            return False # stop the listener

        elif num == 2:
            coordinates['top_right'] = (x, y)
            return False

        elif num == 3:
            coordinates['bottom_left'] = (x, y)
            return False

        elif num == 4:
            coordinates['bottom_right'] = (x, y)
            return False

def activateListener():
    """Creates the listener object that tracks mouse clicks"""

    with Listener(on_click=on_click) as listener:
        listener.join()

def imageFormatter(coordinates):
    """Formats the coordinates for use with PyAutoGui"""

    width = max( coordinates['top_right'][0] - coordinates['top_left'][0], coordinates['bottom_right'][0] - coordinates['bottom_left'][0] )
    height = max( coordinates['bottom_right'][1] - coordinates['top_right'][1], coordinates['bottom_left'][1] - coordinates['top_left'][1] )
    left = coordinates['top_left'][0]
    top = coordinates['top_left'][1]

    return (left, top, width, height)


def imageCreator(left, top, width, height):
    """Creates the actual screenshot"""

    image_file = gui.screenshot(region=(left, top, width, height))
    image = os.path.join(save_location, 'screenshot_' + str(width) + 'x' + str(height) + '.png')
    image_file.save(image)

    print('\nScreenshot created in {}'.format(save_location))


def main():
    """Main application"""

    gui.hotkey('altleft', 'space'); gui.press('n') # Hide the terminal so it won't obstruct screenshot selection. (Wasn't tested on OSX)

    positions = ['top left', 'top right', 'bottom left', 'bottom right']
    for i in positions:
        print('Click the {} of the screenshot'.format(i))
        activateListener() # start the listener

    image_details = imageFormatter(coordinates)
    left, top, width, height = image_details

    imageCreator(left, top, width, height)

    gui.hotkey('altleft', 'tab') # Return terminal after main application completes

if __name__ == '__main__':
    main()
