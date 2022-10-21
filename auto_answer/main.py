import analyzer
i = 1
name = input('Как вас зовут? ')

for i in range (1,80):

    req = input("\033[33m\n"
                "\nЧто вы хотите узнать? \n1. расписание, \n2. стоимость занятий, \n3. контакты, \n4. фотографии, "
                    "\n5. карта, \n6. присоединиться к занятиям, \n7. завершить \nвведите запрос: : ")
    analyzer.main(req,name)
    i += 1
    if 'прис' in req:
        break
    elif 'заверш' in req:
        break



