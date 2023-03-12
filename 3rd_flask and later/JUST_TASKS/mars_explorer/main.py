import db_session
from users import User


def main():
    db_session.global_init("mars_explorer.db")
    user = User()
    user.surname = input()
    user.name = input()
    user.age = input()
    user.position = input()
    user.speciality = input()
    user.address = input()
    user.email = input()
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
