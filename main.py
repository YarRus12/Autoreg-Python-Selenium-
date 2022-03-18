import os
import registration as reg
import mail_send as send

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Попробуй передать в цикле
#m_reg = reg.YandexReg(BASE_DIR)
#m_reg.yandex_registation()

m_send = send.YandexMailSend(BASE_DIR)
m_send.yand_send_mail()

print("Выполнение скрипта завершено")



