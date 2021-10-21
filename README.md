1. create virtual env (PyCharm does it automatically):
```
python -m venv venv
```

2. activate virtual env (PyCharm does it automatically):
```
source venv/bin/activate
```

3. install dependencies (PyCharm does it automatically):
```
pip install -r requirements.txt
```
   
4. add a dependency, e.g.:
```
pip install boto3
```

5. run a script, e.g.:
```
python classes.py
```

6. add manually dependencies to requirements.txt (recommended, no need to specify transitive dependencies) or
   grab installed dependencies (it will include transitive dependencies as well):
```
pip freeze > requirements.txt
```