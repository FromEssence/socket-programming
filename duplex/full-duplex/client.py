import socket
import os
from threading import Thread

s = socket.socket(2,1)
s.connect(('127.0.0.1', 9001))
def recv(s):
    print("执行读取...")
    msg = s.recv(1024)
    print("收到server消息：", msg)
    
def send(s):
    s.send("Hello\n".encode())
    print("执行发送...")

Thread(target=recv, args=(s,)).start()
Thread(target=send, args=(s,)).start()
print("到达源程序底部...")


#s.close()
