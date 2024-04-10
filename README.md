Install ython 3.10 - 3.12
Install Flutter SDK for Windows (or your secific OS)
Install Openai API Key into your Os Envirnmental variables as 'OPENAI_API_KEY'

Navigate to project root folder:
Open command prompt
Type the following:

Pip install -r requirements.txt

python main.py

(takes a second to build db, 2 minutes maybe, on my laptop)

This loads the server, allowing front end to connect and building the database from the files in the 'DOCS' folder


Open another command prompt in the project root folder and type:

fluter run

Should give you options to run in different environments, select 2 for easy testing
