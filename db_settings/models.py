from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    farmer_id = Column(Integer, ForeignKey("farmer.id"))

    def __repr__(self):
        return "<Task(title='{}', description='{}', farmer_id={}, )>".format(
            self.title, self.description, self.farmer_id
        )


class Farmer(Base):
    __tablename__ = "farmer"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    tasks = relationship("task")

    def __repr__(self):
        return "<Farmer(name='{}', phone_number='{}', tasks={}, )>".format(
            self.name, self.phone_number, self.tasks
        )
