#!bin/bash

#chmod 400 deploy_rsa
#todo find a elegant way to instruct ansible to take right pem
cp deploy_rsa ~/.ssh/id_rsa
#rsync -rave "ssh -i pari-test.pem" .* ubuntu@ec2-52-14-252-14.us-east-2.compute.amazonaws.com:/home/ubuntu/pari/
git clone https://github.com/sankarpatw/pari-ansible.git
cd pari-ansible
ansible-playbook -l staging -u ubuntu -i hosts.yml -t deploy site.yml -vvvv