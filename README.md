
# FastApi Project

FastApi project for a technical test.




## API Reference

#### Get all companies

```http
  GET /company/
```

#### Get a company

```http
  GET /company/${company_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `company_id`  | `string` | **Required**. Id of item to fetch |


#### Create a company

```http
  POST /company/
```

| Parameter | Type     | 
| :-------- | :------- | 
| `name`  | `string` | 
| `link`  | `string` | 
| `city`  | `string` | 
| `date_added`  | `Date` |
| `contact_first_name`  | `string` |
| `contact_last_name`  | `string` |
| `contact_phone_number`  | `string` | 
| `contact_email`  | `string` | 
| `country`  | `string` | 

#### Delete a company

```http
  DELETE /company/${company_id}
```
* Deleted the company and all the vacancy with the company_id

#### Update a company

```http
  PUP /company/${company_id}
```

| Parameter | Type     | 
| :-------- | :------- | 
| `name`  | `string` | 
| `link`  | `string` | 
| `city`  | `string` | 
| `date_added`  | `Date` |
| `contact_first_name`  | `string` |
| `contact_last_name`  | `string` |
| `contact_phone_number`  | `string` | 
| `contact_email`  | `string` | 
| `country`  | `string` | 

#### Get all vacancies

```http
  GET /vacancy/
```

#### Get a vacancy

```http
  GET /vacancy/${vacancy_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vacancy_id`  | `string` | **Required**. Id of item to fetch |


#### Create a vacancy

```http
  POST /vacancy/
```

| Parameter | Type     | 
| :-------- | :------- | 
| `company_id`  | `string` | 
| `position_name`  | `string` | 
| `salary`  | `string` | 
| `salary`  | `integer` |
| `max_experience`  | `integer` | 
| `min_experience`  | `integer` |
| `vacancy_link`  | `string` | 
| `skills`  | `string` | 

* max_experience cannot be less than min_experience


#### Delete a vacancy

```http
  DELETE /vacancy/${vacancy_id}
```

#### Update a vacancy

```http
  PUP /vacancy/${vacancy_id}
```
| Parameter | Type     | 
| :-------- | :------- | 
| `company_id`  | `string` | 
| `position_name`  | `string` | 
| `salary`  | `string` | 
| `salary`  | `integer` |
| `max_experience`  | `integer` | 
| `min_experience`  | `integer` |
| `vacancy_link`  | `string` | 
| `skills`  | `string` | 

