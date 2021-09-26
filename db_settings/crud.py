from sqlalchemy import create_engine
from db_settings import config, models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(config.DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    recreate_database()

    task = models.Task(
        title="Dry leaves cutting",
        description="Cut all dry leaves and clean them",
        farmer_id=1,
    )
    with session_scope() as s:
        s.add(task)
