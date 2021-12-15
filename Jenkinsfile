pipeline {
    agent any
        environment{
            DOCKER_CREDS=credentials('docker_id')
            s3_creds=credentials('s3-creds')
            }
    stages{
        stage ('build'){
            steps {
            sh 'aws configure set  aws_access_key "${aws_access_key_id}" '
            sh 'aws configure set aws_secret_access_key "${aws_secret_access_key}" '
            sh 'aws cloudformation create-stack --stack-name s3-stack --template-body file://./s3-cloud-formation.yml --parameters  file://./parameters.json  --region=us-east-1 '
            }
        }
    }
}