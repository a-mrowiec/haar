import cv2

logo_cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture(0)
while (1):

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logos = logo_cascade.detectMultiScale(gray, 1.3, 14)

    # add this
    for (x, y, w, h) in logos:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
