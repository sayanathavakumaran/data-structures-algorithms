class Phone():
    def __init__(self,model,battery,colour):
        self.model = model
        self.battery = battery
        self.colour = colour

    def get_model(self):
        return self.model
    def set_battery(self,battery):
        self.battery = battery
    def get_battery(self):
        return self.battery
    def get_colour(self):
        return self.colour

    def use_app(self):
        if self.battery <= 0:
            print("you have no battery left")
        else:
            self.battery -= 1

    def charge(self):
        if self.battery >= 100:
            print("your battery has reached 100%")
        else:
            self.battery += 1

person1 = Phone("iPhone 13",21,"dark blue")
action = input("do you want to use an app or charge the phone? ")
if action == "use app" or action == "use an app":
    number = int(input("how long are you going to use the app for? "))  
    for x in range(number):
        if person1.get_battery()>0:
            person1.use_app()
        else:
            break
    print(f"battery: {person1.get_battery()}")
elif action == "charge the phone" or action == "charge":
    number = int(input("how long are you going to charge the app for? "))  
    for x in range(number):
        if person1.get_battery()<100:
            person1.charge()
        else:
            break
    print(f"battery: {person1.get_battery()}")

