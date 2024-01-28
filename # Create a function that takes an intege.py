# Create a function that takes an integer as an argument and returns "Even" for even numbers and "Odd" for odd numbers

#write func that takes in an int
#evaluate wether that int is even or odd
#using an if statement combined with % to s=check remainder of division by 2
#return string of Even or Odd depending on the num


#def even_or_odd(num):
    #if num % 2 == 0:
        #return "Even"
   # else:
        #return "Odd"
    
#print(even_or_odd(11))

class Cart():

    def __init__(self, add, remove, show):
        self.add = add
        self.remove = remove
        self.show = show

        cart_dict = {}
        while True:
            user_action = input("Would you like to add/show/remove? Enter 'quit' to exit: ")
            if user_action.lower() == 'quit':
                break
            elif self.add == 'add':
                item = input('What would you like to add? ')
                quantity = int(input('How many?: '))
                if item in cart_dict: 
                    cart_dict[item] += quantity

                else:
                    cart_dict[item] = quantity
                    print(f"{quantity} {item} added to cart.")
            elif self.show == 'show':
                    print(f"{cart_dict}")
            elif self.remove == 'remove':
                item = input('What to remove?')
                if item in cart_dict: 
                    delete_frm_cart = int(input(f'How many {item} would you like to remove?'))
                    if delete_frm_cart >= cart_dict[item]:
                        del cart_dict[item]
                    else:
                        cart_dict[item] -= delete_frm_cart

fruit_cart = Cart()
                    
#def info(self):
    #print(f'{s}')               
