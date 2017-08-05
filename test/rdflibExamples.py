import rdflib
import socket

g = rdflib.Graph()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get a set of triples from a random store
result = g.parse("http://www.w3.org/People/Berners-Lee/card")
print('graph has {} statements'.format(len(g)))

data = g.serialize(format='n3')

#
server = '192.168.0.67'
port = 5555

s.connect((server, port))
s.sendall(data)

