projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

proj_lead = zip(projects, leaders)

for p, l in proj_lead: # zip(projects, leaders):
    print("The leader of ", p, " is ", l, ".")
    #print('The leader of "{}" is {}'.format(p,l))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, l, d in zip(projects, leaders, dates):
    print('The leader of "{}" started "{}" is "{}".'.format(p,l,d))

for i, (p, l, d) in enumerate(zip(projects, leaders, dates)):
    #print(i, 'The leader of "{}" started {} is {}'.format(p, l, d))
    print('{} - The leader of "{}" started {} is {}'.format(i+1, p, l, d))
