import requests

def sendPic (image):
    params={'image': image}
    files = {'file': ('image.jpg', image, 'image/jpeg', {'Expires': '0'})}
    url='http://14.64.173.105:3000/savepic'
    response=requests.post(url=url, files=files)
    print(response.json())


