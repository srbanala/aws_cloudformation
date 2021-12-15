pipeline {
    agent any
        environment{
            DOCKER_CREDS=credentials('docker_id')

            }
    stages{
        stage ('build'){
            steps {
            // sh 'chmod 777 s3-cloud-formation.yml' not required. fixed it
            // Configuring to use AWS credentials.
            withAWS(credentials: 's3-creds', region: 'us-east-1')
            {
           sh 'aws cloudformation create-stack --stack-name cloudformation-stack --template-body file://./cloud-formation.yml --parameters  file://./parameters.json  --region=us-east-1 '
           sh 'aws cloudformation create-stack --stack-name s3-stack --template-body file://./s3-cloud-formation.yml  --region=us-east-1 '
            }
            }
            }
        }
    }
