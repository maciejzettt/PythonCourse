ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
connections = [(o, d) for o in ports for d in ports if o != d]
for (a, b) in connections:
    if (b, a) in connections:
        connections.remove((b, a))
print(connections)
print(len(connections))

