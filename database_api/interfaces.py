import secrets
import string

from database_api.models import engine, Users, Tasks, Solved
from sqlalchemy.orm import sessionmaker

alphabet = string.ascii_letters + string.digits


def generate_password() -> str:
    return ''.join(secrets.choice(alphabet) for _ in range(16))


def init_user(data: dict) -> None:
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        unique_user = session.query(Users).filter_by(telegram_id=data['id']).first()

        oauth_id = generate_password()

        if not unique_user:
            try:

                user = Users(
                    oauth_id=oauth_id,
                    telegram_id=data['id'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    username=data['username']
                )

                session.add(user)
                session.commit()

            except Exception as e:
                session.rollback()
        else:
            pass


def init_questions():
    records = [{
        'value': 1,
        'name_question': 'Language',
        'description': 'На каком языке я пишу?'},
        {
            "value": 2,
            'name_question': 'Programming',
            "description": 'Сколько языков программирования я знаю?'
        }, {
            "value": 4,
            "name_question": 'Project',
            "description": 'Какое название моего лучшего проекта?'
        }, {
            "value": 8,
            "name_question": 'Napitok',
            "description": 'Какой мой любимый напиток?'
        }, {
            "value": 16,
            "name_question": 'Kachestvo',
            "description": 'Какое мое лучшее личное качество?'
        }
        , {
            "value": 32,
            "name_question": 'Kumir',
            "description": 'Какой у меня кумир?'
        }

        , {
            "value": 64,
            "name_question": 'CtF',
            "description": 'Какое направление CTF любимое?'
        }

        , {
            "value": 128,
            "name_question": 'Janr',
            "description": 'Какой любимый жанр музыки?'
        }

        , {
            "value": 256,
            "name_question": 'no homo',
            "description": 'Почему я не люблю PHP?'
        }

    ]

    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        try:
            records = [
                Tasks(value=record["value"], name_question=record["name_question"], description=record["description"])
                for record in records]

            session.add_all(records)
            session.commit()

        except Exception as e:
            session.rollback()


def append_points(telegram_id: int, value: int):
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        try:

            session.query(Users).filter_by(telegram_id=telegram_id).update({
                Users.score: Users.score + value
            })
            session.commit()

        except Exception as e:
            session.rollback()


def update_tasks(task_id: int, value: int):
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        try:
            session.query(Tasks).filter_by(id=task_id).update({
                Tasks.is_solved: Tasks.is_solved + [value]
            }, synchronize_session=False)

            session.commit()

        except Exception as e:
            session.rollback()


def append_solved_user(my_telegram_id: int, executor_id: int):
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        try:
            solved_instance = session.query(Solved).filter_by(customer=my_telegram_id).first()

            if not solved_instance:
                solve = Solved(
                    customer=my_telegram_id,
                    executors=executor_id
                )
            else:
                if executor_id not in solved_instance.executors:
                    solved_instance.executors.append(executor_id)

            session.add(solve)
            session.commit()

        except Exception as e:
            session.rollback()
