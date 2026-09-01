pipeline {
    agent any

    stages {
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t task-api .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run task-api python -m pytest'
            }
        }
    }
}
//check pipeline