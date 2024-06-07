import cv2
from PIL import Image
from util import get_limits

# Change this to the BGR color value you want to detect
blue = [0, 0, 255]  # BGR colorspace value for blue
lowerlimit, upperlimit = get_limits(blue)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_img, lowerlimit, upperlimit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)  # Display the mask for debugging

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
