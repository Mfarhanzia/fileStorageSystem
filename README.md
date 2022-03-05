# fileStorageSystem

To get started with the project follow the following steps

- `git clone git@github.com:Mfarhanzia/fileStorageSystem.git`.
- `cd` into the project e.g:`cd fileStorageSystem`
- Open `spekit_assignment/settings.py` and change the DataBase credentials to your Database.
- Create virtualenv using `virtualenv -p python3 venv`
- Activate virtualenv using `source venv/bin/activate`(linux/mac os).
- install the requirements by staying in the project base directory using cmd `pip install -r requirements.tx`
- run migrations `python manage.py migrate`.
- and start server by using cmd `python manage.py runserver` now goto `http://localhost:8000`

**Project Usage:**
Using the front-end UI
1. First Add folder.
2. then Add Topics.
3. Upload document: by selecting folder and related topics(you can select multiple topics) and add file(not more than 10MB).
4. on the second row user can access the documents of any folder by clicking on the folder name and can also set filter on **Topics** to get the topic specific documents.
