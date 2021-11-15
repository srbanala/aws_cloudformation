pipeline {
    agent any
        environment{
            DOCKER_CREDS=credentials('docker_id')
            }
    stages{
        stage ('build'){
            steps {
            sh 'echo $pwd'
            sh 'aws cloudformation create-stack --stack-name polls_stack --template-body file:./tmp/cloud-formation.yml --parameters  file:./tmp/parameters.json '
            }
        }
    }
}