class Gadgets:
    def start(self):
        print("Gadget started")

class Phone(Gadgets):
    def start(self):
        print("Nokia is starting")

class Laptop(Gadgets):
    def start(self):
        print ("Laptop is starting")  

gadgets = [Phone(), Laptop()]

for gadget in gadgets:
    gadget.start()

class CameraFeature:
    def takephoto(self):
        print("Photo taken")

class WifiEnabled:
    def connect_wifi(self):
        print("Connected to WIFI")    

##Inheritance from multiple classes
class SmartPhone(Phone, CameraFeature, WifiEnabled):
    def start(self):
        print("Smart Phone is starting")            

class SmartPrinter(Gadgets, WifiEnabled):
    def start(self):
        print("Smart Printer is starting")            

##Array
devices = [SmartPhone(), SmartPrinter()]

for device in devices:
    device.start()
    if isinstance(device, CameraFeature):
        device.takephoto()
    if isinstance(device, WifiEnabled):
        device.connect_wifi()    