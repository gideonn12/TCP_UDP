import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip=''
server_port=12345
server.bind((server_ip, server_port))
server.listen(5)

while True:
    client_socket, client_address = server.accept()
    print('Connection from: ', client_address)
    data = client_socket.recv(1024).decode('utf-8')
    while not data == '':
        print('Received: ', data)
        client_socket.send(data.upper().encode('utf-8'))
        data = client_socket.recv(1024)
    
    print('Client disconnected')
    client_socket.close()