import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('environment_variables.env')
load_dotenv(dotenv_path=dotenv_path)

secretkey = os.getenv('secretkey')
api_key = os.getenv('api_key')

print("Testing")
print(api_key)
print(secretkey)