import sys

def getSubTotal():
    subtotal = float(sys.argv[1])*float(sys.argv[2])
    return subtotal 
    

def discountItems(subTotal):
    
    discount = 0
    
    if subTotal >= 1000 and subTotal < 5000:
        discount = 0.03
    elif subTotal >= 5000 and subTotal < 7000:
        discount = 0.05
    elif subTotal >= 7000 and subTotal < 10000:
        discount = 0.07
    elif subTotal >= 10000 and subTotal < 50000:
        discount = 0.1
    elif subTotal >= 50000:
        discount = 0.15
        
    return subTotal*(1+discount)
        


def taxItems(discountedSubTotal):
    provinces = {
        "ON":0.13,
        "QC":0.14975,
        "MB":0.05,
        "NS":0.15,
        "BC":0.05
    }
    
    taxRate = provinces.get(sys.argv[3])
    
    return discountedSubTotal*(1+taxRate)


def main():
    
    print("Calculating total price for your items...\n")
    
    subTotal = getSubTotal()
    discountedItems = discountItems(subTotal)
    total = taxItems(discountedItems)
    
    print("Your total is $" + str(round(total,2)))
    
main()
    
    
    
    
    
