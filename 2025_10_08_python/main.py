total_price = 0
cart = dict()

def add_item(item, price):
    cart[item] = price

def calculate_total(cart):
    total = sum(cart.values())
    return total


def apply_discount(total_price, discount):
    return total_price - (total_price * (discount/100))


item_count = int(input("Kérlek add meg számmal hogy mennyi minden van a kasszádon, és utána egyesével bekérjük őket!\n"))

for i in range(item_count):
    add_item(str(input("Kérlek add meg hogy mit vásárolt a vásárló! \n")), float(input("Kérlek add meg mennyibe került!\n")))

total_price = calculate_total(cart)
print("Eddig ennyit ér a kosara:", total_price)

discount_checker = str(input("Kérlek add meg hogy van e kuponja az illetőnek a következőképpen i/n \n"))
if discount_checker == "i":
    discount = int(input("Kérlek add meg mekkora a kedvezmény! 1-100! "))
    total_price = apply_discount(total_price, discount)
    print("Mivel volt kedvezmény, ezért a végösszeg:", total_price, "huf")

