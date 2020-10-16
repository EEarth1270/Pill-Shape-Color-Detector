import imutils
import cv2
import matplotlib.pyplot as plt
import fed

#import picture
fed.shapeDetector('../pillbox_production_images_full_201812/ZYD00920.jpg')
fed.shapeDetector('../pillbox_production_images_full_201812/SUN01450.jpg')
fed.shapeDetector('../pillbox_production_images_full_201812/SUN05550.jpg')
fed.shapeDetector('../pillbox_production_images_full_201812/AUR08410.jpg')
fed.shapeDetector('../pillbox_production_images_full_201812/00006-0960-54_C31361AB.jpg')
# fed.show_image(mask_org)
# # blurred = cv2.GaussianBlur(gray, (5,5), 0 )
# th1 = cv2.threshold(gray, 165,255,cv2.THRESH_BINARY)[1]
#
#
# plt.imshow(th1, cmap='gray', interpolation='bicubic')
# # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()
#
# contours = cv2.findContours(th1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
#
# contours = imutils.grab_contours(contours) # where cnts is the variable in which contours are stored, replace it with your variable name
# contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10] # sorts contours according to their area from largest to smallest.
# area = cv2.contourArea(contours[0])
# largestCont = contours[0] #store the largest contour
# area = cv2.contourArea(largestCont)
# print(largestCont)
# print(area)
#
# cv2.drawContours(circle_img, largestCont, -1, (0, 0, 255), 5)
# plt.imshow(circle_img, cmap='gray', interpolation='bicubic')
# # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()
# plt.close()
# if it is circle len largest contour is more than 4


# for c in contours:
#    # rect = cv2.boundingRect(c)
#    # x,y,w,h = rect
#    # area = w * h
#    area = cv2.contourArea(c)
#    epsilon = 0.08 * cv2.arcLength(c, True)
#    approx = cv2.approxPolyDP(c, epsilon, True)
#    print(area)
# # กำหนด Area ที่จะทำการ Draw Contour
# if area > 500:
#     cv2.drawContours(imgs, [approx], -1, (0, 0, 255), 5)
#     # cv2.rectangle(imgs, (x, y), (x+w, y+h), (0, 255, 0), 5)
#     print('approx', approx)
#     print('1')
#     # for x in range(0, len(approx)):
#     #     cv2.circle(imgs, (approx[x][0][0], approx[x][0][1]), 30, (0,0,255), -1)
#
# plt.imshow(imgs, cmap='gray', interpolation='bicubic')
# # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()
# plt.close()