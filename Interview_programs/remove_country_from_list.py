# if we remove country which name start from c then why some country is remaining that name start with 'c'
countries = ['America', 'Canada', 'India', 'Australia', 'China', 'Chile', 'California']
for c in countries:
	if c.startswith('C'):
		countries.remove(c)
print(countries)
# output is : ['America', 'India', 'Australia', 'Chile']

'''
    This happens because you are modifying (removing items from) the list while iterating over it. 
    When Python removes an element, the indexes shift, and the loop skips the next item.
    
    First Iteration
        c = 'America'   Does it start with C
    List stays same.
    
    Second Iteration
        c = 'Canada'    Starts with C
        Python removes it.
    Updated list is : ['America', 'India', 'Australia', 'China', 'Chile', 'California']
    But now indexes shift.
    
    Next Iteration
        c = 'Australia'
    
    'India' was skipped because the list shifted.
    
    Next:
        c = 'China'     remove it 
    
    Updated list is : ['America', 'India', 'Australia', 'Chile', 'California']
    Now Python jumps forward again and skips 'Chile'.
    Because 'Chile' was skipped during iteration.
    
    Why This Happens ?
        - When you remove elements during iteration:
        - list size changes
        - indexes shift
        - some elements are skipped
        
    Correct way:
    
        countries = ['America', 'Canada', 'India', 'Australia', 'China', 'Chile', 'California']
        countries = [c for c in countries if not c.startswith('C')]
        print(countries)
'''