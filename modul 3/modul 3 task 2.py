import random


def get_numbers_ticket(min, max, quantity):
    if min<1 and max<1000 and max<min and quantity<max-min+1:
        print('u do it wrong')
    else:
        winners_set=set()
        while len(winners_set) < quantity:
            random_number = random.randint(min,max)  
            winners_set.add(random_number)
    return print (f'The list of winning numbers is {winners_set}')
 #   else: 
 #       print('nnnnn')        
                        

get_win_list = get_numbers_ticket(1,5555,5) 
