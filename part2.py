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
"""

def diamond(size):
  for i in range (0, size):
    i = i+1
    print (' ' * int(size-1), '* ' * int(i))
    if i == size:
      i=i-1
      print (' ' * int(size-1), '* ' * int(i))
    #size = size -1


"""
work on more


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