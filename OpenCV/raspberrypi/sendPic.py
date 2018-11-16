import requests
import socket

def sendPic ():
    with open('image.jpg', 'rb') as file:
        data = file.read()
        files = {'file': ('image.jpg', data, 'image/jpeg', {'Expires': '0'})}
        url='http://localhost:3000/savepic'
        response=requests.post(url=url, files=files)
        print(response.json())

if __name__ == "__main__" :
	sendPic()
