<<<<<<< HEAD
import cv2
import numpy as np

lower_bound = np.array([0,0,0])
upper_bound = np.array([175,255,100])


url = "http://192.168.1.47:8080/video" 
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv , lower_bound, upper_bound)  


    cv2.imshow("Hi",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
=======
import cv2
import numpy as np

lower_bound = np.array([0,0,0])
upper_bound = np.array([175,255,100])


url = "http://192.168.1.47:8080/video" 
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv , lower_bound, upper_bound)  


    cv2.imshow("Hi",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
>>>>>>> f3eb6215b70e0ca5163d32ed1ede7161d371ea77
cv2.destroyAllWindows()