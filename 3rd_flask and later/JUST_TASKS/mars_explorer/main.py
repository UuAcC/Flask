import db_session
from jobs import Jobs


def main():
    db_session.global_init("mars_explorer.db")
    job = Jobs()
    job.team_leader = input()
    job.job = input()
    job.work_size = input()
    job.collaborators = input()
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
