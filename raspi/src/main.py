# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui.main import MainFrame
import cv2

if __name__ == "__main__":
	main = MainFrame(cv2.VideoCapture(0))
	main.show_frame()
	main.start()
