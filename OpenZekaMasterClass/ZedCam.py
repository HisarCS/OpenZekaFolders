import cv2
import pyzed.sl as sl
import threading

class ZedCam:

	LEFT_CAM = sl.VIEW.VIEW_LEFT
	RIGHT_CAM = sl.VIEW.VIEW_RIGHT

	def __init__(self, side=LEFT_CAM, fps=30):
		self.side = side
		
		self.zed = sl.Camera()
    		init = sl.InitParameters()
    		init.camera_resolution = sl.RESOLUTION.RESOLUTION_HD1080
    		init.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_PERFORMANCE
    		init.coordinate_units = sl.UNIT.UNIT_METER
		init.camera_fps = fps

		err = zed.open(init_params)
		if err != sl.ERROR_CODE.SUCCESS:
   			exit(-1)

		self.frame = None
		self.depth = None
		self.depthView = None
		
	def __update__(self):
		while self.update:
			image = sl.Mat()
			depth_map = sl.Mat()
			image_depth_zed = sl.Mat(zed.getResolution().width, sl.get_resolution().height, sl.MAT_TYPE.MAT_TYPE_8U_C4)
			runtime_parameters = sl.RuntimeParameters()
			if self.zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
  				self.zed.retrieve_image(image, self.side)
				self.frame = image
				self.zed.retrieve_measure(depth_map, sl.MEASURE.MEASURE_DEPTH)
				self.depth = depth_map
				self.zed.retrieve_measure(image_depth_zed, sl.VIEW.VIEW_DEPTH)
				self.depth = image_depth_zed

	def startLooking(self):
		self.update = True
		Thread(target=self.__update__, args=()).start()
		return self

	def getDepthData(self):
		return self.depth.get_data()

	def getImage(self):
		return self.frame.get_data()

	def getDepthImage(self):
		return self.depthView.get_data()