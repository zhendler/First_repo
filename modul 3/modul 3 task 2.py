import random


def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<=1000 and max>min and quantity<max-min+1:
        check=True
    else:
       print('WRONG!!!!'),
       check=False
    if check:    
        winners_set=set()
        while len(winners_set) < quantity:
            random_number = random.randint(min,max)  
            winners_set.add(random_number)
            result=(f'The list of winning numbers is {winners_set}')
    else:
        result=('U did something wrong, pls start over')
    return print (result)
    

get_win_list = get_numbers_ticket(20,30,5) 
