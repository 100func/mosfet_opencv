# -*- coding: utf-8 -*-

import cv2
import numpy as np


#img = cv2.imread('!!!!data_path!!!!',cv2.IMREAD_COLOR)
filename = 'trimming/mubaiasu.bmp'

def nothing(x):
    pass

# Create a black image, a window
img1 = np.zeros((300,512,3), np.uint8)
img2 = np.zeros((300,512,3), np.uint8)

cv2.namedWindow('min',cv2.WINDOW_NORMAL)
cv2.namedWindow('max',cv2.WINDOW_NORMAL)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('Min:R','min',0,255,nothing)
cv2.createTrackbar('Min:G','min',0,255,nothing)
cv2.createTrackbar('Min:B','min',0,255,nothing)

cv2.createTrackbar('Max:R','max',0,255,nothing)
cv2.createTrackbar('Max:G','max',0,255,nothing)
cv2.createTrackbar('Max:B','max',0,255,nothing)

# create switch for ON/OFF functionality
switch3 = 'Extraction:0 : OFF \n1 : ON'
cv2.createTrackbar(switch3, 'image',0,1,nothing)


# メイン関数
def main():
    img3 = cv2.imread(filename,cv2.IMREAD_COLOR)

    while True:
        # キー入力を1ms待って、keyが「q」だったらbreak
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            break

        # get current positions of four trackbars
        min_r = cv2.getTrackbarPos('Min:R','min')
        min_g = cv2.getTrackbarPos('Min:G','min')
        min_b = cv2.getTrackbarPos('Min:B','min')

        max_r = cv2.getTrackbarPos('Max:R','max')
        max_g = cv2.getTrackbarPos('Max:G','max')
        max_b = cv2.getTrackbarPos('Max:B','max')

        s3 = cv2.getTrackbarPos(switch3,'image')

        img1[:] = [min_b,min_g,min_r]
        img2[:] = [max_b,max_g,max_r]
        
        if s3 == 0:
            bgrResult = img3
        else:
            # BGRでの色抽出
            bgrLower = np.array([min_r, min_g, min_b])    # 抽出する色の下限
            bgrUpper = np.array([max_r, max_g, max_b])    # 抽出する色の上限
            bgrResult = bgrExtraction(img3, bgrLower, bgrUpper)
         
        cv2.imshow('min',img1)
        cv2.imshow('max',img2)
        cv2.imshow('image', bgrResult)
    
    cv2.destroyAllWindows()
    filesavename = input('file save name:')
    np.save('extraction_npy/'+filesavename,np.array(bgrResult))
    print('min',min_r, min_g, min_b)
    print('min',max_r, max_g, max_b)


# BGRで特定の色を抽出する関数
def bgrExtraction(image, bgrLower, bgrUpper):
    img_mask = cv2.inRange(image, bgrLower, bgrUpper) # BGRからマスクを作成
    result = cv2.bitwise_and(image, image, mask=img_mask) # 元画像とマスクを合成
    return result

if __name__ == '__main__':
    main()
