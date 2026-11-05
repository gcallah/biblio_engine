ODIR = berkeley/templates
MUDIR = myutils
UDIR = utils
TDIR = tests

container:
	docker build -t biblio docker

prod:
	-git commit -a 
	git push origin master
	ssh moabiblio@ssh.pythonanywhere.com 'cd /home/moabiblio/mysite; /home/moabiblio/mysite/myutils/dev.sh'

tests:
	python manage.py test berkeley

dev_env:
	pip install -r requirements/requirements.txt
