# -*-coding: utf-8 -*-
import cv2

#사전 처리로 패턴 감지.
def detect(img, cascade):
    rects = cascade.detectMultiScale(img,
                                     scaleFactor=1.3,
                                     minNeighbors=4,
                                     minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


# cap 이 정상적으로 open이 되었는지 확인하기 위해서 cap.isOpen() 으로 확인가능
cap = cv2.VideoCapture(1)

if (cap.isOpened()) :
    print 'Cannot Open Cam'

# cap.get(prodId)/cap.set(propId, value)을 통해서 속성 변경이 가능.
# 3은 width, 4는 heigh

print 'width: {0}, height: {1}'.format(cap.get(3),cap.get(4))
cap.set(3,900)
cap.set(4,900)


#얼굴 인식 패턴
face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
while(True):
    # ret : frame capture결과(boolean)
    # frame : Capture한 frame
    ret, frame = cap.read()

    if (ret):
        # image를 Grayscale로 Convert함.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray) #히스토그램 생성??
        rects = detect(gray, face)
        draw_rects(frame, rects, (0,255,0))
        sub_frame = frame.copy()
        for x, y, w, h in rects:
            sub_gray = gray[y:y+h, x:x+w]
            sub_color = sub_frame[y:y+h, x:x+w]
            eye_rects = detect(sub_gray.copy(), eye)
            draw_rects(sub_color, eye_rects, (255,0,0))

        cv2.imshow('frame', frame)
        #q로 닫기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
