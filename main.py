import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jung_logik_l2.settings")

django.setup()


from schedule.models import Subject, Teacher, Class, Student, Schedule, Grade


work = True
while work  == True:
    print("""
        1.Додати предмет
        2.Додати вчителя
        3.Додати клас
        4.Додати учня
        0.Зупинити
    """)
    chois = int(input("виберіть дію: "))
    if chois == 0:
        work = False

    if chois == 1:
        name = input("Назва придмету: ")
        description = input ("Опис: ")
        check = Subject.objects.filter(name = name).first()
        if check:
            print("Вже існує!!!")
        else:    
            Subject.objects.create(name = name, description = description)

    if chois == 2:
        name = input("Ім'я: ")
        last_name = input ("Прізвище: ")
        subject = input ("Назва предмету: ")
        check = Subject.objects.filter(name = subject).first()
        if check:
            Teacher.objects.create(name = name, last_name = last_name, subject = check)
        else:
            print('Такого предмету не існує')

    if chois == 3:
        name = input("Назва класу: ")
        year = int( input ("рік навчання: "))
        check = Class.objects.filter(name = name).first()
        if check:
            print("Вже існує!!!")
        else:    
            Class.objects.create(name = name, year = year)
            print("Клас додано!")



    if chois == 4:
        pass


# Додавання учня:
# Користувач вводить дані про учня (ім'я, прізвище, клас).
# Перевірка наявності класу та збереження у базі даних.