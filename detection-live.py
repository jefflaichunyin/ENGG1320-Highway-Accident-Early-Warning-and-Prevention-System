#! /usr/bin/python3
# coding=utf-8
import time
import cv2
import numpy as np
import queue
TIMEOUT = 3
camera = cv2.VideoCapture("http://127.0.0.1:8081")
width = int(camera.get(3))
height = int(camera.get(4))

firstFrame = None
lastDec = None
firstThresh = None

feature_params = dict(maxCorners=50,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3))
num = 0

q_x = queue.Queue(maxsize=2)
#q_y = queue.Queue(maxsize=5)
previous = ""
trigger = 0
counter = 0
last_enter_time = -1
while True:
    (grabbed, frame) = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if counter < 5:
        counter = counter+1
    else:
        counter = 0
        trigger = 0
    # print(counter)
    if firstFrame is None:
        firstFrame = gray
        continue
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 10, 255, cv2.THRESH_BINARY)[1]
    p0 = cv2.goodFeaturesToTrack(thresh, mask=None, **feature_params)
    if p0 is not None:
        x_sum = 0
        y_sum = 0
        for i, old in enumerate(p0):
            x, y = old.ravel()
            x_sum += x
            y_sum += y
        x_avg = x_sum / len(p0)
        y_avg = y_sum / len(p0)

        if q_x.full():

            qx_list = list(q_x.queue)
            key = 0
            diffx_sum = 0
            for item_x in qx_list:
                key += 1
                if key < 2:
                    diff_x = item_x - qx_list[key]
                    diffx_sum += diff_x
            # print(trigger)
            if diffx_sum < -20:
                #print(diffx_sum, x_avg)
                # print("left")
                if trigger >= 0:
                    print("L->R", x_avg)
                    if 0 <= x_avg <= 180:
                        print("ENTER")
                        last_enter_time = time.time()
                    if 350 <= x_avg <= 400:
                        print("EXIT")
                        last_enter_time = -1
                    trigger = 0
                previous = "left"
                if previous == "left":
                    trigger = trigger+1
                #cv2.putText(frame, "some coming from left",
                #            (100, 100), 0, 0.5, (0, 0, 255), 2)
            elif diffx_sum > 20:
                if trigger <= 0:
                    print("R->L", x_avg)
                    if 220 <= x_avg <= 400:
                        print("ENTER")
                        last_enter_time = time.time()
                    if 0 <= x_avg <= 50:
                        print("EXIT")
                        last_enter_time = -1
                    trigger = 0
                previous = "right"
                if previous == "right":
                    trigger = trigger-1

            q_x.get()
        q_x.put(x_avg)
        #cv2.putText(frame, str(x_avg), (300, 100), 0, 0.5, (0, 0, 255), 2)
        frameDelta = cv2.circle(frameDelta, (int(x_avg), int(y_avg)),
                           5, color[i].tolist(), -1)
    if last_enter_time != -1 and (time.time() - last_enter_time) > TIMEOUT:
      print("Broken down vehicle detected!")
      last_enter_time = -1
    cv2.imshow("Detection", frameDelta)
    cv2.waitKey(5)
    firstFrame = gray.copy()


camera.release()
cv2.destroyAllWindows()
