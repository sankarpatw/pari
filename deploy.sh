#!bin/bash

chmod 400 pari-test.pem
rsync -rave "ssh -i pari-test.pem" .* ubuntu@ec2-52-14-252-14.us-east-2.compute.amazonaws.com:/home/ubuntu/pari/
