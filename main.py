# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = ('dog',1,'слон', True, 0,'apple')
print(type (immutable_var ))
print(immutable_var )
print(immutable_var [0])
# immutable_var.appeng("zero") # выдает ошибку так как "Кортеж"
# immutable_var = ([3]) # Не добавляет элемент, а просто создает новый кортеж
# print(immutable_var )
# immutable_var.remove('слон')
# print(immutable_var ) #  так же не убирает элемент а выдает ошибку
# Вывод кортеж дествительно отличается от списков.. и не все действия выполняет как списки..

mutable_list= [1,'Vitali',"T", 0.1,2,True]
print(type(mutable_list))
print(mutable_list)
mutable_list [0]="E-mail"
print(mutable_list)
mutable_list.remove(0.1)
print(mutable_list[0:5:2])
print('T' in mutable_list)
print(('T' not in mutable_list))
