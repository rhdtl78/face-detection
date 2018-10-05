import requests
import socket

def sendPic ():
    with open('image.jpg', 'rb') as file:
        data = file.read();
        files = {'file': ('image.jpg', file, 'image/jpeg', {'Expires': '0'})}
        url='http://14.64.173.105:3000/savepic'
        response=requests.post(url=url, files=files)
        print(response.json())

if __name__ == "__main__" :
	sendPic();
