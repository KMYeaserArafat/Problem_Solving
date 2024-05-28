
# Ominuas-Number
"""
A company sells its products with a unique serial number on it. Company has found that there are some products that
don’t sell well which are identified to have ominous numbers in the serial number of the product. 
So if a serial number of the product contains atmost ’k’ ominous number then it won’t sell.
Given a range form s to e, you need to find number of products 
that would sell, leaving out the products that contains atmost ’k’ ominous numbers.

"""


def CheackSellable_Product():
   sellable_product = 0

   for serialNumber in range(s,e+1):
      ominousCount = 0
      for digit in str(serialNumber):
         if digit in ominous:
            ominousCount+=1
         if(ominousCount>k):
           sellable_product+=1
   
   print(f"Totol Sellable Product : {sellable_product}")

        


s = int(input("Enter the Starting Range : "))
e = int(input("Enter the Ending range : "))
k = int(input("Enter the atmost ominous Number : "))
ominous = ['4', '7']
CheackSellable_Product()