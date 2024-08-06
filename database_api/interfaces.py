from database_api.models import Users, engine
from sqlalchemy.orm import sessionmaker


def init_user(oauth_id, username):
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        try:
            user = Users(
                username=username,
                oauth_id=oauth_id
            )

            session.add(user)
            session.commit()

        except Exception as e:
            session.rollback()


def append_points():
    pass


def update_tasks():
    pass
