# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

prices = {1:"570000$", 2:"68000$", 3:"450000$", 4:"8900$", 5:"4500$"}

for price, car in enumerate(cars, start=1):
    print ("car: %s  price: %s"%(car, prices[price]))

for price, car in enumerate(cars, start=1):
    print("accessory: %s  price: %s"%(accessories, prices[price+len(cars)]))    

# i see that it's working fine. But, I really don't understand this.

# eta hocche na