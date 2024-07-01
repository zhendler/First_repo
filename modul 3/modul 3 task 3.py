import re

p_numbers=("    +38(050)123-32-34"
    "     0503451234"
    "(050)8889900"
    "38050-111-22-22"
    "38050 111 22 11   "
    )
def normalize_phone(number):
    valid_number=re.sub(r'[^\d+ ]','',number)
    valid_number=valid_number.replace(' ','')                
    print(valid_number)
    
    
for number in p_numbers:
    normalize_phone(number)   



    pass