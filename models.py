from sqlite3 import Date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Vacancy(Base):
    __tablename__ = "vacancies"

    vacancy_id = Column(String, primary_key=True, index=True)
    position_name = Column(String)  
    salary = Column(Integer)
    max_experience = Column(Integer)
    vacancy_link = Column(String)
    min_experience = Column(Integer)
    skills = Column(String)
    company_id = Column(String)

class Company(Base):
    __tablename__ = "companies"
    
    company_id = Column(String, primary_key=True, index=True)
    name = Column(Integer, primary_key=True,)
    link = Column(Integer)
    city = Column(Integer)
    date_added = Column(DateTime) 
    contact_first_name = Column(Integer)
    contact_last_name = Column(Integer)
    contact_phone_number = Column(Integer)
    contact_email = Column(Integer)
    country = Column(Integer)

    

