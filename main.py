from email import message
from os import link, name
from tokenize import Name
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud, schemas, database
import uvicorn


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
def read_company(company_id: str, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
       raise HTTPException(status_code=404, detail="Company not found")
    return db_company 


@app.get("/company/", response_model=List[schemas.Company])
def get_companies(db: Session = Depends(get_db)):
    companies = crud.get_companies(db)
    return companies


@app.post("/company/")
def create_company(new_company: schemas.Company, db: Session = Depends(get_db)):  
    db_company = crud.get_company_by_name(db, name=new_company.name)
    if db_company:
       raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_new_company(new_company,db) 



@app.delete("/company/{company_id}")
def delete_company(company_id: str, db: Session = Depends(get_db)):
    db_company = crud.delete_company(company_id, db)
    if db_company is None:
       raise HTTPException(status_code=404, detail="Company not found")
    return db_company 


@app.put("/update_company/{company_id}")
def update_company(company_id: str, updateCompany: schemas.Company, db: Session = Depends(get_db)):
    return crud.update_company(updateCompany,company_id,db)
    

@app.post("/vacancy/")
def create_vacancy(new_vacancy: schemas.Vacancy, db: Session = Depends(get_db)):
    return crud.create_new_vacancy(new_vacancy, db)

@app.get("/vacancy/")
def get_vacancy(db: Session = Depends(get_db)):
    return crud.get_vacancies(db)

@app.get("/vacancy/{vacancy_id}", response_model=schemas.Vacancy)
def read_vacancy(vacancy_id: str, db: Session = Depends(get_db)):
    db_vacancy = crud.get_vacancy(vacancy_id, db)
    if db_vacancy is None:
       raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy 

@app.delete("/vacancy/{vacancy_id}")
def delete_vacancy(vacancy_id: str, db: Session = Depends(get_db)):
    db_vacancy = crud.delete_vacancy(vacancy_id, db)
    if db_vacancy is None:
       raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy 

@app.put("/update_vacancy/{vacancy_id}")
def update_vacancy(vacancy_id: str, updateVacancy: schemas.Vacancy, db: Session = Depends(get_db)):
    return crud.update_vacancy(updateVacancy,vacancy_id,db)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
