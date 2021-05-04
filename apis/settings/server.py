from .base import *
import re
import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "xh0hdptp4mb$h_qje*j=wp9hblb6pcg2fbwdq5yod10=2k)e0-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True
BIRTH_REL_NAME = "place of birth"
DEATH_REL_NAME = "place of death"
APIS_BASE_URI = "https://thinktanknetworkresearch.net/"


ALLOWED_HOSTS = ["thinktanknetworkresearch.net","ttnr.qprf.de"]
# You need to allow '10.0.0.0/8' for service health checks.


DEBUG = True
DEV_VERSION = True

SPECTACULAR_SETTINGS["COMPONENT_SPLIT_REQUEST"] = True
SPECTACULAR_SETTINGS["COMPONENT_NO_READ_ONLY_REQUIRED"] = True

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

LANGUAGE_CODE = "de"


APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]
