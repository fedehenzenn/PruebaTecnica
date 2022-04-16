from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

vacancy_test = {
    "VacancyId": 1,
    "CompanyId": 1,
    "PositionName": "Python Dev",
    "Salary": 9999999,
    "MaxExperience": 4,
    "VacancyLink": "xxxx",
    "MinExperience": 1,
    "Skills": "xxxxx"
}

company_test = {
    "Name": "Hunty",
    "Link": "xxxxx",
    "City": "Bogota",
    "DateAdded": "2022-04-14",
    "ContactFirstName": "John"
    ,"ContactLastName": "Appleseed"
    ,"ContactPhoneNumber": "999-999-999"
    ,"ContactEmail": "hola@workijobs.com"
    ,"CompanyId": "094160d6-f80a-4b4b-b1c6-204bc2d7de41",
    "Country": "Colombia"
    }

#Company Tests
def test_create_company():
    response = client.post("/company/", json=company_test)
    assert response.status_code == 200
    assert response.json() == { "message": "Company has been created"}

def test_get_company():
    response = client.get("/company/094160d6-f80a-4b4b-b1c6-204bc2d7de41", json=company_test)
    assert response.status_code == 200
    assert response.json() ==  {
    "company_id": "094160d6-f80a-4b4b-b1c6-204bc2d7de41",
    "name": "Prueba",
    "link": "asd.com",
    "city": "Rafaela",
    "date_added": "2022-02-15",
    "contact_first_name": "Fede",
    "contact_last_name": "ASD",
    "contact_phone_number": "5412595",
    "contact_email": "prueba@asd.com",
    "country": "Argentina"
  }

def test_update_company():
    response = client.put("/update_company/77894bb0-718b-48b7-890f-711411776e58", json={
    "name": "Company fantasy",
    "link": "asd.com",
    "city": "Susana",
    "date_added": "2022-01-01",
    "contact_first_name": "Fede",
    "contact_last_name": "Prueba",
    "contact_phone_number": "5412595",
    "contact_email": "prueba@asd.com",
    "country": "Argentina"
  })
    assert response.status_code == 200
    assert response.json() == {"message": "Company update"} 

def test_delete_company():
    response = client.delete("/company/d76a178b-1978-46bb-a401-9fd5a55844eb", json=company_test)
    assert response.status_code == 200
    assert response.json() == { "message": "Company has been deleted"}

#Vacancy Tests
def test_create_vacancy():
    response = client.post("/vacancy/", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == {"message": "Vacancy created"}

def test_get_vacancy():
    response = client.get("/vacancy/91e526ed-45e0-4891-aeab-720e472376a9", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == {
    "vacancy_id": "91e526ed-45e0-4891-aeab-720e472376a9",
    "salary": 15000,
    "vacancy_link": "asd",
    "skills": "many",
    "max_experience": 5,
    "position_name": "dev",
    "min_experience": 2,
    "company_id": "af1b859b-2e0a-40d4-b220-05a9ffaa1b77"
  }

def test_update_vacancy():
    response = client.put("/update_vacancy/90913b79-814e-4299-99af-8b5db54825e5", json={
    "vacancy_id": "90913b79-814e-4299-99af-8b5db54825e5",
    "salary": 20000,
    "vacancy_link": "prueba",
    "skills": "many",
    "max_experience": 5,
    "position_name": "dev",
    "min_experience": 2,
    "company_id": "af1b859b-2e0a-40d4-b220-05a9ffaa1b77"
  })
    assert response.status_code == 200
    assert response.json() == {"message": "Vacancy update"}

def test_delete_vacancy():
    response = client.delete("/vacancy/af1b859b-2e0a-40d4-b220-05a9ffaa1b77", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == { "message": "Vacancy has been deleted"}