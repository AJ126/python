
import cv2
import dlib
import numpy as np


def shape_to_np(shape):
    """Convert facial landmarks into a NumPy array."""
    return np.array(
        [(shape.part(i).x, shape.part(i).y) for i in range(68)],
        dtype=np.int32
    )


def eye_on_mask(mask, shape, points):
    """Draw an eye region on the mask."""
    eye_points = shape[points]
    return cv2.fillConvexPoly(mask, eye_points, 255)


def contouring(thresh, offset, img):
    """Find the largest contour and mark its center."""
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    if not contours:
        return

    contour = max(contours, key=cv2.contourArea)
    moments = cv2.moments(contour)

    if moments["m00"] == 0:
        return

    cx = int(moments["m10"] / moments["m00"]) + offset
    cy = int(moments["m01"] / moments["m00"])

    cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)


# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_68.dat")

# Eye landmark indexes
LEFT_EYE = [36, 37, 38, 39, 40, 41]
RIGHT_EYE = [42, 43, 44, 45, 46, 47]

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open the webcam.")

WINDOW = "image"
cv2.namedWindow(WINDOW)
cv2.createTrackbar("threshold", WINDOW, 30, 255, lambda _: None)

kernel = np.ones((9, 9), dtype=np.uint8)

try:
    while True:
        ret, img = cap.read()

        if not ret:
            print("Could not read a frame from the webcam.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(gray, 1)

        thresh = np.zeros(gray.shape, dtype=np.uint8)

        for face in faces:
            shape = shape_to_np(predictor(gray, face))

            # Create mask for both eyes
            mask = np.zeros(gray.shape, dtype=np.uint8)
            eye_on_mask(mask, shape, LEFT_EYE)
            eye_on_mask(mask, shape, RIGHT_EYE)

            mask = cv2.dilate(mask, kernel, iterations=5)

            # Keep only the eye regions
            eyes = cv2.bitwise_and(img, img, mask=mask)

            # Make pixels outside the eye regions white
            outside_mask = (mask == 0)
            eyes[outside_mask] = [255, 255, 255]

            # Convert eye regions to grayscale
            eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)

            threshold = cv2.getTrackbarPos("threshold", WINDOW)

            _, thresh = cv2.threshold(
                eyes_gray,
                threshold,
                255,
                cv2.THRESH_BINARY
            )

            # Reduce noise and improve pupil detection
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=4)
            thresh = cv2.medianBlur(thresh, 3)
            thresh = cv2.bitwise_not(thresh)

            # Split image between the eyes
            mid = (shape[42][0] + shape[39][0]) // 2

            # Detect pupil centers in each half
            contouring(thresh[:, :mid], 0, img)
            contouring(thresh[:, mid:], mid, img)

        cv2.imshow("eyes", img)
        cv2.imshow(WINDOW, thresh)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
