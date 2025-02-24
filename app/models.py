from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    steps = Column(Integer)
    user = relationship("User")


class Sleep(Base):
    __tablename__ = "sleep"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    duration = Column(Float)
    user = relationship("User")


class BloodTest(Base):
    __tablename__ = "blood_tests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    glucose = Column(Float)
    user = relationship("User")


class HealthScoreWeights(Base):
    __tablename__ = "health_score_weights"
    id = Column(Integer, primary_key=True, index=True)
    steps_weight = Column(Float, default=0.4)
    sleep_weight = Column(Float, default=0.4)
    glucose_weight = Column(Float, default=0.2)
