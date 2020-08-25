# UDP    
# 用到的时间函数需python 3.7及以上
# windows默认套接字缓冲区为8KB，最好在注册表修改下

import socket
import time
def get_send_msg(filepath:str)->str:

    '''
    输入文件路径，按行读取文件后拼接成一个字符串返回。
    注意：该程序会将windows的换行回车\r\n读取成\n，因此读取到的字节数小于文件实际字节数。
    '''
    send_msg = ""
    #cnt = 0
    with open(filepath, 'rt') as f:
        for line in f:
            #cnt += 1
            send_msg += line
    # print(send_msg)
    # print(cnt)
    return send_msg

def udp_send_to_cloud(filepath:str):
    
    client = socket.socket(type=socket.SOCK_DGRAM)

    # set buf size
    bufsize = client.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("buf before:", bufsize)
    client.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 1024*500)
    bufsize = client.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("buf after:", bufsize)
    
    send_data = get_send_msg(filepath)
    start_time = time.perf_counter_ns()
    print(type(start_time))

    c = client.sendto(send_data.encode(), ("10.170.16.145", 9001))

    end_time = time.perf_counter_ns()
    print("成功发送%d字节数据至云服务器~"%len(send_data))
    print("发送时间：%f"%(end_time-start_time))
    client.close()

    return

if __name__ == "__main__":
    filepath = "./queries.txt"
    udp_send_to_cloud(filepath)

