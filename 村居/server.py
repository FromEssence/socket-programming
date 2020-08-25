import socket
s = socket.socket(2, 1)

s.bind(('', 9001))
s.listen(6)

poem = ['大儿锄豆溪东,\n', '中儿正织鸡笼,\n', '最喜小儿亡赖,\n', '溪头卧剥莲蓬。\n']
while True:
    ns, addr = s.accept()
    print(addr)
    ns.send('四句诗,想看哪句:'.encode())
    for i in range(4):
            
        msg = ns.recv(1024)
        print(msg)
        ns.send(poem[i].encode())
    ns.send("Bye".encode())
    ns.close()
    #ns.sendto("hello".encode(), addr)
      

s.close()

