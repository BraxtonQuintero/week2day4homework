from IPython.display import clear_output

# Step 1
def address_book(my_book={}): # Step 2
    
    while True: # Step 3
        
        # Step 4
        name = input('What is the name you would like to add to your address book? ').title()
        address = input(f"What is {name}'s address? ")
        
        # Step 5
        my_book[name] = address
        clear_output()
        ask = input('Would you like to continue? y/n ').lower()
        
        while ask not in {'y', 'n'}:
            clear_output()
            ask = input('That is not a valid response. Please type y or n ')
            
        # Step 6
        if ask == 'n':
            clear_output()
            break
    
    # Step 7
    for name, address in my_book.items():
        print(f"{name} lives at {address}")
        
    return my_book
        
# Step 8
my_address_book = address_book() 



person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']

# Available Times: '12:00' and '14:30'
# Think intersect

# input the lists with all times 
# outputs the time that intersects between person 1-4
# use intersect, make an empty list
# make a list cross referencing all list and seeing if we can pull the times out of the list that match each individual

person5 = set(person1)
person6 = set(person2)
person7 = set(person3)
person8 = set(person4)
def available_times(*args):
    for a in args:
        return a & a
available_times(person5 & person6 & person7 & person8)