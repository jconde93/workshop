import socket
import sys
import rdflib

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

g = rdflib.Graph()


try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(1)
print('Waiting for connection')

conn, addr = s.accept()
print('Connected with {}:{}'.format(addr[0], str(addr[1])))

store = []
result = conn.recv(4096)
while (len(result) > 0):
    store.append(result.decode('utf-8'))
    result = conn.recv(4096)


if len(result) <= 0:
    conn.close()

print('Printing Store:')

for t in store:
    print(t)
