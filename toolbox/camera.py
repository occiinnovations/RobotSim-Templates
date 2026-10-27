import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not metime.isOpened():
    print("Camera index 0 failed to open.")
    metime = cv2.VideoCapture(1, cv2.CAP_DSHOW)

print("OpenCV Status: Active")
print("Press 'q' to end.")

while True:
    ret, frame = metime.read()

    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    cv2.imshow('OpenCV Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

metime.release()
cv2.destroyAllWindows()
