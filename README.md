# EXPENSE TRACKER APP

# Overview


# Description
Expense Tracker is a Flask web application to keep track of all household expenses.  

![](https://github.com/Ataisi/QAProject-ExpenseTracker/blob/main/application/static/images/home.png)


### Main feature of the application:
- Input Expenses.
- View expenses 
- Update expenses
- Delete entry


## Objective
- The objective of this project to develop an application that integrates with a data base and demonstrates CRUD functionality. 
- Utilize containers to host and deploy the application.
- Create a continuous integration(CI/) and continuous deployment(CD) pipeline that will automatically test, build and deploy the application.

## Key Modules Used
This application is developed using Python 3.9.1 and the Database used is SQLite
- Flask - web framework
- Jinja2 - Templating engine
- Continuous Integration: Jenkins
- Continuous Deployment: Docker 
- Version Control: GIT.

A full list of the required installation dependencies is in the requirement.txt file.




# Installation
To run the application on your local machine, you will need to do the following:

`Python 3.7 or above` is required to run the application.

Clone this repository to get the source code
`git clone https://github.com/Ataisi/QAProject-ExpenseTracker`


create a virtual ennvironment
`python3 -m venv venv`

Activate the virtual environment
`python3 -m venv venv`

`Run`
`pip install -r requirements.txt` to install  all the application dependecies

`Run` 
`python app.py`

# Roadmap
- #### Define app requirements, prioritisation and tracking 
Jira is used as the project management tool to prioritize the user stories. MoSCoW prioritization technique was deployed to focus on features with CRUD functionality.

![](https://user-images.githubusercontent.com/82120833/194843902-a29d3748-45d9-40a4-a5ca-d1352383c209.png)


![](https://github.com/Ataisi/QAProject-ExpenseTracker/blob/main/application/static/images/Picture3.png)


- ### Database Design

The application has two tables: Expenses and Categories with a one-to-many relationship

![](https://user-images.githubusercontent.com/82120833/195162334-7a729b5b-5a2c-4ed8-9011-689321fbc26e.jpeg)



- ###  Create the application file structure and initialize a GitHub repository.

- ### Create  app and database implementation

- ### Build CICD pipeline 

- ###  Deployment

- ## Test
Testing was carried out using the Pytest framework
![Sample of testing done](https://user-images.githubusercontent.com/82120833/195158649-2c823df6-e66e-432b-959c-fc5c32f890f8.png)

To run the test:

`(venv) $ python -m pytest -v`

To check the code coverage of the test:

`venv $ python -m pytest --cov-report  term-missing --cov=application`




# Risks Assesment
The following were identified as potential risk factors and  mitigation put in place to minimize risk.
![](https://user-images.githubusercontent.com/82120833/195163988-9b4fc702-d4c1-4318-827f-8046905fb77a.png)






# Future Improvements
- Add search functionality and option to filter by category and date
- Add the functionality to display expenses graphically





