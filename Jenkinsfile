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
                sh 'docker compose up -d --build'
                sh 'docker compose exec -T task-api python create-tables.py'
                sh 'docker compose exec -T task-api python -m pytest'
            }
        }
    }
}
