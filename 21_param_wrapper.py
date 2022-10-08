import os


def LogFileOperation_wrapper(action, logfile):
    import datetime

    def wrapper_middle(func):

        def wrapper_inner(fpath):
            fl = open(logfile, 'a')
            ctime = datetime.datetime.today()
            fl.write("Action {0} executed on {1}, time: {2}\n".format(action, fpath, ctime))
            res = func(fpath)
            return res
        return wrapper_inner
    return wrapper_middle


@LogFileOperation_wrapper("FILE CREATE", "g:/py/exdata/21_log_create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+").close()


@LogFileOperation_wrapper("FILE DELETE", "g:/py/exdata/21_log_delete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'g:/py/exdata/dummy_file.txt')
delete_file(r'g:/py/exdata/dummy_file.txt')
create_file(r'g:/py/exdata/dummy_file.txt')
delete_file(r'g:/py/exdata/dummy_file.txt')