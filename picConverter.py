from PIL import Image
class picConverter:

    def converter(self, path):
        # img = Image.open(path)
        stop =0
        for i in range(len(path)):
          if(path[i]=="."):
            stop = i
        print(path[stop:])

path = input("paste the image path here: ")

obj = picConverter()
obj.converter(path)

