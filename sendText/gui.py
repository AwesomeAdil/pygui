import pyautogui
import time
import cv2 as cv 
import numpy as np
import sys

branch = "Icons/"
screenWidth, screenHeight = 3456, 2234 
guiWidth, guiHeight = pyautogui.size()
img1 = cv.imread(branch + 'Message.png')

try:
	corrected_img1 = cv.cvtColor(img1, cv.COLOR_RGB2BGR)
except:
	print("Message icon not recognized? Is it in Icons?")
	exit()

messageLocation = pyautogui.locateOnScreen(corrected_img1, confidence=.75) 
try:
	messageLocationCenter = pyautogui.center(messageLocation) 
except TypeError:
	print('Could not find Message Icon, replace it in Icons or reduce confidence')
	exit()

messagex, messagey = messageLocationCenter.x, messageLocationCenter.y


#for i in range(3):
#	print(i+1)
#	time.sleep(1)


pyautogui.moveTo(messagex/screenWidth * guiWidth, messagey/screenHeight * guiHeight)
pyautogui.click()

time.sleep(0.5)

path = branch+'Contacts/'+str(sys.argv[-1])+'.png'
img2 = cv.imread(path)

try:
	corrected_img2 = cv.cvtColor(img2, cv.COLOR_RGB2BGR)
except:
        print("Contact not recognized? Is it in Contacts?")
        exit()
sentence = ' '.join(sys.argv[1:-1])

contactLocation = pyautogui.locateOnScreen(corrected_img2, confidence=.80)

try:
	contactLocationCenter = pyautogui.center(contactLocation)
except TypeError:
        print('Could not find Contact Icon, replace it in Icons or reduce confidence')
        exit()

contactx, contacty = contactLocationCenter.x, contactLocationCenter.y
pyautogui.moveTo(contactx/screenWidth * guiWidth, contacty/screenHeight * guiHeight)
pyautogui.click()

pyautogui.write(sentence)
choice = pyautogui.confirm(text='enter', title='Enter?', buttons=['OK', 'Cancel'])

if choice == 'OK':
	pyautogui.moveTo(contactx/screenWidth * guiWidth, contacty/screenHeight * guiHeight)
	pyautogui.click()
	pyautogui.press('enter')
