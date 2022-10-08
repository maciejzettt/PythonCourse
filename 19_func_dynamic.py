import datetime as dt


def create_datediff_fnc(unit='m'):
    units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    code = """
def f(date1, date2):
    diff = date2 - date1
    diff = diff.total_seconds()
    return diff / {0}
""".format(units[unit])
    exec(code, globals())
    return f


time_span_m = create_datediff_fnc('m')
time_span_h = create_datediff_fnc('h')
time_span_d = create_datediff_fnc('d')


start = dt.datetime(2019, 10, 17, 0, 0, 0)
end = dt.datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
