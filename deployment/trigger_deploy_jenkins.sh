ssh ubuntu@172.31.7.214 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /var/lib/jenkins/horey_instances.pem -tt /home/ubuntu/trigger_deploy_backend.sh