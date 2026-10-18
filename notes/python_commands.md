Python command

01) upgrade python 
	command: python.exe -m pip install --upgrade pip
	
02) check python version
		python --version or python -V

03) upgrade all python packages
        	01) first check putdated packages with command
				pip list --outdated
			02) create requirement.txt file
				pip freeze > requirements.txt
			03) run requirement.txt file 
				pip install -r requirements.txt --upgrade
				