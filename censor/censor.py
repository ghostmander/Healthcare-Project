import cv2
import numpy as np

# init part
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)

box_start = []
box_end = []


def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    count = 0
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
        if count == 0:
            box_start.clear()
            box_end.clear()
            box_start.extend([x, y])
            box_end.extend([x, y])
            count = 1

    return frame


def detect_eyes(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)  # detect eyes
    width = np.size(img, 1)  # gets face frame width
    height = np.size(img, 0)  # gets face frame height
    left_eye = None
    right_eye = None

    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # gets the eye center
        

        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
            print(y, x)
            box_start[0] += x
            box_start[1] += y
        else:
            right_eye = img[y:y + h, x:x + w]
            print(y, x)
            box_end[0] += x + w
            box_end[1] += y + h

    #print(left_coord, right_coord)

    return left_eye, right_eye

    


def main():

    EyeData = {}

    #frame = cv2.imread("human-rights-exhibits.jpg")
    #frame = cv2.imread("child-1388700__340.jpg")
    frame = cv2.imread("AFRICAN_BOY.jpg")
    frame = cv2.resize(frame, (510, 340), interpolation = cv2.INTER_AREA)

    
    face_frame = detect_faces(frame, face_cascade)

    if face_frame is not None:
        #cv2.imshow("FaceFrame",face_frame)
        eyes = detect_eyes(face_frame, eye_cascade)

        if eyes[0] is not None:
            cv2.imshow("Left", eyes[0])
            EyeData["Left"] = eyes[0]
            
        if eyes[1] is not None:
            cv2.imshow("Right", eyes[1])
            EyeData["Right"] = eyes[1]

        #print(EyeData)
        print(box_start, box_end)

        frame = cv2.rectangle(frame, tuple(box_end), tuple(box_start), (0,0,0), -1)
            

        cv2.imshow('image', frame)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()