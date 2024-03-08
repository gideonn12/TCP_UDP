import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip='127.0.0.1'
dest_port=12345     
s.connect((dest_ip, dest_port))

msg = 'hello, server'
while not msg == 'quit':
    s.send(msg.encode('utf-8'))
    data =s.recv(4096).decode('utf-8')
    print('Server sent: ', data)
    msg = 'hello, server'

s.close()
