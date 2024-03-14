#code demo for calculating discounts on the 

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        new_price = price - (price * discount_percent / 100) #price after discount 
        return new_price
    else:
        return price

def main():
    original_price = int(input("Enter the original price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print("Final price after applying discount: $", round(final_price, 2))
    else:
        print("No discount applied. Original price: $", round(original_price, 2))

