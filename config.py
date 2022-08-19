import os

basedir = os.path.abspath(os.path.dirname(__file__))


# creating a configuration class
class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'\

    # MONGO_URI = os.environ.get('MONGO_URI') or  os.environ.get("MONGO_URI")

    # MONGO_URI_1 = os.environ.get('MONGO_URI_1') or  os.environ.get("MONGO_URI_1")


christest = RqWserxiKEAvhTTB

uri = 'mongodb+srv://christest:<password>@christest.syc3ksr.mongodb.net/?retryWrites=true&w=majority'