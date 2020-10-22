import imutils
import cv2
import matplotlib.pyplot as plt
import fed

#import picture

#Round
# 2bfe798f-7e4c-62fa-e054-00144ff8d46c.jpg
# 001850401.jpg
# 101440594.jpg
#Oval
# 005363757.jpg
# 000540252.jpg
# 68180-0559-09_C00E6013.jpg
# 64679-0968-01_NLMIMAGE10_7939BC9D.jpg
#Capsule
# 00591-3210-60_341C9A14.jpg
# 31722-0223-05_17080B80.jpg
# 00115-0533-01_9405CA2E.jpg
# 421950145.jpg
# 76439-0302-10_NLMIMAGE10_37459BAC.jpg
# 009045307.jpg
# 510790747.jpg
#Rectangle
# 65862-0098-01_BC16DE56.jpg
# 00093722298.jpg
# 60505-2673-03_NLMIMAGE10_D648EB27.jpg
#Triangle
# 00093-7424-56_0F280780.jpg
# 00093512701.jpg
# 597625210.jpg
# 000031612.jpg
#Diamond
# 00093-2068-01_NLMIMAGE10_A2405112.jpg
# 005910744.jpg
#FREEFORM should be classless -> combination of everyclass
# SQUARE
# 55111-0725-30_NLMIMAGE10_9F3A4FC2.jpg
# # 00093-7425-56_D727EBFF.jpg
# TRAPEZOID               20
# HEXAGON (6 SIDED)       17
# OCTAGON (8 SIDED)       12
# PENTAGON (5 SIDED)      11
# TEAR                     6
# BULLET                   4
# DOUBLE CIRCLE            4
# SEMI-CIRCLE              1