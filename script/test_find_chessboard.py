#!/usr/bin/env
# coding: utf-8


import cv2
import sys

if __name__ == "__main__":

    sys.stderr.write("Test code for cv2.findChessbordCorners().\n" + \
                     "<Usage>\n"
                     "s: save image\n" + \
                     "q: quit\n")

    vc = cv2.VideoCapture(0)

    if not vc.isOpened():
        sys.stderr.write("[ERROR] Failed to open camera\n")
        sys.exit()

    pattern_size = (10, 7)
    # pattern_size = (8, 5)
    # pattern_size = (6, 3)

    sys.stderr.write("[INFORMATION] The number of corners on the pattern is set to " + \
                     str(pattern_size) + "\n")

    cv2.namedWindow("image")

    not_found_yet = True
    find_chessboard_counter = 0
    find_chessboard_interval = 0
    saved_image_counter = 0

    while True:

        ret, frame = vc.read()
        frame_to_draw = frame.copy()

        if not ret:
            sys.stderr.write("[ERROR] Failed to read next frame\n")
            sys.exit()

        if find_chessboard_interval == find_chessboard_counter:
            found, corners = cv2.findChessboardCorners(frame, pattern_size)
            not_found_yet = False
            find_chessboard_counter = 0
        else:
            find_chessboard_counter += 1

        if not not_found_yet:
            cv2.drawChessboardCorners(frame_to_draw, pattern_size, corners, found)

        cv2.imshow("image", frame_to_draw)

        command = cv2.waitKey(1)
        
        if command == ord('q'):
            sys.stderr.write("[INFORMATION] Quit\n")
            break
        elif command == ord('s'):
            file_name = "images/" + str(saved_image_counter) + ".jpg"
            cv2.imwrite(file_name, frame)
            sys.stderr.write("[INFORMATION] Wrote " + file_name + "\n")
            saved_image_counter += 1

    vc.release()
    cv2.destroyAllWindows()

    
