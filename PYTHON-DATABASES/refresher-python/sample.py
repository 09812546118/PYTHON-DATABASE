"""
 A program that would accept two (2)
  values and display the sum, difference,product,quotient
  of the inputted values
"""
#import the necessary library for clearing the screen
from os import system

#this function main
## define
def main():
  system ("cls") # clear the screen
  a = int(input("Enter first value:"))
  b = int(input("Enter first value:"))
  sum = a + b
  dif = a - b
  prod = a * b
  quot = a / b
  print (f"The sum of %d and %d is %d"%(a,b,sum,))
  print (f"The sum of %d and %d is %d"%(a,b,dif,))
  print (f"The sum of %d and %d is %d"%(a,b,prod,))
  print (f"The sum of %d and %d is %f"%(a,b,quot,))
  #main trigger
if __name__=="__main__":
	main()