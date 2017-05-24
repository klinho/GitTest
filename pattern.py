#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:18:04 2017

@author: ho
"""
import numpy as np

# accessible_table


#axs_table = [ [2,4,5], [1,3,4,5,6], [2,5,6], \
#              [1,2,5,7,8], [1,2,3,4,6,7,8,9], [2,3,5,8,9], \
#              [4,5,8], [4,5,6,7,9], [5,6,8] ]

axs_table = [ [2,3,4,5,7], [1,3,4,5,6,8], [1,2,5,6,9], \
              [1,2,5,6,7,8], [1,2,3,4,6,7,8,9], [2,3,4,5,8,9], \
              [1,4,5,7,8], [2,4,5,6,7,9], [3,5,6,7,8] ]


start = 1
start_index = start - 1

def judge_i(histLst, i):
    # whether i is in hist
    if i in histLst:
        return False
    # bool_crossCheck
    bool_15 = False
    bool_26 = False
    bool_48 = False
    bool_59 = False
    bool_24 = False
    bool_35 = False
    bool_57 = False
    bool_68 = False
    bool_2 = True
    bool_4 = True
    bool_5 = True
    bool_6 = True
    bool_8 = True
    
    boolLst = [bool_15, bool_26, bool_48, bool_59, \
               bool_24, bool_35, bool_57, bool_68, \
               bool_2, bool_4, bool_5, bool_6, bool_8]
    
    point_start = histLst[0]
    for j in histLst[1:]:
        point_end = j
        tuple_shinkou = (point_start, point_end)
        if tuple_shinkou == (1,5) or tuple_shinkou == (5,1):
            boolLst[0] = True
        if tuple_shinkou == (2,6) or tuple_shinkou == (6,2):
            boolLst[1] = True
        if tuple_shinkou == (4,8) or tuple_shinkou == (8,4):
            boolLst[2] = True
        if tuple_shinkou == (5,9) or tuple_shinkou == (9,5):
            boolLst[3] = True
        if tuple_shinkou == (2,4) or tuple_shinkou == (4,2):
            boolLst[4] = True
        if tuple_shinkou == (3,5) or tuple_shinkou == (5,3):
            boolLst[5] = True
        if tuple_shinkou == (5,7) or tuple_shinkou == (7,5):
            boolLst[6] = True
        if tuple_shinkou == (6,8) or tuple_shinkou == (8,6):
            boolLst[7] = True
        if point_start == 2:
            boolLst[8] = False
        if point_start == 4:
            boolLst[9] = False
        if point_start == 5:
            boolLst[10] = False
        if point_start == 6:
            boolLst[11] = False
        if point_start == 8:
            boolLst[12] = False
        if point_end == 2:
            boolLst[8] = False
        if point_end == 4:
            boolLst[9] = False
        if point_end == 5:
            boolLst[10] = False
        if point_end == 6:
            boolLst[11] = False
        if point_end == 8:
            boolLst[12] = False
        point_start = j
    # whether i is invalid
    last_point = histLst[-1]
    new_point = i
    move_tuple = (last_point, new_point)
    for k in range ( len ( boolLst ) ):
        if boolLst[k]:
            if k==0 and ( move_tuple == (2,4) or move_tuple == (4,2) ):
                return False
            if k==1 and ( move_tuple == (3,5) or move_tuple == (5,3) ):
                return False
            if k==2 and ( move_tuple == (5,7) or move_tuple == (7,5) ):
                return False
            if k==3 and ( move_tuple == (6,8) or move_tuple == (8,6) ):
                return False
            if k==4 and ( move_tuple == (1,5) or move_tuple == (5,1) ):
                return False
            if k==5 and ( move_tuple == (2,6) or move_tuple == (6,2) ):
                return False
            if k==6 and ( move_tuple == (4,8) or move_tuple == (8,4) ):
                return False
            if k==7 and ( move_tuple == (5,9) or move_tuple == (9,5) ):
                return False
            if len(histLst) >= 2:
                if k==8 and ( move_tuple == (1,3) or move_tuple == (3,1) ):                   
                    return False                
                if k==9 and ( move_tuple == (1,7) or move_tuple == (7,1) ):
                    return False                
                if k==10 and ( move_tuple == (2,8) or move_tuple == (8,2) ):
                    return False                
                if k==10 and ( move_tuple == (4,6) or move_tuple == (6,4) ):
                    return False                
                if k==11 and ( move_tuple == (3,9) or move_tuple == (9,3) ):
                    return False                
                if k==12 and ( move_tuple == (7,9) or move_tuple == (9,7) ):
                    return False                
            else:
                if k==8 and ( move_tuple == (1,3) or move_tuple == (3,1) ):                   
                    return False                
                if k==9 and ( move_tuple == (1,7) or move_tuple == (7,1) ):
                    return False                
                if k==10 and ( move_tuple == (2,8) or move_tuple == (8,2) ):
                    return False                
                if k==10 and ( move_tuple == (4,6) or move_tuple == (6,4) ):
                    return False                
                if k==11 and ( move_tuple == (3,9) or move_tuple == (9,3) ):
                    return False                
                if k==12 and ( move_tuple == (7,9) or move_tuple == (9,7) ):
                    return False
    if len(histLst) >= 2:
        if ( move_tuple == (1,3) or move_tuple == (3,1) ) and histLst[-2] == 2:                   
            return False                
        if ( move_tuple == (1,7) or move_tuple == (7,1) ) and histLst[-2] == 4:
            return False                
        if ( move_tuple == (2,8) or move_tuple == (8,2) ) and histLst[-2] == 5:
            return False                
        if ( move_tuple == (4,6) or move_tuple == (6,4) ) and histLst[-2] == 5:
            return False                
        if ( move_tuple == (3,9) or move_tuple == (9,3) ) and histLst[-2] == 6:
            return False                
        if ( move_tuple == (7,9) or move_tuple == (9,7) ) and histLst[-2] == 8:
            return False        
        if i not in axs_table[ ( histLst[-1] - 1 ) ]:
            raise ValueError("i is strange")
    return True
    

def nextStep(AllPattern_histLst):
    next_pattern = []
    for histLst in AllPattern_histLst:
        recent_point = histLst[-1]
        recent_point_index = recent_point - 1
        # candidate_validation
        candidate = axs_table[recent_point_index]
        for i in candidate:
            bool_forehead = judge_i(histLst,i)
            if bool_forehead:
                next_pattern.append( list ( np.append(histLst, i) ) )
    return next_pattern

all_pattern = [ [1], [4], [7] ]
print all_pattern
all_pattern = nextStep ( all_pattern ) 
print "2-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "3-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "4-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "5-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "6-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "7-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "8-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "9-point-pattern:", len ( all_pattern )

#final_lst = [[1,2,3,4], 

import cv2
import math

def cvArrow(img, pt1, pt2, color, thickness=5, lineType=12, shift=0):
    cv2.line(img,pt1,pt2,color,thickness,lineType,shift)
    vx = pt2[0] - pt1[0]
    vy = pt2[1] - pt1[1]
    v  = math.sqrt(vx ** 2 + vy ** 2)
    ux = vx / v
    uy = vy / v

    w = 25
    h = 30
    ptl = (int(pt2[0] - uy*w - ux*h), int(pt2[1] + ux*w - uy*h))
    ptr = (int(pt2[0] + uy*w - ux*h), int(pt2[1] - ux*w - uy*h))

    cv2.line(img,pt2,ptl,color,thickness,lineType,shift)
    cv2.line(img,pt2,ptr,color,thickness,lineType,shift)

def for_loop_save_image(pattern_lst):
    pos_len = 180
    
    pos_1 = (85, 65) # [y, x]
    pos_4 = (85, 65 + pos_len*1 ) # [y, x]
    pos_7 = (85, 65 + pos_len*2 ) # [y, x]
    pos_2 = (85 + pos_len*1, 65) # [y, x]
    pos_5 = (265, 245) # [y, x]
    pos_8 = (85 + pos_len*1, 65 + pos_len*2) # [y, x]
    pos_3 = (85 + pos_len*2, 65) # [y, x]
    pos_6 = (85 + pos_len*2, 65 + pos_len*1) # [y, x]
    pos_9 = (85 + pos_len*2, 65 + pos_len*2) # [y, x]
    pos_lst = [pos_1, pos_2, pos_3, pos_4, pos_5, \
               pos_6, pos_7, pos_8, pos_9, ]
    
    sav_no = 1
    for pattern_i in range ( len(pattern_lst) ):
        # Verify whether pattern_i is no naname
        bool_pattern_i = False
        point_start = pattern_lst[pattern_i][0]
        nanameCount = 0
        for j in pattern_lst[pattern_i][1:]:
            point_end = j
            tuple_shinkou = (point_start, point_end)
#            if tuple_shinkou == (1,5) or tuple_shinkou == (5,1):
#                bool_pattern_i = True
#            if tuple_shinkou == (2,6) or tuple_shinkou == (6,2):
#                bool_pattern_i = True
#            if tuple_shinkou == (4,8) or tuple_shinkou == (8,4):
#                bool_pattern_i = True
#            if tuple_shinkou == (5,9) or tuple_shinkou == (9,5):
#                bool_pattern_i = True
#            if tuple_shinkou == (2,4) or tuple_shinkou == (4,2):
#                bool_pattern_i = True
#            if tuple_shinkou == (3,5) or tuple_shinkou == (5,3):
#                bool_pattern_i = True
#            if tuple_shinkou == (5,7) or tuple_shinkou == (7,5):
#                bool_pattern_i = True
#            if tuple_shinkou == (6,8) or tuple_shinkou == (8,6):
#                bool_pattern_i = True

            if tuple_shinkou == (1,5) or tuple_shinkou == (5,1):
                nanameCount += 1
            if tuple_shinkou == (2,6) or tuple_shinkou == (6,2):
                nanameCount += 1
            if tuple_shinkou == (4,8) or tuple_shinkou == (8,4):
                nanameCount += 1
            if tuple_shinkou == (5,9) or tuple_shinkou == (9,5):
                nanameCount += 1
            if tuple_shinkou == (2,4) or tuple_shinkou == (4,2):
                nanameCount += 1
            if tuple_shinkou == (3,5) or tuple_shinkou == (5,3):
                nanameCount += 1
            if tuple_shinkou == (5,7) or tuple_shinkou == (7,5):
                nanameCount += 1
            if tuple_shinkou == (6,8) or tuple_shinkou == (8,6):
                nanameCount += 1

            if (tuple_shinkou == (1,3) or tuple_shinkou == (3,1) ):
                bool_pattern_i = True
            if ( tuple_shinkou == (1,7) or tuple_shinkou == (7,1) ):
                bool_pattern_i = True
            if ( tuple_shinkou == (4,6) or tuple_shinkou == (6,4) ):
                bool_pattern_i = True
            if ( tuple_shinkou == (2,8) or tuple_shinkou == (8,2) ):
                bool_pattern_i = True
            if ( tuple_shinkou == (3,9) or tuple_shinkou == (9,3) ):
                bool_pattern_i = True
            if ( tuple_shinkou == (7,9) or tuple_shinkou == (9,7) ):
                bool_pattern_i = True
            
            if nanameCount >= 2:
                bool_pattern_i = False
            
            point_start = j
            
        if bool_pattern_i:
#            print pattern_lst[pattern_i]
            pattern = pattern_lst[pattern_i]
            img = cv2.imread("/Users/ho/Desktop/PatternLockSearch/image_blank.png")
            start_point = pattern[0]
            
            cv2.circle(img, pos_lst[start_point-1], 50, (0,0,255), thickness=5 )
            for point_i in range ( len ( pattern ) - 1 ):
                start_arrow = pattern[point_i] 
                end_arrow = pattern[point_i + 1]
                start_pos = pos_lst[start_arrow-1] 
                end_pos = pos_lst[end_arrow-1]
                cvArrow(img, start_pos, end_pos, (255-point_i*35 , point_i*35, point_i*35))
#                color_rand = np.uint8 ( np.random.rand(3)* 255 )
#                cvArrow(img, start_pos, end_pos, ( int(color_rand[0]), int(color_rand[1]), int(color_rand[2]) ) )
                cv2.circle(img, pos_lst[start_point-1], 10, (255,0,0), thickness=-1 )
            img = cv2.resize(img, (np.shape(img)[1]/2,np.shape(img)[0]/2) )
            cv2.imwrite("%04d.jpg"%(sav_no), img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
            sav_no += 1
#        return img
#img = for_loop_save_image([ [4,5,6,9,8,7], [2,3,1,5] ])
#cv2.imshow("img", img)  

import os
os.chdir("/Users/ho/Desktop/PatternLockSearch")
# Draw the pattern and Save Result
all_pattern = [ [1] ]
task_name = "UL"
if not os.path.exists(task_name):
    os.mkdir(task_name)
os.chdir(task_name)

print all_pattern
all_pattern = nextStep ( all_pattern ) 
print "2-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "3-point-pattern:", len ( all_pattern )
all_pattern = nextStep ( all_pattern ) 
print "4-point-pattern:", len ( all_pattern )
if not os.path.exists("4point"):
    os.mkdir("4point")
os.chdir("4point")
for_loop_save_image(all_pattern)
os.chdir("../")

all_pattern = nextStep ( all_pattern ) 
print "5-point-pattern:", len ( all_pattern )
if not os.path.exists("5point"):
    os.mkdir("5point")
os.chdir("5point")
for_loop_save_image(all_pattern)
os.chdir("../")

all_pattern = nextStep ( all_pattern ) 
print "6-point-pattern:", len ( all_pattern )
if not os.path.exists("6point"):
    os.mkdir("6point")
os.chdir("6point")
for_loop_save_image(all_pattern)
os.chdir("../")

all_pattern = nextStep ( all_pattern ) 
print "7-point-pattern:", len ( all_pattern )
if not os.path.exists("7point"):
    os.mkdir("7point")
os.chdir("7point")
for_loop_save_image(all_pattern)
os.chdir("../")

all_pattern = nextStep ( all_pattern ) 
print "8-point-pattern:", len ( all_pattern )
if not os.path.exists("8point"):
    os.mkdir("8point")
os.chdir("8point")
for_loop_save_image(all_pattern)
os.chdir("../")

all_pattern = nextStep ( all_pattern ) 
print "9-point-pattern:", len ( all_pattern )
if not os.path.exists("9point"):
    os.mkdir("9point")
os.chdir("9point")
for_loop_save_image(all_pattern)
os.chdir("../")              

os.chdir("../")

