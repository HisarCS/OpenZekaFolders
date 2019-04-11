import cv2
import imutils
from imutils import perspective
import numpy as np
from scipy.optimize import fsolve
from time import sleep

def polyFit(xAxis, yAxis, degree):
    equation = list()
    if degree is 1:
        equation.append(np.polyfit(xAxis, yAxis, 1)[0])
        equation.append(np.polyfit(xAxis, yAxis, 1)[1])
    else:
        equation = []
    return equation

def convertToEquation(lines, image):
    equations = list()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            equations.append(polyFit((x1, x2), (image.shape[0] - y1, image.shape[0] -y2), 1))
    return equations


def drawEquations(image, equations):
    copyImage = image
    for equation in equations:
        y1 = 0
        y2 = image.shape[0]

        x1 = int(solveInverseOfEquation(equation, y1))
        x2 = int(solveInverseOfEquation(equation, y2))

        print((x1, x2), (image.shape[0] - y1, image.shape[0] - y2))

        cv2.line(copyImage, (x1, image.shape[0] - y1), (x2, image.shape[0] - y2), 120, 10)

    return copyImage


def solveInverseOfEquation(equation, x):
    inverseEquation = [1/equation[0], -equation[1]/equation[0]]
    # func = np.poly1d(equation)
    # invFunc = np.poly1d(inverseEquation)
    print(equation, "        ", inverseEquation)
    print((inverseEquation[0] * x) + inverseEquation[1])

    return (inverseEquation[0] * x) + inverseEquation[1]


def lineOperations(equations):
    equationsWithCloseValues = list()
    closeIndexes = list()
    equations.sort()

    for (i, test_equation1) in enumerate(equations, 0):
        for (j, test_equation2) in enumerate(equations, 0):

            diff = abs(np.arctan(test_equation1[0]) - np.arctan(test_equation2[0])) * 180/np.pi

            if (diff < 20) and (not equations[j] in closeIndexes):
                closeIndexes.append(test_equation2)

        if closeIndexes not in equationsWithCloseValues:
            equationsWithCloseValues.append(closeIndexes)

        closeIndexes = list()

    topThreeInLength = sortTheArrayLen(equationsWithCloseValues)
    TheReliableThreeLines = list()
    for line in sorted(topThreeInLength):
        # print(line)
        # print("   ")
        slopes = list()
        for s in line:
            slopes.append(s[0])
        intercepts = list()
        for i in line:
            intercepts.append(i[1])

        meanSlope = np.mean(slopes)
        meanIntercept = np.mean(intercepts)
        # print(meanSlope, meanIntercept)
        TheReliableThreeLines.append([meanSlope, meanIntercept])

    return TheReliableThreeLines


def sortTheArrayLen(array):
    theIndexList = list()
    for (i, l1) in enumerate(array):
        theIndexList.append([len(l1), i])
    theIndexList = sorted(theIndexList, reverse=True)

    theTopThree = list()
    for t in theIndexList[:3]:
        indexNumber = t[1]
        theTopThree.append(array[indexNumber])

    return theTopThree


def warpImage(testImage):
    pts = np.array([(int(testImage.shape[1] * 0.25), int(testImage.shape[0] * 0.0)),
                    (int(testImage.shape[1] * 0.75), int(testImage.shape[0] * 0.0)),
                    (testImage.shape[1] * 0, testImage.shape[0] * 1),
                    (testImage.shape[1] * 1, testImage.shape[0] * 1)])

    warped = perspective.four_point_transform(testImage.copy(), pts)
    # print(warped)
    return warped


frame = cv2.imread("test_image.jpg", 0)

############### IMAGE TAKING COMPLETE #################################

############### IMAGE PRE PROCESS START #################################
cv2.imshow("actual frame", frame)
frame = warpImage(frame[int(frame.shape[0]*0.50):int(frame.shape[0]),:])

blurred = cv2.GaussianBlur(frame, (15, 15), 0)
cannyImage = cv2.Canny(blurred, 80, 220)
cannyImage = cv2.GaussianBlur(cannyImage, (3, 3), 0)
############### IMAGE PRE PROCESS DONE #################################

############### FINDING THE LINES #################################

thresh_area = 40
minLineLength = int(frame.shape[0]*0.333)
maxLineGap = int(frame.shape[0]*0.333)
lines = cv2.HoughLinesP(cannyImage, 3, np.pi/30, thresh_area, np.array([]), minLineLength=minLineLength, maxLineGap=maxLineGap)

equationsg = convertToEquation(lines, cannyImage)
Reliables = lineOperations(equationsg)
drawnImage = drawEquations(frame, Reliables)
############### FINDING THE LINES DONE #################################



cv2.imshow("testImage", frame)
cv2.imshow("blurred", blurred)
cv2.imshow("canny image", cannyImage)
# cv2.imshow("warped", warped)
cv2.imshow("line image", drawnImage)

cv2.waitKey(0)

