import os
import registration as reg
import mail_send as send
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

archive_zip = zipfile.ZipFile(BASE_DIR, 'w') #Работаем над этим


#m_reg = reg.MailReg(BASE_DIR)
#m_reg.yandex_registation(BASE_DIR)
#print("Почта создана! Данные об аккаунте сохранены в файл '/Data/Created_accounts.txt'")

#m_send = send.MailSend(BASE_DIR)
#m_send.log_in_yandex()
#m_send = send.MailSend(BASE_DIR)
#m_send.send_mail(BASE_DIR)


print("Выполнение скрипта завершено")



