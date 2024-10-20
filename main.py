# ДЗ 8.3. Унікальне число
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
# знаходить серед них унікальне число та повертати його. Унікальне число - це число,
# яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел,
# перевіряти не потрібно.
# Приклад:
# def find_unique_value(some_list):
#    pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")
def add_one(some_list):
   add_1=1 #доданок 1
   number="".join([str(y) for y in some_list]) #записуємо список числом
   number=int(number)+add_1 #додаємо до числа доданок
   str1=str(number) #робимо число рядком, щоб порахувати довжину
   lst1=[] #порожній список
   i=0
   while i < len(str1): #в циклі створюємо новий список
       lst1.append(int(str1[i])) #додаємо елементи у список
       i += 1 # крок
   return lst1 #повертаємо новий список
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")