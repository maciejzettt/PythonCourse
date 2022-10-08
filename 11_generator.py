ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen1 = ((a, b) for a in ports for b in ports)
i = 0
for x in gen1:
    i += 1
    print(x, end=' ')
else:
    print('\n', i, "connections in total.")

gen2 = ((a, b) for a in ports for b in ports if a != b)
i = 0
for x in gen2:
    i += 1
    print(x, end=' ')
else:
    print('\n', i, "connections in total.")

gen3 = ((a, b) for a in ports for b in ports if a < b)
i = 0
for x in gen3:
    i += 1
    print(x, end=' ')
else:
    print('\n', i, "connections in total.")