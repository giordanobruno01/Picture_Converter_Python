from PIL import Image
class picConverter:

    def converter(self, path):
        img = Image.open(path)
        stop =0
        for i in range(len(path)):
          if(path[i]=="."):
            stop = i
        ext = path[stop:].lower()
        print("The current extension is: ", ext)
        arr = [".jpg", ".jpeg", ".png"]
        
        arr.remove(ext)
        
        for i in range(len(arr)):
          print(i+1," for ",arr[i])
        choice = int(input())
        

path = input("paste the image path here: ")

obj = picConverter()
obj.converter(path)
