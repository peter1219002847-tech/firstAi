from sqlalchemy import Column, Integer, String,ForeignKey,Date
from sqlalchemy.orm import relationship
from .base import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    location = Column(String(100))

    employees = relationship(
        'Employee',
        back_populates='department',
        lazy="selectin"
    )

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    hire_date = Column(Date)

    department_id = Column(
        Integer,
        ForeignKey('departments.id', ondelete="RESTRICT"),
        nullable=False
    )

    department = relationship(
        "Department",
        back_populates="employees",
        lazy="joined"
    )