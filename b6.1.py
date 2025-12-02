print('NGUYEN NGOC CHI MSSV 245752021610164')
class Circle(object):
    def __init__(self, r):
        """Constructor nhan vao ban kinh cua hinh tron."""
        self.radius = r
    def area(self):
        """Method tinh dien tich hinh tron."""
        return self.radius**2*3.14
#Tao doi tuong Circle voi ban kinh la 2
aCircle = Circle(8)
#In dien tich cua hinh tron
print(aCircle.area())
