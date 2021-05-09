# Image_Repository

## Instructions to run

After cloning the repository, navigate into it and following these steps:

1. Create and activate your python virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

2. Setup and install dependencies

```bash
pip install -e .
```

3. Run tests/coverage as desired

```bash
# to just run tests
pytest

# to run coverage
coverage run -m pytest

# to get coverage report
coverage report
```

4. Run the application

```bash
export FLASK_APP=Image_Repository
export FLASK_ENV=development
flask init-db
flask run
```

After running the above commands and confirming the development server is up, go to this [link](http://localhost:5000) 
