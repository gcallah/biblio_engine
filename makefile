ODIR = berkeley/templates
MUDIR = myutils
UDIR = utils
TDIR = tests

prod:
	-git commit -a 
	git push origin master
	ssh moabiblio@ssh.pythonanywhere.com 'cd /home/moabiblio/mysite; /home/moabiblio/mysite/myutils/dev.sh'

# the engine on its own (a made-up site), then the Oakeshott site
tests: engine_tests oakeshott_tests

engine_tests:
	python manage.py test berkeley --settings=mysite.settings_engine_test

oakeshott_tests:
	python manage.py test berkeley sites.oakeshott

dev_env:
	pip install -r requirements/requirements.txt
