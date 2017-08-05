import rdflib

g = rdflib.Graph()
result = g.parse("http://www.w3.org/People/Berners-Lee/card")

print('graph has {} statements'.format(len(g)))

s = g.serialize(format='n3')
uncode = s.decode()
print(uncode)
# print( g.serialize(format='n3'))

