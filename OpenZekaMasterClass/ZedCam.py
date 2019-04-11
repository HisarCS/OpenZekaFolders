import sys

import cv2
import pyzed.sl as sl
from threading import Thread
from time import sleep


class ZedCam:

	def __init__(self, fps=100):

		
		self.zed = sl.Camera()
		self.side = sl.VIEW.VIEW_LEFT
		init = sl.InitParameters()
		init.camera_resolution = sl.RESOLUTION.RESOLUTION_VGA
		init.coordinate_units = sl.UNIT.UNIT_METER
		init.camera_fps = fps

		err = self.zed.open(init)
		if err != sl.ERROR_CODE.SUCCESS:
			self.zed.close()
			exit(-1)

		self.currentFrame = None
		self.updateFeed = False

		self.framesToShow = dict()

		self.isWindowShowEnabled = False
		self.isRecording = False
		self.output = None
		self.key = None

############################################################
	def startLooking(self):
		self.updateFeed = True
		Thread(target=self.__updateCameraFeed__, args=()).start()
		return self


	def __updateCameraFeed__(self):
		while self.updateFeed:
			image = sl.Mat()
			runtime_parameters = sl.RuntimeParameters()
			if self.zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
				self.zed.retrieve_image(image, self.side)
				self.currentFrame = image.get_data()

	def stopCamera(self):
		self.updateFeed = False

#############################################################

	def startRecording(self, nameOfTheFile="output.avi"):
		self.output = cv2.VideoWriter(nameOfTheFile, cv2.VideoWriter_fourcc("M", "J", "P", "G"), 30, (self.currentFrame.shape[1], self.currentFrame.shape[0]))
		self.isRecording = True		
		Thread(target=self.__updateRecording__, args=()).start()

	def __updateRecording__(self):
		while self.isRecording:
			frameToSave = cv2.cvtColor(self.currentFrame, cv2.COLOR_BGRA2BGR)
			self.output.write(frameToSave)
		self.output.release()

	def stopRecording(self):
		self.isRecording = False

##############################################################

	def showFrame(self, windowName="frame", frameToShow=None):
		if frameToShow is None:
			self.framesToShow[windowName] = self.currentFrame
		else:
			self.framesToShow[windowName] = frameToShow

		if not self.isWindowShowEnabled:
			self.isWindowShowEnabled = True
			Thread(target=self.__updateWindowFrame__, args=()).start()


	def __updateWindowFrame__(self):

		while self.isWindowShowEnabled:

			for name in self.framesToShow.copy():
				cv2.imshow(name, self.framesToShow[name])

			self.key = cv2.waitKey(1)

			if self.key == ord("q"):
				
				self.stopCamera()
				sleep(0.1)

				self.zed.close()
				cv2.destroyAllWindows()
				self.isWindowShowEnabled = False
				break

#############################################################

	def getImage(self):
		return self.currentFrame




