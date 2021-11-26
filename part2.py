"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 





work on more

def diamond(size):
  for i in range (0, size):
    i = i+1
    print (' ' * int(size-1), '* ' * int(i))
    if i == size:
      i=i-1
      print (' ' * int(size-1), '* ' * int(i))
    #size = size -1

<string>.center(2*size - 1)

print (i.center(2 * size - 1))

elif program == "2":
  s = int(input("Enter diamond size: "))
  part2.diamond(s)

while leg > 0:
    for i in range (0, leg):
      i = i+1 
      print (' ' * int(leg-1), '* ' * int(i))
      leg = leg-1
      
"""


def diamond(size):
  ast = '*'
  space = ' '
  for i in range (0, size+1):
    if i == 1:
      print (ast)
    elif i >= 1:
      #x = ast * i
      print (ast + (space * (2*i-3)) + ast)
  if size >= i:
      print (ast + (space * (2*i-5)) + ast)
      i = i - 1

    
#can't figure out how to get the last few rows and center align
