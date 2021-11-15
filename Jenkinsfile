pipeline {
    agent any
        environment{
            DOCKER_CREDS=credentials('docker_id')
            }
    stages{
        stage ('build'){
            steps {
            sh 'echo $pwd'
            sh 'aws cloudformation create-stack --stack-name polls_stack --template-body file://./cloud-formation.yml --parameters  file://./parameters.json  --region=us-east-1 ''
            }
        }
    }
}