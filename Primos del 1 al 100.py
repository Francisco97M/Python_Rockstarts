for n in range(0, 100, 1):
   if n > 1:
       for i in range(2,n,1):
           if (n % i) == 0:
               break
       else:
           print(n)