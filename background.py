import cv2
#This is my webcam
cap = cv2.VideoCapture(0)


while cap.isOpened():
    #Reading from my Webcam
    ret, back = cap.read()
    #back is what the camera is reading
    if ret:
        cv2.imshow("image",back)

        if cv2.waitKey(5) == ord('q'):
            
            #Save the image
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows