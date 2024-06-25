immutable_var=1,2,3,'phone',str
print(immutable_var)
#immutable_var[4]=4 В Python кортежи являются неизменяемыми последовательностями, то есть их элементы не могут быть изменены после создания. Это означает, что попытка изменить элемент кортежа приведёт к ошибке.
mutable_list=[1,2,'apple','orange']
mutable_list[1]='coconud'
print(mutable_list)

