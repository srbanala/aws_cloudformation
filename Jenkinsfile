pipeline {
    agent any
        environment{
            DOCKER_CREDS=credentials('docker_id')
            }
    stages{
        stage ('build'){
            steps {
            sh 'aws cloudformation create stack --stack-name polls_stack --template-body file:/tmp/cloud-formation.yml --parameters  ParameterKey=VpcId ParamerValue=vpc-08ae2ef40662a7b41   ParameterKey=KeyName ParameterValue=mykp  ParameterKey=PublicSubnetId ParameterValue=vpc-08ae2ef40662a7b41 '
            }
        }
}