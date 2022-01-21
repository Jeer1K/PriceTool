#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import numpy
import os

image = None
template = None
threshold = None
img_display = None

def main(argv):
    """ PriceTool """
    global threshold
    threshold = 0.999
    path = ".\icons"
    template_list = os.listdir(path)
    global image
    global template
    image = cv2.imread("screenshot3.png", cv2.IMREAD_COLOR)
    

    if(image is None):
        print("One of the images is not readable")
        return -1

    global img_display
    img_display = image.copy()
    for i in range(len(template_list)):
        template = cv2.imread("./icons/" + template_list[i], cv2.IMREAD_COLOR)
        #result = cv.matchTemplate(img, templ, match_method, None, mask)
        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
        template_h, template_w, _ = template.shape
        while 1:
            _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
            #print(_maxVal)
            if(_maxVal > threshold):
                matchLoc = maxLoc
                #cv2.rectangle(img_display, matchLoc, (matchLoc[0] + template_w, matchLoc[1] + template_h), (0,0,0), 2, 8, 0 )
                cv2.rectangle(result, matchLoc, (matchLoc[0] + template_w, matchLoc[1] + template_h), (0,0,0), 2, 8, 0 )
                cv2.putText(img_display, template_list[i][:4], (matchLoc[0], matchLoc[1] + template_h) ,cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2, cv2.LINE_AA)
                result[matchLoc[1]-template_h//2:matchLoc[1]+template_h//2 + 1, matchLoc[0]-template_w//2:matchLoc[0]+template_w//2+1] = 0
            else:
                break
    if(template is None):
        print("One of the templates is not readable")
        return -1
    #cv2.rectangle(img_display, matchLoc, (matchLoc[0] + template_h, matchLoc[1] + template_w), (0,0,0), 2, 8, 0 )
    #cv2.rectangle(result, matchLoc, (matchLoc[0] + template_h, matchLoc[1] + template_w), (0,0,0), 2, 8, 0 )
    cv2.imshow("image_window", img_display)
    cv2.imshow("result_window", result)

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

def templateMatch():
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    template_h, template_w, _ = template.shape
    while 1:
        _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
        #print(_maxVal)
        matchLoc = maxLoc
        if(_maxVal > threshold):
            cv2.rectangle(img_display, matchLoc, (matchLoc[0] + template_h, matchLoc[1] + template_w), (0,0,0), 2, 8, 0 )
            cv2.rectangle(result, matchLoc, (matchLoc[0] + template_h, matchLoc[1] + template_w), (0,0,0), 2, 8, 0 )
            result[matchLoc[1]-template_h//2:matchLoc[1]+template_h//2 + 1, matchLoc[0]-template_w//2:matchLoc[0]+template_w//2+1] = 0
        else:
            break
    return

    

if __name__ == "__main__":
    main(sys.argv[1:])