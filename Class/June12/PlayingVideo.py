import cv2
cap =  cv2.VideoCapture('F:\\series\\Suits\\Season 1\\Episode 1 - Pilot.mkv')

while cap.isOpened():
    ret, frame=cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()