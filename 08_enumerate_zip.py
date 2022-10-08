projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, name in zip(projects, leaders):
    print("The leader of %s project is %s" % (project, name))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, date, name in zip(projects, dates, leaders):
    print("The leader of project %s started %s is %s" % (project, date, name))

for i, (project, date, name) in enumerate(zip(projects, dates, leaders), 1):
    print("%d - The leader of project %s started %s is %s" % (i, project, date, name))