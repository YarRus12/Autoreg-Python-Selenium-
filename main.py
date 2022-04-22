import os
import registration as reg
import mail_send as send

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

y_reg = reg.YandexReg(BASE_DIR)
y_reg.yandex_registation()
y_send = send.YandexMailSend(BASE_DIR)
y_send.yand_send_mail()

print("Выполнение скрипта завершено")