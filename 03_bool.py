def DisplayOptions(options):
    print("Select option:")
    i = 1
    for element in options:
        print("%d - %s" % (i, element))
        i += 1
    response = input("Your choice: ")
    return response


options = ["Load data", "Export data", "Analyze & predict"]
choice = 'x'
while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
            if 3 >= choice_num > 0:
                print("You have chosen %d: %s" % (choice_num, options[choice_num]))
            else:
                print("Value out of range")
                # choice = ''
        except ValueError:
            print("Give an number")
            # choice = ''
    else:
        print("Program terminated")