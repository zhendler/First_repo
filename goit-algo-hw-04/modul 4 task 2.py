from pathlib import PurePath


def get_cats_info(cat_info_path):
    try:    
        cats_info = []
        with open(cat_info_path) as cip:
            for line in cip:
                one_cat_data = line.split(',')
                one_cat_info = {
                    'name': one_cat_data[1],
                    'age': one_cat_data[2].rstrip('\n'),
                    'id': one_cat_data[0], 
                                }
                cats_info.append(one_cat_info)
        for cat in cats_info:
            print(cat)
                
    except FileNotFoundError as e:
        print(f"Error: file not found: {e.filename}")
        return []
    except Exception as e:
        print(f"Error happend: {e}")
        return []




cat_info_path = PurePath('goit-algo-hw-04/cats_data.txt')
get_cats_info(cat_info_path)