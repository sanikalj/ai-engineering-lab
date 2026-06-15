from  typing import List

# labelling a simple variable
username : str = "Tom"

#labelling a function with input and output
def calculate(price:float, quantity:int) ->float:
    return price * quantity
print(calculate(1.99, 2))