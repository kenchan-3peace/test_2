いいい
import socket
import time

tello_ip = '192.168.10.1'
tello_port = 8889

#udpソケット作成
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)

#コマンドモードを使うため'command'というテキストを投げる
socket.sendto('command'.encode('utf-8'),tello_address)
print('離陸準備')
time.sleep(5)
#コマンドモードを使うため'command'というテキストを投げる
print('電池チェック')
socket.sendto('battery?'.encode('utf-8'),tello_address)
data, server = socket.recvfrom(1518)
print(data.decode(encoding="utf-8"))
time.sleep(5)
