import socket
s = socket.socket(2, 1)
s.bind(('', 9001))
s.listen(6)

ns, addr = s.accept()
print("连接来自：",addr)
while True:
  msg = ns.recv(1024)
  print("客户端消息: ", msg)
  ns.send("nice".encode())
