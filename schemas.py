from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Vacancy(BaseModel):
    VacancyId: int
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
    CompanyId: int
    Name: str
    Link: str
    City: str
    DateAdded: datetime
    ContactFirstName: str
    ContactLastName: str
    ContactPhoneNumber: str
    ContactEmail: str
    Country: str
    
    class Config:
        orm_mode = True