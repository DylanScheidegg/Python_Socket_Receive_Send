import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def send():
    arr = ['1','2','3']
    lis = ""
    for x in arr:
        lis += x

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(lis, 'utf-8'))
        data = s.recv(1024)

    print('Received', repr(data))

def rec():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                arr = []
                for x in data.decode('utf-8'):
                    # print(x)
                    arr.append(int(x))
                print(arr)
                conn.sendall(data)

while True:
    send()