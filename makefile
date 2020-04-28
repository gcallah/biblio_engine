ODIR = berkeley/templates
MUDIR = myutils
UDIR = utils
TDIR = tests

container:
	docker build -t biblio docker

prod:
	-git commit -a 
	git push origin master
	ssh gcallah@ssh.pythonanywhere.com 'cd /home/gcallah/mysite; /home/gcallah/mysite/myutils/dev.sh'

tests:
	echo "testing ... "
