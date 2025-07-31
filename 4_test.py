square=[]
class Rectangle:
    def __init__(self,horizontal,vertical,height):
        self.horizontal=horizontal
        self.vertical=vertical
        self.height=height
    #function to calculate the area
    def calc_area(self):
        return self.horizontal*self.vertical
    #funtion to calculate the volume 
    def calc_volume(self):
        return self.horizontal*self.vertical*self.height

#function to create instances that will be used by class rectangle
def create_instance():
    global square
    r1 = Rectangle(3, 4, 5)
    r2 = Rectangle(50, 60, 70)
    r3 = Rectangle(333, 444, 555)
    square=[r1,r2,r3]
#function to generate the output message and and excute 
def play():
    create_instance()
    for i in square:
      area=i.calc_area()
      print(f"Area is {area}")
      volume=i.calc_volume()
      print(f"volume is {volume}")

#staring program
play()