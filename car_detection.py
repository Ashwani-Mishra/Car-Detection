import cv2
car = cv2.VideoCapture('car3.mp4')
car_cascade = cv2.CascadeClassifier('car.xml')

while True:

    ret,frame =car.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,9)

    for(x,y,w,h) in cars:
        plate =frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(51,51,255),2)
        cv2.rectangle(frame,(x,y -40),(x+w,y),(51,51,255),-2)
       
        cv2.putText(frame, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Car Detection',plate)
    frame = cv2.resize(frame,(600,400))
    cv2.imshow("Car Detection System",frame)
    if cv2.waitKey(13)==ord('q'):
        break
car.release()
cv2.destroyAllWindows()
