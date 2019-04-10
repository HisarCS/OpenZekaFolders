import sys
sys.path.append("..") ## Must be added to include the OpenZeka Class
from OpenZekaMasterClass import PIDController
from time import sleep


PID = PIDController(kp=0.5,ki=0.01,kd=0.5,maxCorr=34)

# maxCorr variable is there to limit the correction
# The ki should be very small for autonomus vehicle applications
# The sleeps affect the system correction


for error in range(0, 55, 5):
    correction = PID.calc(error)
    print("The error: {} and the calculated correction varible to make the error as close to None(zero): {}".format(error, correction))
    sleep(1)

print("reached 50")

for error in range(45, -5, -5):
    correction = PID.calc(error)
    print("The error: {} and the calculated correction varible to make the error as close to None(zero): {}".format(error, correction))
    sleep(1)

print("reached 0")

for error in range(-5, -50, -5):
    correction = PID.calc(error)
    print("The error: {} and the calculated correction varible to make the error as close to None(zero): {}".format(error, correction))
    sleep(1)




