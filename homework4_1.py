def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None
    
    if count == 0:
        print("Файл містить недостатньо даних")
        return None
    
    average = total / count
    
    return total, average


total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")