from database_api.models import engine, Users, Quests, Profiles
from sqlalchemy.orm import sessionmaker

from loguru import logger


def init_user(data: dict) -> None:
    # data = kwargs
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        unique_user = session.query(Users).filter_by(telegram_id=data['id']).first()

        oauth_id = 1200
        secret_code = 9994999

        # if not unique_user:
        try:

            # TODO! заполнить все поля таблицы + генерация

            user = Users(
                oauth_id=oauth_id,
                telegram_id=data['id'],
                secret_code=secret_code,
            )
            profile = Profiles(
                telegram_id=data['id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username']
            )

            session.add_all([user, profile])
            session.commit()

        except Exception as e:
            session.rollback()
        # else:
        #     pass


def init_questions():
    # TODO! заполнить все вопросы

    records = [{
        'value': 1,
        'name_question': 'First_task',
        'description': 'example text'},
        {
            "value": 2,
            'name_question': 'Second_task',
            "description": 'example text'
        }, {
            "value": 4,
            "name_question": 'Third_task',
            "description": 'example text'
        }, {
            "value": 8,
            "name_question": 'Fourth_task',
            "description": 'example text'
        }, {
            "value": 16,
            "name_question": 'Fifth_task',
            "description": 'example text'
        }]

    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        try:
            records = [
                Quests(value=record["value"], name_question=record["name_question"], description=record["description"])
                for record in records]

            session.add_all(records)
            session.commit()

        except Exception as e:
            session.rollback()


def append_points():
    pass


def update_tasks():
    pass
