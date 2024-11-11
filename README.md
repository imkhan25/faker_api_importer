# Faker API importer

A simple Python application to fetch user data from faker API.

## Features

- Fetch user data
- Anonymize the data using the following guidelines:
- We are only interested in data about user location, age, and email providers
- User-identifiable information may be masked(use **** to express that the data
is masked)
- Data generalization, where individual values of attributes are replaced with a
broader category:
■ Birthdate: substitute the value by a ten year age group(i.e someone
with a birthdate 12-4-1991 must be substituted by [30-40])
■ Email: we must remove the first part of the email and just keep the
domain.
● Insert the data into SQL Lite

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
   git clone https://github.com/imkhan25/faker_api_importer.git
   
2.Install dependencies:

pip install -r requirements.txt

Usage
Run the application:

python main.py


## Important notes:

Source code of the application is in src folder.

## There are two stand alone files in src folder as below:
-> query.sql : this contains the sql query for the questions asked for the assignnment. 

-> report_UI.png : Its a simple bar chart generated with the data generated. 
