def calculate_paint(efficiency, *areas):
    ret = sum(areas) * efficiency
    print("Calculated paint: {0:7.2f} litres.".format(ret))


def log_it(file, *args, **kwargs):
    try:
        with open(file, mode='a') as log_fl:
            for arg in args:
                log_fl.write(arg+'\n')
            for kw in kwargs:
                log_fl.write('\t' + kw + ' :: ' + kwargs[kw] + '\n')
            log_fl.write('\n')
    except FileNotFoundError:
        print("File not found.")


calculate_paint(2.3, 4, 2.1, 18, 5.5)
list_of_areas = [4, 2.1, 18, 5.5]
calculate_paint(2.3, *list_of_areas)

log_it(r"G:/py/exdata/logit.txt", "This is the beginning of the log", "A second parameter", errno='0x437')