from email import message
from os import link, name
from tokenize import Name
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database


app = FastAPI()

companies = []
vancancies = []
id_c = 0

crud.CreateDatabase()

def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/company/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    #db_company = crud.get_company(db, company_id=company_id)
    #if db_company is None:
    #    raise HTTPException(status_code=404, detail="Company not found")
    #return db_company 
    for company in companies:
        if company_id == company.CompanyId:
            return company
    raise HTTPException(status_code=404, detail="Company not found") 


@app.get("/companies/")
def get_companies():
    return companies

@app.post("/company/", response_model=schemas.Company)
def create_company(new_company: schemas.Company, db: Session = Depends(get_db)):
    #db_company = crud.get_company_by_name(db, name=company.Name)
    #if db_company:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    #return crud.create_new_company(company,db)
    for company in companies:
        if new_company.Name == company.Name:
            raise HTTPException(status_code=400, detail="Name already registered")
    companies.append(new_company)
    return new_company

@app.get("/company/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    #db_company = crud.get_company(db, company_id=company_id)
    #if db_company is None:
    #    raise HTTPException(status_code=404, detail="Company not found")
    #return db_company 
    for company in companies:
        if company_id == company.CompanyId:
            return company
    raise HTTPException(status_code=404, detail="Company not found") 

@app.delete("/company/{company_id}")
def delete_company(company_id: int):
    for index,company in enumerate(companies):
        if company.CompanyId == company_id:
            companies.pop(index)
            return {message: "Company has been deleted"}
    raise HTTPException(status_code=404, detail="Company not found")

@app.put("/update_company/{company_id}")
def update_company(company_id: int, updateCompany: schemas.Company):
    for index,company_T in enumerate(companies):
        if company_T.CompanyId == company_id:   
            companies[index].Name = updateCompany.Name
            companies[index].Link = updateCompany.Link
            companies[index].City = updateCompany.City
            companies[index].ContactFirstName = updateCompany.ContactFirstName
            companies[index].ContactLastName = updateCompany.ContactLastName
            companies[index].ContactPhoneNumber = updateCompany.ContactPhoneNumber
            companies[index].DateAdded = updateCompany.DateAdded
            companies[index].ContactEmail = updateCompany.ContactEmail
            companies[index].Country = updateCompany.Country
            return companies[index]
    raise HTTPException(status_code=404, detail="Company not found")

@app.get("/vacancy_in_company/{company_id}")
def vacancy_in_company(company_id: int):
    vacancies_in_company = []
    for vacancy_t in vancancies:
        if vacancy_t.CompanyId == company_id:
            vacancies_in_company.append(vacancy_t)
    if not vacancies_in_company:
        raise HTTPException(status_code=400, detail="The company has no vacancies")
    return vacancies_in_company

@app.post("/vacancy/", response_model=schemas.Vacancy)
def create_vacancy(new_vacancy: schemas.Vacancy, db: Session = Depends(get_db)):
    vancancies.append(new_vacancy)
    return new_vacancy

@app.get("/vacancy/")
def get_vacancy():
    return vancancies

@app.delete("/vacancy/{vacancy_id}")
def delete_company(vacancy_id: int):
    for index,vacancy in enumerate(vancancies):
        if vacancy.VacancyId == vacancy_id:
            vancancies.pop(index)
            return {message: "Vacancy has been deleted"}
    raise HTTPException(status_code=404, detail="Vacancy not found")

@app.put("/update_vacancy/{vacancy_id}")
def update_vacancy(vacancy_id: int, updateVacancy: schemas.Vacancy):
    for index,vacancy in enumerate(vancancies):
        if vacancy.VacancyId == vacancy_id:   
            vancancies[index].CompanyId = updateVacancy.Name
            vancancies[index].PositionName = updateVacancy.Link
            vancancies[index].Salary = updateVacancy.City
            vancancies[index].MaxExperience = updateVacancy.ContactFirstName
            vancancies[index].VacancyLink = updateVacancy.ContactLastName
            vancancies[index].MinExperience = updateVacancy.ContactPhoneNumber
            vancancies[index].Skills = updateVacancy.ContactEmail
            return {"message": "Vacancy has been updated"}
    raise HTTPException(status_code=404, detail="Vacancy not found")