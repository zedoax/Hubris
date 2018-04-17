import os
import secrets

# Project
PROJECT_NAME = "Hubris"


# SQL Alchemy
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

# Database

# Application Secret Key
SECRET_KEY = secrets.token_hex(64)

# IPA Integration
# TODO: IPA Credentials and Implementation

# Plug Support
PLUG_ENABLED = os.getenv("PLUG_ENABLED", 'False')
