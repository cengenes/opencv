import cv2
import numpy as np

webcam = cv2.VideoCapture(0)  # webcam için 0 yazıyoduk

def nothing(x):  # trackbar için dümenden bir fonksiyon oluşturuyoduk.
    pass

cv2.namedWindow("Trackbar")  # trackbar için pencere oluşturuyoduk.
cv2.resizeWindow("Trackbar",500,500)  # trackbar penceremizi tekrar boyutlandırdık,istediğimiz gibi gelmiyo çünkü.500e 500 lük kare oluşturduk.

cv2.createTrackbar("altsınır-H","Trackbar",0,180,nothing)
cv2.createTrackbar("altsınır-S","Trackbar",0,255,nothing)
cv2.createTrackbar("altsınır-V","Trackbar",0,255,nothing)

cv2.createTrackbar("üstsınır-H","Trackbar",0,180,nothing)
cv2.createTrackbar("üstsınır-S","Trackbar",0,255,nothing)
cv2.createTrackbar("üstsınır-V","Trackbar",0,255,nothing)

# setTrackbarPos(), trackbar’ın başlangıç değerini ayarlamak için kullanılır.
cv2.setTrackbarPos("üstsınır-H","Trackbar",180)
cv2.setTrackbarPos("üstsınır-S","Trackbar",255)
cv2.setTrackbarPos("üstsınır-V","Trackbar",255)

while True:
    ret,frame = webcam.read()
    frame = cv2.flip(frame,1)  # bunu aynada gördüğümüz gibi görmek için yapıyoduk.
    
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #	Kullanıcının trackbar’ları hareket ettirmesiyle değişen değerler cv2.getTrackbarPos() ile okunur.
    altsinir_h = cv2.getTrackbarPos("altsınır-H","Trackbar")
    altsinir_s = cv2.getTrackbarPos("altsınır-S","Trackbar")
    altsinir_v = cv2.getTrackbarPos("altsınır-V","Trackbar")
    
    ustsinir_h = cv2.getTrackbarPos("üstsınır-H","Trackbar")
    ustsinir_s = cv2.getTrackbarPos("üstsınır-S","Trackbar")
    ustsinir_v = cv2.getTrackbarPos("üstsınır-V","Trackbar")
    
    alt_color = np.array([altsinir_h,altsinir_s,altsinir_v])
    ust_color = np.array([ustsinir_h,ustsinir_s,ustsinir_v])
    
    # cv2.inRange(), bir görüntü içindeki belirli bir HSV aralığında kalan pikselleri beyaz (255), diğerlerini siyah (0) olarak gösteren bir ikili (binary) maske oluşturur.
    mask = cv2.inRange(frame_hsv,alt_color,ust_color)
    
    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)
    
    if cv2.waitKey(20) % 0xFF == ord("q"):
        break
    
webcam.release()
cv2.destroyAllWindows()
    
    
    
     