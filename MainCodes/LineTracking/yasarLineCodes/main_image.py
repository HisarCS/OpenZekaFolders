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

def drawLines(image, lines):
    line_image = np.zeros_like(image)
    equations = list()
    print("printing the slope \n")
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            equations.append(polyFit((x1, x2), (image.shape[0] - y1, image.shape[0] -y2), 1))
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
            print(polyFit((x1, x2), (image.shape[0] - y1, image.shape[0] -y2), 1))
    print("\n printed the slopes \n")

    return equations, line_image

def lineOperations(equations):
    equationsWithCloseValues = list()
    closeIndexes = list()
    equations.sort()

    for (i, test_equation1) in enumerate(equations, 0):
        # closeIndexes.append([i])
        # print(closeIndexes)

        for (j, test_equation2) in enumerate(equations, 0):
            diffEq = diffBetweenEqs(test_equation1, test_equation2)
            integral = linearIntegralFinder(diffEq)
            intersectionPoint = findIntersection(test_equation1, test_equation2, 0.0)

            area = integralSquareFinder(integral, intersectionPoint, intersectionPoint + 100)
            # test_equation2 = [test_equation2, area]
            # closeIndexes[0].append(test_equation2)

            if (area < 20000000) and (not equations[j] in closeIndexes):
                # print(len(closeIndexes), "blbl")
                # test_equation2 = [test_equation2, area]
                closeIndexes.append(test_equation2)

            # sleep(0.0005)

        if closeIndexes not in equationsWithCloseValues:
            equationsWithCloseValues.append(closeIndexes)

        closeIndexes = list()

    for line in sorted(equationsWithCloseValues):
        print(line)
        print("   ")




def quadraticSolver(array, value):
    return array[0] * (value ** 2) + array[1] * value + array[2]

def integralSquareFinder(equation, lowRange, highRange):
        return (quadraticSolver(equation, highRange) - quadraticSolver(equation, lowRange)) ** 2

def linearIntegralFinder(equation, c=0):
    integral = list()
    integral.append(equation[0] / 2.0)
    integral.append(equation[1])
    integral.append(c)

    return integral

def diffBetweenEqs(equation1, equation2):
    resultantEq = list()
    resultantEq.append(equation1[0] - equation2[0])
    resultantEq.append(equation1[1] - equation2[1])
    return resultantEq


def findIntersection(eq1,eq2,x0):
    fun1 = np.poly1d(eq1)
    fun2 = np.poly1d(eq2)

    return fsolve(lambda x : fun1(x) - fun2(x),x0)[0]




def warpImage(testImage):
    pts = np.array([(int(testImage.shape[1] * 0.25), int(testImage.shape[0] * 0.0)),
                    (int(testImage.shape[1] * 0.75), int(testImage.shape[0] * 0.0)),
                    (testImage.shape[1] * 0, testImage.shape[0] * 1),
                    (testImage.shape[1] * 1, testImage.shape[0] * 1)])

    warped = perspective.four_point_transform(testImage.copy(), pts)
    # print(warped)
    return warped


frame = cv2.imread("new_road.jpg", 0)

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

equationsg, line_image = drawLines(cannyImage, lines)
lineOperations(equationsg)

############### FINDING THE LINES DONE #################################



cv2.imshow("testImage", frame)
cv2.imshow("blurred", blurred)
cv2.imshow("canny image", cannyImage)
# cv2.imshow("warped", warped)
cv2.imshow("line image", line_image)

cv2.waitKey(0)

