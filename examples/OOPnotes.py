### PROJECT NOTES! ###


# Client wanting rental prop calc.

# OOP that will calc ROI for rental props 

# 




# def calculate_total_income(self):
        # Calculate total income based on the number of units and their monthly rents
#            self.total_income = (
#            self.num_small_units * self.monthly_rent_small +
#            self.num_medium_units * self.monthly_rent_medium +
#            self.num_large_units * self.monthly_rent_large +
#            self.num_delux_units * self.monthly_rent_delux +
#            self.num_storage * self.storage +
#            self.num_boat_slip * self.boat_slip +
#            self.num_covered_parking * self.covered_parking
#        )
#        return total_income
#  




class ROI:
    pass

# method = Class + Function 
class Item:

# attributes 
    pay_rate = 0.8

# fuction 
    def __init__(self, name, price, quant, amount):
        # Values 
        self.name = name
        self.price = price
        self.quant = quant
        self.amount = amount
        
    def calculate_total_price(self):
        return self.price * self.quant
    
    def apply_disc(self):
        self.price = self.price * Item.pay_rate

#instance
item1 = Item("phone", 100, 5, "Text" )
item1.apply_disc()
print(item1.price)


#print(item1.name)
#print(item1.quant)
#print(item1.amount)
#print(item1.price)

#print(item1.calculate_total_price())