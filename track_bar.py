import cv2
import numpy as np
import argparse

def nothing(x):
    pass

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--src')
	args = parser.parse_args()

	mat = cv2.imread(args.src)

	height, width = mat.shape[:2]
	mat = cv2.resize(mat, (int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_AREA)

	name = "effect"

	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	cv2.createTrackbar('sigmaS',name,0,200,nothing)
	cv2.createTrackbar('sigmaR',name,0,10,nothing)
	cv2.createTrackbar('shade',name,0,10,nothing)

	cv2.setTrackbarPos('sigmaS',name, 25)
	cv2.setTrackbarPos('sigmaR',name,2)
	cv2.setTrackbarPos('shade',name, 1)


	while True:
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break

		sigma_s = cv2.getTrackbarPos('sigmaS',name)
		sigma_r = cv2.getTrackbarPos('sigmaR',name)
		shade = cv2.getTrackbarPos('shade',name)

		dst_mono,dst_color = cv2.pencilSketch(mat,
			sigma_s=sigma_s,
			sigma_r=sigma_r * 0.1,
			shade_factor=shade * 0.01)

		cv2.imshow(name,dst_color)


if __name__ == "__main__":
	main()
