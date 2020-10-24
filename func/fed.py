import imutils
import cv2
import matplotlib.pyplot as plt


def load_image(path_img):
    img = cv2.imread(path_img)
    img2 = imutils.resize(img, width=360)
    return img2


def show_image(img):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
    plt.show()
    pass


def cvt2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def create_mask(img, number=25,cont=3.5):
    # return cv2.threshold(img,number,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,  number,cont)


def largest_contour(mask):
    contours = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    # cv.CHAIN_APPROX_SIMPLE,CHAIN_APPROX_TC89_KCOS
    contours = imutils.grab_contours(contours)
    # where cnts is the variable in which contours are stored, replace it with your variable name
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    # sorts contours according to their area from largest to smallest.
    largestCont = contours[1]  # store the largest contour
    area = cv2.contourArea(largestCont)
    # print('area = ', area)
    return largestCont


def drawing_cont(img, contour,coefficient=0.037):
    epsilon = coefficient * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    # print(len(approx))
    cv2.drawContours(img, approx, -1, (255, 0, 255), 5)
    return approx




def shapeDetector(path_img):
    img = load_image(path_img)
    gray = cvt2gray(img)
    mask = create_mask(gray, 0)
    # show_image(mask)
    cont = largest_contour(mask)
    # we use the second largest because normally largest are box of the picture
    approx = drawing_cont(img, cont)
    # show_image(img)
    pred = shapePred(approx)
    # cv2.imwrite(save_path,img)
    return len(approx), pred


def shapePred(approx):
    a = 'FREEFORM'
    if len(approx) == 8:
        a = 'ROUND'
    elif len(approx) == 7:
        a = 'OVAL'
    elif len(approx) == 6:
        a = 'CAPSULE'
    elif len(approx) == 5:
        a = 'TRIANGLE'
    elif len(approx) == 4:
        a = 'QUADRANGLE'
    return a


def Grid_shape_pred(path_img,block_size,constant,coefficient):
    img = load_image(path_img)
    gray = cvt2gray(img)
    mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
    cont = largest_contour(mask)
    approx = drawing_cont(img, cont,coefficient)
    # show_image(img)
    pred = shapePred(approx)
    # cv2.imwrite(save_path,img)
    return len(approx), pred



