#!/usr/bin/env puthon3.7

#Python code beings here using continue statement 

count =0 
while count <10 :
  
#For printing only the odd numbers 
  if count % 2 ==0 :
    count +=1
    continue 
  print(f" We're counting odd numbers : {count}")
  count +=1
    
  #Continue will stop the execution of the loop for current iteration 
