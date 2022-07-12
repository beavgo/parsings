'''Парсинг электронной почты с последующим сохранением
   результатов в excel формате. В данном случае собираются
   адрес отправителя, дата отправки и тема письма'''

import imaplib
from email.parser import BytesParser
from email.policy import default
import pandas


def read_mailbox():
    mail = imaplib.IMAP4_SSL('проткол сервиса, с которым будет соединение', 993)
    mail.login(user='', 
               password='') #заполнить почту и пароль
    mail.select('INBOX')

    result, data = mail.search(None, 'ALL')
    ids = data[0].split()

    mail_parser = BytesParser(policy=default)
    result_dict = {
        'from':[],
        'date':[],
        'subject':[]
    }
    for num in ids:
        typ, data = mail.fetch(num, '(RFC822)')
        headers = mail_parser.parsebytes(data[0][1], headersonly=True)

        result_dict['from'].append(headers['from'])
        result_dict['date'].append(headers['date'])
        result_dict['subject'].append(headers['subject'])

    mail.close()
    mail.logout()
    print('Readng done!')
    return result_dict


def make_table(data):
    data_frame = pandas.DataFrame({'Отправитель': data['from'],
                                   'Тема письма': data['subject'],
                                   'Дата получения': data['date']})
    data_frame.to_excel('data.xlsx')


def main():
    data = read_mailbox()
    make_table(data)


if __name__ == "__main__":
    main()
