from setuptools import setup , find_packages 
from src.exception_file import CustomException 
import sys 

HYPEN_DOT = "-e ."

try:
    def get_requirements(file):

        with open(file) as f:

            data = f.readlines()
            data = [i.replace("\n", "") for i in data]

            if HYPEN_DOT in data:
                data.remove(HYPEN_DOT)

        return data  

except Exception as e:
    raise CustomException(e,sys)

try:
    setup(
    name = "e_t_e_p",
    version='0.0.1',
    author="BOT",
    author_email="phewpheww123@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt") 
)
 
except Exception as e:
    CustomException(e,sys)
