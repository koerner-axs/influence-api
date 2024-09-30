from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from influencepy.persistence.cutoff.cutoff import IndexingCutoff
from influencepy.persistence.orm_base import Base


def connect(db_host: str = 'localhost', db_port: int = 5434, db_name: str = 'infpydb', db_user: str = 'influencepy',
            db_password: str = 'influencepy'):
    DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(DATABASE_URL)
    InfPyDbSession = sessionmaker(bind=engine)
    session = InfPyDbSession()
    return engine, session


if __name__ == '__main__':
    engine, session = connect()
    Base.metadata.create_all(engine)
    print(session.query(IndexingCutoff).all())
    session.close()
