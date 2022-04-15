from datetime import datetime
from sqlite3 import Date
from pydantic import BaseModel
from typing import Optional

class Vacancy(BaseModel):
    vacancy_id: Optional[str]
    company_id: str
    position_name: str
    salary : int
    max_experience: int
    vacancy_link: str
    min_experience: int
    skills: str

    class Config:
        orm_mode = True




class Company(BaseModel):
    company_id: Optional[str]
    name: str
    link: str
    city: str
    date_added: Date
    contact_first_name: str
    contact_last_name: str
    contact_phone_number: str
    contact_email: str
    country: str
    
    class Config:
        orm_mode = True
    