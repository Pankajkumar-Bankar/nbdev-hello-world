# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/testing.ipynb.

# %% auto 0
__all__ = ['add', 'subtract', 'multiply', 'divide']

# %% ../nbs/testing.ipynb 2
def add(x,y):
    """This is add function"""
    return x + y
 
def subtract(x,y):
    """This is subtract function"""
    return x - y

def multiply(x,y):
    """This is multiply function"""
    return x * y

def divide(x,y):
    """This is divide function"""
    if y == 0:
        raise ValueError("Cannot divide by 0")
        
    return round(x / y,2)
