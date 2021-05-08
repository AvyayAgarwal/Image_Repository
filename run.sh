#!/bin/bash

export FLASK_APP=Image-Repository
export FLASK_ENV=development
flask init-db
flask run
