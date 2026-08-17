import cv2 as cv
import numpy as np
import time

def pixel_array(box, x_steps, y_steps):
    x1 = box[0][0]
    x2 = box[1][0]
    y1 = box[0][1]
    y2 = box[1][1]
    #Create list x and y values
    x_coords = list(np.linspace(x1, x2, x_steps+1, endpoint=False))
    x_coords.pop(0)
    for i, coord in enumerate(x_coords):
        x_coords[i] = int(coord)
    y_coords = list(np.linspace(y1, y2, y_steps+1, endpoint=False))
    y_coords.pop(0)
    for i, coord in enumerate(y_coords):
            y_coords[i] = int(coord)
    #create list of coordinates
    coords = []
    for x in x_coords:
         for y in y_coords:
              coords.append([x, y])
    return coords

#Only give back blue value since the 
#Default BGR
def pixel_color_array(frame, coords):
    B_vals = []
    for coord in coords:
        B = frame[coord[1], coord[0], 0]
        B_vals.append(B)
    return B_vals

#Checks if any of the coords changes in B value. If any do change, it passes as true
def color_check(curr_color):
    for i, coord in enumerate(curr_color):
        if curr_color[i] > 100:
            return True
    return False
window_name = "YARG Window"
#Boxes for reference on how to score
x_steps = 3
y_steps = 3
#BGR
red = (0, 0, 255)
green = (0, 255, 0)
color = (255, 255, 255)
thickness = 1
instrument_names = ["vocals", "guitar", "bass", "drums"] #Change this to match
vocal_box = [(150, 135), (175, 165)]
instrument_1_box = [(100, 410), (125, 435)]
instrument_2_box = [(308, 410), (332, 435)]
instrument_3_box = [(515, 410), (540, 435)]
streak_boxes = [vocal_box, instrument_1_box, instrument_2_box, instrument_3_box]

vocal_coords = pixel_array(vocal_box, x_steps, y_steps)
instr_1_coords = pixel_array(instrument_1_box, x_steps, y_steps)
instr_2_coords = pixel_array(instrument_2_box, x_steps, y_steps)
instr_3_coords = pixel_array(instrument_3_box, x_steps, y_steps)
coords_array = [vocal_coords, instr_1_coords, instr_2_coords, instr_3_coords]

prev_frame_colors = []
streaks_alive = [False, False, False, False]
cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read() #Default BGR
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.resizeWindow(window_name, 720, 480)
    #Draw boxes and get 9 pixel color values from each box
    instrument_colors = []
    for i, box in enumerate(streak_boxes):
        cv.rectangle(frame, box[0], box[1], color, thickness)
        instrument_colors.append(pixel_color_array(frame, coords_array[i]))
    for i, instr in enumerate(instrument_colors):
        if len(prev_frame_colors) == 0:
            streaks_alive[i] = False
        else:
            streaks_alive[i] = color_check(instr)
    prev_frame_colors = instrument_colors
    print(streaks_alive)
    for i, streak in enumerate(streaks_alive):
        if streak == True:
            chosen_color = green
        else:
            chosen_color = red
        cv.rectangle(frame, streak_boxes[i][0], streak_boxes[i][1], chosen_color, thickness)
            

    cv.imshow(window_name, frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break