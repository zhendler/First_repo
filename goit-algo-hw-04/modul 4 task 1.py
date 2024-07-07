from pathlib import Path




def total_salary(salary_list_file_path):
    result = {}
   #if salary_list_file_path.is_file():
    with open(salary_list_file_path) as slfp:
        for line in slfp:
            worker_name, salary_amount = line.split(',')
            print(worker_name), print(salary_amount)
            #print(salary_amount)
            salary_amount = salary_amount.rstrip('\n')
            result[salary_amount] = worker_name
            #print(result)
    return result





salary_list_file_path=Path('month_salary.txt')
print(type(salary_list_file_path))
#total_salary(salary_list_file_path)
o = open(salary_list_file_path,'r+')
print(o)