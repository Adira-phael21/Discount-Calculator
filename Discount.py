# Function to calculate the discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price < original_price:
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: {original_price:.2f}")
