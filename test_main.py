from fastapi import testclient
from .main import app

client = testclient(app)

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
        "DateAdded": 20201-12-1,
        "ContactFirstName": "John",
        "ContactLastName": "Appleseed",
        "ContactPhoneNumber": "999-999-999",
        "ContactEmail": "hola@workijobs.com",
        "CompanyId": 1,
        "Country": "Colombia",
}

#Company Tests
def test_create_company():
    response = client.post("/company/", json=company_test)
    assert response.status_code == 200
    assert response.json() == company_test

def test_get_company():
    response = client.post("/company/1", json=company_test)
    assert response.status_code == 200
    assert response.json() == company_test

def test_update_company():
    response = client.put("/company/1", json={
        "Name": "Prueba",
        "Link": "prueba",
        "City": "Buenos Aires",
        "DateAdded": 20211-12-1,
        "ContactFirstName": "Jose",
        "ContactLastName": "Perez",
        "ContactPhoneNumber": "+54454545",
        "ContactEmail": "prueba@workijobs.com",
        "CompanyId": 1,
        "Country": "Argentina",
    })
    assert response.status_code == 200
    assert response.json() == {
        "Name": "Prueba",
        "Link": "prueba",
        "City": "Buenos Aires",
        "DateAdded": 20211-12-1,
        "ContactFirstName": "Jose",
        "ContactLastName": "Perez",
        "ContactPhoneNumber": "+54454545",
        "ContactEmail": "prueba@workijobs.com",
        "CompanyId": 1,
        "Country": "Argentina",
    }

def test_delete_company():
    response = client.post("/company/1", json=company_test)
    assert response.status_code == 200
    assert response.json() == { "message": "Company has been deleted"}

#Vacancy Tests
def test_create_vacancy():
    response = client.post("/vacancy/", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == vacancy_test

def test_get_vacancy():
    response = client.post("/vacancy/1", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == vacancy_test

def test_update_vacancy():
    response = client.put("/vacancy/1", json={
        "VacancyId": 1,
        "CompanyId": 1,
        "PositionName": "C# Dev",
        "Salary": 9999999,
        "MaxExperience": 3,
        "VacancyLink": "Prueba",
        "MinExperience": 2,
        "Skills": "Prueba"
})
    assert response.status_code == 200
    assert response.json() == {
        "VacancyId": 1,
        "CompanyId": 1,
        "PositionName": "C# Dev",
        "Salary": 9999999,
        "MaxExperience": 3,
        "VacancyLink": "Prueba",
        "MinExperience": 2,
        "Skills": "Prueba"
}

def test_delete_vacancy():
    response = client.post("/vacancy/1", json=vacancy_test)
    assert response.status_code == 200
    assert response.json() == { "message": "Vacancy has been deleted"}