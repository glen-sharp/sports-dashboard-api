from sqlalchemy import (
    Column,
    String,
    Integer,
)

from database import Base

class F1DriverStandings(Base):
    __tablename__ = 'f1_driver_standings'

    id = Column(Integer, primary_key=True)
    ranking = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    points = Column(Integer, nullable=False)

class SnookerRankings(Base):
    __tablename__ = 'snooker_rankings'

    id = Column(Integer, primary_key=True)
    ranking = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    nationality = Column(String(100), nullable=False)
    points = Column(Integer, nullable=False)
