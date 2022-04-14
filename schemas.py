from datetime import datetime
from sqlite3 import Date
from pydantic import BaseModel
from typing import Optional

class Vacancy(BaseModel):
    VacancyId: Optional[int]
    CompanyId: int
    PositionName: str
    Salary : int
    MaxExperience: int
    VacancyLink: str
    MinExperience: int
    Skills: str

    class Config:
        orm_mode = True




class Company(BaseModel):
    CompanyId: Optional[int]
    Name: str
    Link: str
    City: str
    DateAdded: Date
    ContactFirstName: str
    ContactLastName: str
    ContactPhoneNumber: str
    ContactEmail: str
    Country: str
    
    class Config:
        orm_mode = True