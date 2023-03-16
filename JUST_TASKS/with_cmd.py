import sys

name = sys.stdin
global_init(name)
db_sess = create_session()
users = db_sess.query(Users)
for user in users:
    print(user)
