'''
PROJECT : 
You are tasked with implementing a simple shopping cart for an online store. The cart should 
be able to perform the following operations:
Add an item to the cart along with its quantity.
Remove an item from the cart.
Update the quantity of an item in the cart.
Calculate the total cost of all items in the cart

'''


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
        else:
            print(f"{item} not found in the cart.")

    def update_quantity(self, item, quantity):
        if item in self.cart:
            self.cart[item] = quantity
        else:
            print(f"{item} not found in the cart.")

    def calculate_total_cost(self):
        total_cost = 0
        for item, quantity in self.cart.items():
            # Replace the below line with the actual cost of each item from your store
            item_cost = 10  # Example: Assume each item costs $10
            total_cost += item_cost * quantity
        return total_cost

    def view_cart(self):
        print("\nShopping Cart:")
        for item, quantity in self.cart.items():
            print(f"{item}: {quantity}")


# Test the shopping cart
if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_item("Shirt", 2)
    cart.add_item("Pants", 1)
    cart.add_item("Shoes", 1)

    cart.view_cart()

    cart.update_quantity("Shirt", 3)
    cart.remove_item("Pants")

    cart.view_cart()

    total_cost = cart.calculate_total_cost()
    print(f"\nTotal Cost: ${total_cost}")
