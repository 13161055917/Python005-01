import socket

HOST = 'localhost'
PORT = 10000

def week02_client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 接收文件并发送服务端
        data = input('开始发送')
        if data == 'exit':
            break
        with open(data, 'rb') as f:
            s.sendfile(f)

        data2 = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('GBK'))

    s.close()

if __name__ == "__main__":
    week02_client()