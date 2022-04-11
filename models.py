from datetime import datetime
from pydantic import BaseModel

class Vacancy(BaseModel):
    PositionName: str
    CompanyId: str
    Salary : int
    MaxExperience: int
    VacancyId: str
    VacancyLink: str
    MinExperience: int
    Skills: str

class Company(BaseModel):
    Name: str
    Link: str
    City: str
    DateAdded: datetime
    ContactFirstName: str
    ContactLastName: str
    ContactPhoneNumber: str
    ContactEmail: str
    CompanyId: str
    Country: str
    