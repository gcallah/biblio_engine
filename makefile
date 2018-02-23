ODIR = berkeley/templates
MUDIR = myutils
UDIR = utils
TDIR = tests

dev:
	-git commit -a 
	git push origin master
	ssh gcallah@ssh.pythonanywhere.com 'cd /home/gcallah/mysite; /home/gcallah/mysite/myutils/dev.sh'

# prod:
# 	git push origin master
# 	ssh gcallah@ssh.pythonanywhere.com 'cd /home/gcallah/Emu86; /home/gcallah/Emu86/myutils/prod.sh'

# for future use:
#	ansible-playbook -i $(ADIR)/inventories/hosts $(ADIR)/dev.yml
