# face-detection
OpenCV와 Tensor를 이용하는 얼굴 인식 출입 통보 시스템.

raspberrypi 디렉토리 내부의 cameraShot.py로 사진을 촬영.
facedetect.py에서 cameraShot을 모듈로 추가해 스레드로 3초 딜레이 생성.
사진을 찍고 sendPy로 보내려 했으나 스크립트로 보내려니 연결 거부 발생.
express로 보내니 문제없이 전송됨.
다른 방법 찾는중.
