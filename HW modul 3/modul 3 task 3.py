import re

p_numbers=("    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
    )
def normalize_phone(number):
    valid_number=re.sub(r'[^\d+ ]','',number)
    valid_number=valid_number.replace(' ','') 
    while len(valid_number)>10:
        valid_number=valid_number[1:]

    return '+38' + valid_number 
    
#normalize_phone('38050-111-22-22')
final_valid_numbers=[]    
for number in p_numbers:
    final_valid_number=normalize_phone(number)   
    final_valid_numbers.append(final_valid_number)

print(f'Here is list of valid phone numbers: {final_valid_numbers}')
