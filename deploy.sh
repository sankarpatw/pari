#!bin/bash

rsync -rave "ssh -i travis.pem" ./pari ubuntu@ec2-52-14-252-14.us-east-2.compute.amazonaws.com:/home/ubuntu/pari/
