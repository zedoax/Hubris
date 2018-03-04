import os
import secrets


# SQL Alchemy
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

# Database
DATABASE_CREATION_SCRIPT = os.getenv("DATABASE_CREATION_SCRIPT", "/database/db_init.sql")

# Application Secret Key
SECRET_KEY = secrets.token_hex(64)

# IPA Integration
# TODO: IPA Credentials and Implementation

# Plug Support
PLUG_ENABLED = os.getenv("PLUG_ENABLED", 'False')
