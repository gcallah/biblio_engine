ODIR = berkeley/templates
MUDIR = myutils
UDIR = utils
TDIR = tests

# the PythonAnywhere account to deploy to (pushing master deploys the
# Oakeshott site through GitHub Actions anyway)
PA_USER ?= moabiblio

prod:
	-git commit -a 
	git push origin master
	ssh $(PA_USER)@ssh.pythonanywhere.com 'cd /home/$(PA_USER)/mysite; /home/$(PA_USER)/mysite/myutils/dev.sh'

# the engine on its own (a made-up site), then the Oakeshott site
tests: engine_tests oakeshott_tests

engine_tests:
	python manage.py test berkeley --settings=mysite.settings_engine_test

oakeshott_tests:
	python manage.py test berkeley sites.oakeshott

dev_env:
	pip install -r requirements/requirements.txt
