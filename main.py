def discount_price(price, discount):
    print(price, discount)
    def apply_discount():
        nonlocal price
        price *= (1-discount)
        print(price)
        return price
    apply_discount() 
        
        

    
    return price
discount_price(100, 0.1)