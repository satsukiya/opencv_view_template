
import numpy as np
import cv2
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--src')
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.src)

    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter('output.mp4', fmt, fps, (cap_width,cap_height))

    while cap.isOpened():
        _ret, frame = cap.read()
        
        if frame is None:
            break

        ## [TODO] image process ##
        dst = frame

        writer.write(dst)

    cap.release()
    writer.release()


if __name__ == '__main__':
    main()
