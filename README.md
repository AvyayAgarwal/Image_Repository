# Image_Repository

This project is a general image repository that allows one to `upload`, `delete` and `view` images. It supports functionality for uploading images `publicly` for anyone to view without logging in as well as keeping images `private` for secure viewing based on user accounts.

## Setup

Create and activate your python virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

Setup and install dependencies

```bash
pip install -e .
```

## Testing

```bash
# to just run tests
pytest

# to run coverage
coverage run -m pytest

# to get coverage report
coverage report
```

## Running

```bash
export FLASK_APP=Image_Repository
export FLASK_ENV=development
flask init-db
flask run
```

After running the above commands and confirming the development server is up, go to this [link](http://localhost:5000) 


## Planned improvements

In its current state, the application is not at a stage for proper usage and scaled deployment. Some of the improvements to current issues are as follows:

* Currently using sqlite3 as a database which is not suitable as amount of data increases. Migrate to a more robust database
* Images are currently stored and accessible within the static directory causing a scalability and security issue as well. Ideally, images would be stored in solutions like AWS S3 or other cloud counterparts
* User account flows and authentication is not robust and secure and can use proper auth technologies and practices 
* Front End UI design is currently very rudimentary and needs to improvement