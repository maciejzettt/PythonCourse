days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
print(days, workdays)
workdays.remove('sat')
workdays.remove('sun')
print(days, workdays)
