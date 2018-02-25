import os
import secrets


# SQL Alchemy
SQL_DATABASE_URI = os.getenv("SQL_DATABASE_URI", None)
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

# Application Secret Key
SECRET_KEY = secrets.token_hex(64)

# IPA Integration
# TODO: IPA Credentials and Implementation

# Plug Support
PLUG_ENABLED = os.getenv("PLUG_ENABLED", "False")
