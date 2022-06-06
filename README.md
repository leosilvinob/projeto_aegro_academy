# Project Aegro Academy

Project with the purpose of creating a data pipeline that acquires data from Twitter's open API and writes it to a database.

## Description

The pipeline acquires data from Twitter's open API, via a given hashtag, search date and number of tweets.

The database to be used is PostgreSQL, a relational database. The data modeling follows below:
![Modelagem_dados](https://user-images.githubusercontent.com/78217387/172247521-1174e345-4ce9-4f20-b07a-643456f576c0.png)

After the data (tweets) are acquired through the Twitter API, they are processed, sent to the database and finally three searches for information are performed:

*The five users with the most followers (Among those who returned).

*The total number of tweets per tag (Based on the chosen Tag and only the language in Portuguese).
*Total posts grouped by day.

At the end of the searches, they are archived separately in csv files.

Each step is performed through Apache Airflow, following the diagram below:
![image](https://user-images.githubusercontent.com/78217387/172247885-3e68ece4-c0d6-44aa-866a-51599a2ea351.png)

All these steps are performed daily, once a day, that is, the schedule in airflow is set to daily.

## Getting Started

### Dependencies

* Linux/MacOS/Windows(via WSL2 or via Linux Containers).
* Python >= 3
* Apache Airflow 2.1
* PostgreSQL 12.0 >=
* Other dependencies such as specific libraries is on the file "requirements.txt"

### Installing

* Unzip the file.
* Put the "airflow" folder inside the directory where your "dags" folder of your airflow is.
* Create a postgreSQL database for the project.
* Create or edit(if it already exists) an airflow connection with the name "postgres_default" connecting to the database you created previously for the project.
* Create four variables in Airflow with your API Twitter credentials: "access_key","access_secret","consumer_key" and "consumer_secret".

### Executing program

* Run the airflow webserver by your terminal: airflow webserver
* Run the airflow schedulerby your terminal: airflow scheduler
* Acess the airflow webserver, open your browser and acess(by default, it changes depending on how it was installed):http://localhost:8080/
* Go to "main_project".
* Start the dag.

## Authors

Contributors names and contact info:

*Author Name: Leonardo Silvino 
*Author Linkedin: https://www.linkedin.com/in/leonardo-silvino/
