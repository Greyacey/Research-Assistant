#The function will be written using the following approach:
#1.	Get the form k*2n, if the given number is a proth number, by deducting 1.
#2.	Then, check if k can divide n in such a way that ( n/k ) is a power of 2 or not by looping through all odd number starting form k=1 to n/k.
#3.	If such k is found, print ‘The number is a Proth Number’
#4.	If no such value of k is found then Print ‘Not a Proth Number’

#The implementation in Python 3 is seen below

def powerofTwo(n):  
        
    return (n and (not(n & (n - 1))))   
      
      
# to check if the given number is Proth number or not 
def isProthNumber( n): 
  
       k = 1
      
    while(k < (n//k)): 
          
        # check if k divides n or not 
        if(n % k == 0): 
  
            # Check if n / k is power of 2 or not 
            if(powerofTwo(n//k)): 
                    return True
          
   
        # update k to next odd number 
        k = k + 2       
      
      
    # If we reach here means 
    # there exists no value of K 
    # Such that k is odd number   
    # and n / k is a power of 2 greater than k 
    return False
          
              
              
# Driver code 
  
# Get n 
    int n = 25; 
  
# Check n for Proth Number 
if(isProthNumber(n-1)): 
    print("The number is a Proth Number"); 
else: 
    print("Not a Proth Number"); 
