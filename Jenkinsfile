pipeline {

    agent any

    stages {

        stage('Test') {
            steps {
                sh 'docker compose up -d --build postgres task-api'
                sh 'docker compose exec -T task-api python create_tables.py'
                sh 'docker compose exec -T task-api python -m pytest'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t cyrielle123/task-api:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push cyrielle123/task-api:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker compose down --rmi local'
        }
    }
}