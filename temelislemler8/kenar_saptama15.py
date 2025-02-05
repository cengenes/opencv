# cv2.Canny(input,minThreshold,maxThreshold)

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    kenar = cv2.Canny(frame,100,200) # cv2.Canny(frame, 100, 200): Bu satır, Canny algoritmasını kullanarak kenar tespiti yapar.
    """•	frame: Kenar tespiti yapılacak görüntüdür.
	•	100: Minimum eşik değeri (minThreshold). Kenarları tespit etmek için düşük eşik değeridir. Bu değerin altında kalan pikseller kenar olarak kabul edilmez.
	•	200: Maksimum eşik değeri (maxThreshold). Bu değerin üzerindeki pikseller kenar olarak kabul edilir."""    
    
    
    cv2.imshow("Frame",frame)
    cv2.imshow("kenarlı",kenar)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    






    
