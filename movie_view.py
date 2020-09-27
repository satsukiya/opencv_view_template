
import numpy as np
import cv2
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--src')
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.src)

    name = "effect"
    fps = cap.get(cv2.CAP_PROP_FPS)

    while cap.isOpened():
        _ret, frame = cap.read()

        k = cv2.waitKey(int(fps)) & 0xFF
        if k == 27:
            break
        
        if frame is None:
            break

        ## [TODO] image process ##
        dst = frame
        cv2.imshow(name,dst)

    cap.release()


if __name__ == '__main__':
    main()
