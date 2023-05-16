import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

# server Details
server = os.getenv('server')
username = os.getenv('username')
password = os.getenv('password')

def _dbConnection():
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+password+';TrustServerCertificate=yes')
	return cnxn