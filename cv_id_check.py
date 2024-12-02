import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == ord('s'):
        cv2.imwrite('test.jpg', frame)

cap.release()
cv2.destroyAllWindows()