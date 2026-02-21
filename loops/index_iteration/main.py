prices = [29.99, 45.50, 12.75, 38.2]
          
for price in range(len(prices)):
    if price == 0:
        multiplier = 0.90    # 10% off
    elif price == 1:
        multiplier = 0.80    # 20% off
    elif price == 2:
        mulitplier = 0.85    # 15% off
    elif price == 3:
        mulitplier = 0.95    # 95% off
        
    prices[price] *= multiplier
    
    print(f"Updated price for item {price}: ${prices[price]:.2f}")
