name_for_userid = {
382: 'Alice',
950: 'Bob',
590: 'Dilbert',
}
def greeting(userid):
    return 'Hi %s!' % name_for_userid[userid]
print(greeting(382))

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'

"""
The official Python documentation specifically recommends an “easier to ask for forgiveness than permission” (EAFP)
"""