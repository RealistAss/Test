def send_mail(message, recipient,*, sender = 'university.help@gmail.com'):

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif '@' not in  recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient.endswith ('.com' or '.ru' or '.net'):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)

    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)

    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_mail('Alpen gold', 'university.help@gmail.com', )
send_mail('Milka', 'Ilyamolot.mail.ru')
send_mail('Dove', 'Ilyamolot@mail.ru')
send_mail('Crispy', 'Ilyamolot@mail.ru', sender ='yamolot@mail.ru' )