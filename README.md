# 324-gamehub
Database (ICS324@KFUPM) project: Social network - Player and game directory

We hope the experience stored here is beneficial, but this repository is not to be referenced for best coding or Django practices.

###Description of directory:
- GameHub - Main project folder (includes all HTML templates)
- gametest - Project folder for Game entities
- groups - Project folder for Groups and Blogposts
- userpage - Project folder for User entity
- ddlite.sql - SQL CREATE statements
- dml.sql - SQL INSERT statements
- db.sqlite3 - SQLite3 DB files (CREATE and INSERT statements were applied to it. Includes some Django tables)
- requirements.txt - Requirements needed to run the website
- Other files and folders are not worth mentioning

###How to run it?
- ~~Method 1: Use our PythonAnywhere hosted instance~~
- Method 2: Install and run locally as described below

###Installation:
1. Install Python (preferably 2.7): https://www.python.org/downloads/
2. Install the requirements:
  1. navigate to the folder containing GameHub, gametest, ..
  2. run `pip install -r requirements.txt`
3. Run the server:
  1. navigate to the folder containing GameHub, gametest, ..
  2. run `python manage.py runserver`
4. The website will be at 127.0.0.1:8000

###Creating the sqlite3 database:
db.sqlite3 is a database that can already be used. If you want to create your own:

1. Run sqlite3 to see if you have sqlite3 installed. If you don't, install it:
  1. download sqlite-tools from https://www.sqlite.org/
  2. the file sqlite3.exe is the program we need
2. Navigate to the folder containing GameHub, gametest, ..
3. Delete db.sqlite3
4. Run `sqlite3 db.sqlite3`
5. Run `.read ddlite.sql`
6. Run `.read dml.sql`
7. Run `.quit`
8. Run `python manage.py migrate`
