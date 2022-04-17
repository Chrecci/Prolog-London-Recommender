# Prolog-London-Recommender
Group assignment for Minerva CS152. Based on Prolog and PySWIP, a full stack application to recommend activities to do in a Post-Covid London

## Setup (Windows)

Enter virtual environment:
```
source env/Scripts/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run Server:
```
cd london_recommender
python manage.py runserver --nothreading --noreload
```

You should be able to open application at http://127.0.0.1:8000/