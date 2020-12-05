import socket

HOST = 'Localhost'
PORT = 10000

def week02_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}, {conn}')
        file = open('filebook', 'wb')

        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
            file.close()
        conn.close()

if __name__ == "__main__":
    week02_server()