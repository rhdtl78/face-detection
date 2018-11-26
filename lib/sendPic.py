import requests


def sendPic():
	try:
		with open('image.jpg', 'rb') as file:
			data = file.read()
			files = {'file': ('image.jpg', data, 'image/jpeg', {'Expires': '0'})}
			url = 'http://apex-openface-server.herokuapp.com/savepic'
			response = requests.post(url=url, files=files)
			print(response.json())
	except FileNotFoundError:
		print ("image not exists")
	except ConnectionError:
		print ("Connection Error")


if __name__ == "__main__":
	sendPic()
