from distutils.errors import LinkError
from os import link
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models, schemas
from uuid import uuid4
from fastapi import HTTPException

def CreateDatabase():
    return Base.metadata.create_all(bind=engine)



def get_vacancy(db: Session, vacancy_id: str):
    return db.query(models.Vacancy).filter(models.Vacancy.vacancy_id == vacancy_id).first()



def create_new_vacancy(vacancy:schemas.Vacancy,db:Session):
    db_vacancy = models.Vacancy(**vacancy.dict())
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy

def get_company(db: Session, company_id: str):
    company = db.query(models.Company).filter(company_id == company_id).first()
    return company

def get_companies(db: Session):
    companies = db.query(models.Company).offset(0).limit(100).all()
    return companies

def get_company_by_name(db: Session, name: str):
    return db.query(models.Company).filter(models.Company.name == name).first()

def create_new_company(company:schemas.Company,db:Session):
    db_company = models.Company(
        name = company.name
        ,link = company.link
        ,city = company.city 
        ,date_added = company.date_added
        ,contact_first_name = company.contact_first_name
        ,contact_last_name = company.contact_last_name
        ,contact_phone_number = company.contact_phone_number
        ,contact_email = company.contact_email
        ,country = company.country 
    )
    db_company.company_id=str(uuid4())
    print (db_company.__dict__)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return {"message": "Company created"}

def update_company(company:schemas.Company, company_id: str, db: Session):
    db_company = db.query(models.Company).filter(models.Company.company_id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    db_company.name = company.name
    db_company.link = company.link
    db_company.city = company.city
    db_company.contact_first_name = company.contact_first_name
    db_company.contact_last_name = company.contact_last_name
    db_company.contact_phone_number = company.contact_phone_number
    db_company.date_added = company.date_added
    db_company.contact_email = company.contact_email
    db_company.country = company.country
    
    db.commit()
    return {"message": "Company update"}  

def delete_company(company_id: str, db: Session):
    company = db.query(models.Company).filter(models.Company.company_id == company_id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    vacancies = db.query(models.Vacancy).filter(models.Vacancy.company_id == company_id)
    for vacancy in vacancies:
        db.delete(vacancy)
    
    db.delete(company)
    db.commit()
    return {"message": "Company deleted"}


def create_new_vacancy(vacancy:schemas.Vacancy,db:Session):
    db_vacancy = models.Vacancy(
        position_name = vacancy.position_name
        ,salary =vacancy.salary
        ,max_experience =vacancy.max_experience 
        ,vacancy_link =vacancy.vacancy_link
        ,min_experience =vacancy.min_experience
        ,skills =vacancy.skills
    )
    db_vacancy.vacancy_id=str(uuid4())
    company = db.query(models.Company).filter(models.Company.company_id == vacancy.company_id).first()
    if not company:    
        raise HTTPException(status_code=400, detail="The company doesn't exist")
    if db_vacancy.max_experience < db_vacancy.min_experience:
        raise HTTPException(status_code=400, detail="The max experience cannot be less than min_experience")
    
    db_vacancy.company_id= vacancy.company_id
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return {"message": "Vacancy created"}

def get_vacancy(vacancy_id: str, db: Session):
    vacancy = db.query(models.Vacancy).filter(models.Vacancy.vacancy_id == vacancy_id).first()
    return vacancy

def get_vacancies(db: Session):
    vacancies = db.query(models.Vacancy).offset(0).limit(100).all()
    return vacancies

def update_vacancy(vacancy:schemas.Vacancy, vacancy_id: str, db: Session):
    db_vacancy = db.query(models.v).filter(models.Vacancy.vacancy_id == vacancy_id).first()
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    db_vacancy.vacancy_id = vacancy.vacancy_id
    db_vacancy.position_name = vacancy.position_name
    db_vacancy.salary = vacancy.salary
    db_vacancy.max_experience = vacancy.max_experience
    db_vacancy.vacancy_link = vacancy.vacancy_link
    db_vacancy.min_experience = vacancy.min_experience
    db_vacancy.company_id = vacancy.company_id

    db.commit()
    return {"message": "Vacancy update"}  

def delete_vacancy(vacancy_id: str, db: Session):
    vacancy = db.query(models.Vacancy).filter(models.Vacancy.vacancy_id == vacancy_id).first()
    if vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    db.delete(vacancy)
    db.commit()
    return {"message": "Vacancy deleted"}