class Car:
    count = 0
    def __init__(self, var1, var2):
        self.color = var1
        self.speed = var2
        Car.count += 1

    def upSpeed(self, num):
        self.speed += num

    def downSpeed(self, num):
        self.speed -= num

    def getSpeed(self):
        print("현재 속도: %d" % (self.speed))

    def getColor(self):
        print("차량 색: %s" % (self.color))

    def getNum(self):
        print("차량 총 수: %d" % (Car.count))

class Sedan(Car):
    def __init__(self, var1, var2, var3):
        self.num = var1
        Car.__init__(self, var2, var3)

    def getPassenger(self):
        print("차량의 좌석 수: %d" % (self.num))

class Truck(Car):
    def __init__(self, var1):
        self.load = var1

    def getLoad(self):
        print("차량의 적재량: %d" % (self.load))

s1 = None; t1 = None;
s2 = None; t2 = None;

s1 = Sedan(4, "red", 50)
t1 = Truck(100)
s2 = Sedan(5, "yellow", 40)
t2 = Truck(1000)

s1.getSpeed()
#s1.getColor()
s1.getPassenger()


#t1.getSpeed()
#t1.getColor()
t1.getLoad()



         

        
