import os
import registration as reg
import mail_send as send

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#y_reg = reg.YandexReg(BASE_DIR)
#y_reg.yandex_registation()
#y_send = send.YandexMailSend(BASE_DIR)
#y_send.yand_send_mail()

#g_reg = reg.GMailReg(BASE_DIR)
#g_reg.gmail_registation()

m_reg = reg.MailruReg(BASE_DIR)
m_reg.mailru_registation()

print("Выполнение скрипта завершено")



