from pathlib import PurePath




def total_salary(salary_list_file_path):
    try:
        total_salary=0
        salary_list=[]
        with open(salary_list_file_path) as slfp:
            for line in slfp:
                worker_name, salary_amount = line.split(',')
                salary_list.append(salary_amount)
                total_salary+=float(salary_amount)
            avarage_salary=total_salary/len(salary_list)
            #print(total_salary)
            #print(avarage_salary)
            return total_salary, avarage_salary
    except FileNotFoundError:
        print(f"File not found: {salary_list_file_path}")
        return (0, 0)
    except Exception as e:
        print(f"Error: {e}")
        return (0, 0)
    





salary_list_file_path=PurePath(r'C:\Users\Dell\Documents\First_repo\goit-algo-hw-04\month_salary.txt')

#total_salary(salary_list_file_path)
total, average = total_salary(salary_list_file_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")