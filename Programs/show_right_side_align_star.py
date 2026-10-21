# below both approaches will give the same output
n = int(input("Enter a Number: "))
for i in range(1, n+1):
    print("*" * i + " " * (n - i))
print('')

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print('')


#Output:
# *         
# **        
# ***       
# ****      
# *****     
# ******    
# *******   
# ********  
# ********* 
# **********