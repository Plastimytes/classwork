#1.Define Class for Engines
class Engine:
    def __init__(self, name, horsePorwer, Cylinders, Capacity, BoreWidth):
        #Attributes
        self.name=name
        self.horsePower=horsePorwer
        self.Cylinders=Cylinders
        self.Capacity=Capacity
        self.BoreWidth=BoreWidth

    #Print stsatement/method
    def display_info(self):
        return(f"This is an engine of the brand {self.name} and horsePower of {self.horsePower} with {self.Cylinders}. A capacity of {self.Capacity} and Bore width of {self.BoreWidth}.")

#Instances
Mitsubishi=Engine('4G63T', 276, '4(Inline)', '2.0L', '85mm')
Toyota=Engine('2JZ-GTE', 276, '6(Inline)', '3.0L', '86mm')
Nissan=Engine('RB26DETT', 276, '6(Inline)', '2.6L', '86mm')
Honda=Engine('K20A', 246, '4(Inline)', '2.0L', '86mm')
Mazda=Engine('13B-REW', 276, 'Rotary', '1.3L', 'N/A')         

#Accessing attributes in each instance
print("----Engine----")
print(Mitsubishi.display_info())
print(Toyota.display_info())
print(Nissan.display_info())
print(Honda.display_info())
print(Mazda.display_info())



#Define Class for Dinosaurs
class Dino:
    def __init__(self, name, height, weight, type, age):
        #Attributes
        self.name=name
        self.height=height
        self.weight=weight
        self.type=type
        self.age=age

    #Print stsatement/method
    def display_info(self):
        return(f"This is a dinosaur of the name {self.name}, height of {self.height} and a weight of {self.weight}. It is of the {self.type} type and is from the {self.age} age.")

#Instances
Tyrannosaurus=Dino('T-Rex', '4.8-5.4m', '5700-7000kg', 'Canivoruos', 'Cretaceous')
Velociraptor=Dino('Velociraptor', '0.5m', '14-19kg', 'Canivoruos', 'Cretaceous')
Stegosaurus=Dino('Stegosaurus', '4.5m', '3800kg', 'Herbivorous', 'Jurrassic')
Triceratops=Dino('Triceratops', '3m', '9000kg', 'Herbivorous', 'Cretaceous')
Brachiosaurus=Dino('Brachiosaurus', '15m', '46900kg', 'Herbivorous', 'Jurrassic')        

#Accessing attributes in each instance
print("----Dinosaurs----")
print(Tyrannosaurus.display_info())
print(Velociraptor.display_info())
print(Stegosaurus.display_info())
print(Triceratops.display_info())
print(Brachiosaurus.display_info())


#Define Class for Hair
class Hair:
    def __init__(self, type, texture, styling, porosity, maintenance):
        #Attributes
        self.type=type
        self.texture=texture
        self.styling=styling
        self.porosity=porosity
        self.maintenance=maintenance

    #Print stsatement/method
    def display_info(self):
        return(f"This is hair of the type {self.type}, with a {self.texture} texture and requires a styling of {self.styling}. It is of the porosity {self.porosity} porosity type and requires a maintenance {self.maintenance}.")

#Instances
Straight=Hair('1', 'fine', 'curls', 'low', 'frequent washing')
Wavy=Hair('2', 'medium', 'curls', 'medium', 'moisture balance')
Curly=Hair('3', 'voluminous', 'gentle', 'high', 'requires moisturizing')
Coily=Hair('4', 'delicate', 'braid', 'high', 'gentle handling')
Regular=Hair('5', 'medium', 'curls', 'medium', 'washing')        

#Accessing attributes in each instance
print("----Hair----")
print(Straight.display_info())
print(Wavy.display_info())
print(Curly.display_info())
print(Coily.display_info())
print(Regular.display_info())


#1.Define Class for Trains
class Train:
    def __init__(self, name, horsePorwer, length, Capacity, weight):
        #Attributes
        self.name=name
        self.horsePower=horsePorwer
        self.length=length
        self.Capacity=Capacity
        self.weight=weight

    #Print stsatement/method
    def display_info(self):
        return(f"This is a train of the type; {self.name} and horsePower of {self.horsePower} with a length of {self.length}. A capacity of {self.Capacity} passengers and weight of {self.weight}.")

#Instances
Hspt=Train('High-Speed Passenger train', 8000, '800', '1000', '400-800')
Hhft=Train('Heavy-Haul Freight train', 6000, '4000', '10000', '20000')
Crt=Train('Commuter rail train', 1000, '500', '1500', '150-400')
Mag=Train('Maglev', 10000, '300', '1000', '200')
Steam=Train('Steam train', 6000, '100', '100', '200')         

#Accessing attributes in each instance
print("----Train----")
print(Hspt.display_info())
print(Hhft.display_info())
print(Crt.display_info())
print(Mag.display_info())
print(Steam.display_info())



#Define Class for Dinosaurs
class Brick:
    def __init__(self, name, length, weight, type, use):
        #Attributes
        self.name=name
        self.length=length
        self.weight=weight
        self.type=type
        self.use=use

    #Print stsatement/method
    def display_info(self):
        return(f"This is a brick of the name {self.name}, length of {self.length} and a weight of {self.weight}. It is of the {self.type} type and is used for {self.use}.")

#Instances
CB=Brick('Common Burnt', '220', '3.6', 'solid', 'Walls')
FB=Brick('Facing', '215', '3.2', 'Solid', 'External facades')
EB=Brick('Engineering', '220', '4.1', 'Low Absorption', 'Structural')
FiB=Brick('Fire Bricks', '229', '4.5', 'Low thermal', 'Furnaces')
PB=Brick('Perforated', '220', '2.7', 'Perforated', 'Walls')        

#Accessing attributes in each instance
print("----Bricks----")
print(CB.display_info())
print(FB.display_info())
print(EB.display_info())
print(FiB.display_info())
print(PB.display_info())


