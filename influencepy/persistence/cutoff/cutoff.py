from sqlalchemy import Column, String, Integer, TIMESTAMP, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from influencepy.persistence.orm_base import Base


class IndexingCutoff(Base):
    __tablename__ = 'cutoffs'

    type = Column(String, primary_key=True)
    last_block = Column(Integer, nullable=False)
    last_update = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())


def update_cutoff(session: Session, cutoff_type, last_block):
    try:
        cutoff = session.query(IndexingCutoff).get(cutoff_type)
        if cutoff is None:
            cutoff = IndexingCutoff(type=cutoff_type, last_block=last_block)
            session.add(cutoff)
        else:
            cutoff.last_block = last_block
        session.commit()
    except IntegrityError:
        session.rollback()
