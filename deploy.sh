export project_name=mysite
export user_name=wm1065

echo "SSHing to PythonAnywhere."
sshpass ssh -o "StrictHostKeyChecking no" $user_name@ssh.pythonanywhere.com << EOF
    cd ~/$project_name; ~/$project_name/rebuild.sh $1
EOF
