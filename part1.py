"""
Define a function sumofsquares that takes an integer input number. The function then adds all the first n perfect squares (starting from 1).

For example, sumofsquares(3) should return 14, since 1 + 4 + 9 = 14.
"""

def sumofsquares(number):
  sums = []
  while number > 0:
    for i in range (0,number):
      sums.append (i * i)
    print(sum(sums))



#not sure what i did pls fix



"""
if program == "1":
  n = int(input("Enter a number: "))
  print(part1.sumofsquares(n))

#need to work on
"""