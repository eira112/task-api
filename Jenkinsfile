pipeline {
    agent any
    stages{
        stage('Test') {
            steps {
                sh 'docker compose up -d --build'
                sh 'docker compose exec -T task-api python create_tables.py'
                sh 'docker compose exec -T task-api python -m pytest'
            }
        }
        post{
            always{
                sh 'docker compose down --rmi local'
            }
        }
    }
}
