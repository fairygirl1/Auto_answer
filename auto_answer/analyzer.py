
from PIL import Image

def main(req,name):
    dict_schedule = {
        'Wogue': 'Tue at 7 pm and Fri at 2 pm',
        'Hills': 'Wed at 9 pm and Sun at 8 pm',
        'Hip-Hop': 'Mon at 4 pm and Sat at 5 pm',
        'Lasting of all classes': '2 hours per day'
    }

    dict_price = {
        'Wogue': '2500 rub per one class',
        'Hills': '3600 rub per one class',
        'Hip-Hop': '2100 rub per one class'
    }

    dict_contacts = {
        'Wogue': 'Anastasia, +7(950)900-00-00',
        'Hills': 'Valeria, +7(900)666-66-66',
        'Hip-Hop': 'Maxim, +7(300)333-33-33'
    }







    if 'расп' in req or '1' in req:
        schedule(dict_schedule)
    elif 'стоим' in req or '2' in req:
        price(dict_price)
    elif 'конт' in req or '3' in req:
        contacts(dict_contacts)
    elif 'фот' in req or '5' in req:
        q = int(
            input("\n____________________________________________________________________________________________"
                  "\nКакой стиль вам больше нравится? \n1. вог,\n2. хиллс,\n3. хип-хоп\nнапишите номер: : "))
        if q == 1:
            pic_vogue()
        elif q == 2:
            pic_hills()
        elif q == 3:
            pic_hop()
        else:
            print("К сожалению, запрос не верный((")
    elif 'карт' in req or '5' in req:
        direction()
    elif 'присоед' in req or '6' in req:
        print('Спасибо за обращение! Мы скоро с вами свяжемся.')


    elif 'заверш' in req or '7' in req:
        print( + 'Хорошего дня!')
    else:
        print("К сожалению, запрос не верный((")






def schedule(dict):
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))

def price(dict):
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))

def contacts(dict):
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))

def pic_vogue():
    for i in range(1, 4):
        img = Image.open(f'/home/alexandra/pythonProject/auto_answer/pic/{i}.jpg')
        img.show()

def pic_hills():
    for i in range(4, 7):
        img = Image.open(f'/home/alexandra/pythonProject/auto_answer/pic/{i}.jpg')
        img.show()

def pic_hop():
    for i in range(7, 10):
        img = Image.open(f'/home/alexandra/pythonProject/auto_answer/pic/{i}.jpg')
        img.show()

def direction():
    import webbrowser
    webbrowser.open('https://goo.gl/maps/nKTUXZvUYXwAmqxQ8')





