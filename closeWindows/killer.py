import torch
import cv2 as cv
import pyautogui as pg
import numpy as np

screenWidth, screenHeight = 3456, 2234
guiWidth, guiHeight = pg.size()
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp21/weights/last.pt', force_reload = True)

while True:
    screen = pg.screenshot()
    screen_array = np.array(screen)
    # height, width, channels
    #cropped_region = screen_array[:, screenWidth//2:, :]
    #convert to BGR
    corrected_colors = cv.cvtColor(screen_array, cv.COLOR_RGB2BGR)
    
    results = model(corrected_colors)
    #cv.imshow('YOLO', np.squeeze(results.render()))
    
    locs = []
    for item in results.xyxy[0]:
        cx = (item[0] + item[2])/2
        cy = (item[1] + item[3])/2
        locs.append((cx, cy))

	
	
    #print('\n', results.xyxy[0][0][0].item(), results.xyxy[0][0][1].item())
    print(len(locs))
    if len(locs):
        pg.moveTo(locs[0][0]/screenWidth * guiWidth - 18.25, locs[0][1]/screenHeight * guiHeight + 2, 2)
        pg.click()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
