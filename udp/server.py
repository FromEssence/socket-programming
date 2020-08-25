import socket
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(("10.170.16.144", 9001))

cnt = 0
while True:
    # 接收数据:
    print("waiting...")
    
    data, addr = server.recvfrom(1024*1000)
    print('Received from %s:%s.' % addr, data.decode())
    print(cnt)
    cnt += 1


