from PIL import  Image

def visualization(path : str) ->None:
    with open(path, 'rb') as obj:
        img = Image.open(obj)
        img.show()
visualization('/home/developer/Desktop/zakat.jpg')

