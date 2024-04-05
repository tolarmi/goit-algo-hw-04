
def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None
    
    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)