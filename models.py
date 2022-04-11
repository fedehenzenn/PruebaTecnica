from sqlite3 import Date
from xmlrpc.client import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Vacancy(Base):
    __tablename__ = "vacancies"

    vacancy_id = Column(Integer, primary_key=True, index=True)
    position_name = Column(String)  
    salary = Column(Integer)
    max_experience = Column(Integer)
    vacancy_link = Column(String)
    min_experience = Column(Integer)
    skills = Column(String)
    company_id = Column(Integer, ForeignKey('companies.company_id'))

class Company(Base):
    __tablename__ = "companies"
    
    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)
    link = Column(Integer)
    city = Column(Integer)
    date_added = Column(DateTime) 
    contact_first_name = Column(Integer)
    contact_last_name = Column(Integer)
    contact_phone_number = Column(Integer)
    contact_email = Column(Integer)
    country = Column(Integer)
    vacancies = relationship("Vacancy")
    

