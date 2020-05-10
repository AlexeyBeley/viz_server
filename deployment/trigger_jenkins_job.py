import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='horey', password='WERG$%^56533ERGGNH!!!^&^')
server.build_job('Deploy_Prod', {})
print('Hello %s from Jenkins %s' % (user['fullName'], version))