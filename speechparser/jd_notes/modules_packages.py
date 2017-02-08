
# each file is a module
# each folder with __init__.py is a package

from my_module import my_sum
from my_module import my_sum
import my_module
import my_module as mm
from my_module import my_sum as ms

from my_package import package_module
from my_package.package_module import factorial
from my_package.package_module import factorial as fact

# using modules
print(my_sum(5, 6))
print(my_module.my_sum(5, 6))
print(mm.my_sum(1, 2))
print(ms(6, 7))

# using packages
print(package_module.factorial(5))
print(factorial(6))
print(fact(7))

