class FoodOrder():
    def __init__(self,orderid,customer,foodprice,deliveryprice):
        self.orderid = orderid
        self.customer = customer
        self.foodprice = foodprice
        self.deliveryprice = deliveryprice
    def show_order(self):
        print(self.orderid)
        print(self.customer)
        print(self.foodprice)
        print(self.deliveryprice)
class Standard(FoodOrder):
    def __init__(self,orderid,customer,foodprice,distance,deliveryprice,time):
        FoodOrder.__init__(self,orderid,customer,foodprice,deliveryprice)
        self.distance = distance
        self.time = time
    def show_order(self):
        print("standard order")
        print("*************")
        FoodOrder.show_order(self)
        print(self.distance)
        print(self.time)
        print("")

class Express(FoodOrder):
    def __init__(self,orderid,customer,foodprice,extrafee,extrasides,deliveryprice):
        FoodOrder.__init__(self,orderid,customer,foodprice,deliveryprice)
        self.extrafee = extrafee
        self.extrasides = extrasides
    def show_order(self):
        print("express order")
        print("*************")
        FoodOrder.show_order(self)
        print(self.extrafee)
        print(self.extrasides)

standardorder = Standard(1234,"customer1","£29.09","3km","£1.57","10 minutes")
standardorder.show_order()
expressorder = Express(1234,"customer1","£29.09","£5.17","mayonnaise","£1.57")
expressorder.show_order()
