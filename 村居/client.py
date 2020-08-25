import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("10.170.64.205", 9001))

while True:
    for i in range(4):
        msg = s.recv(1024)
        print(msg.decode())
        msg_send = input("输入发送信息：\n")
        s.send(msg_send.encode())

    msg = s.recv(1024)
    print(msg.decode())

    
