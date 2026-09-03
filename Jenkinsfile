pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "cyrielle123/task-api"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

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
                sh 'docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} .'
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
                        docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {

                sh '/opt/homebrew/bin/kubectl config use-context kind-learning'

                withCredentials([usernamePassword(
                    credentialsId: 'postgres-db-creds',
                    usernameVariable: 'DB_USERNAME',
                    passwordVariable: 'DB_PASSWORD'
                )]) {
                    sh '''
                        /opt/homebrew/bin/kubectl create secret generic postgres-secret \
                          --from-literal=POSTGRES_PASSWORD="$DB_PASSWORD" \
                          --from-literal=DATABASE_URL="postgresql+psycopg://$DB_USERNAME:$DB_PASSWORD@postgres:5432/task_api" \
                          --dry-run=client \
                          -o yaml | /opt/homebrew/bin/kubectl apply -f -
                    '''
                }

                sh '/opt/homebrew/bin/kubectl apply -f k8s/postgres.yaml'

                sh '/opt/homebrew/bin/kubectl set image deployment/task-api task-api=${DOCKER_IMAGE}:${IMAGE_TAG}'

                sh '/opt/homebrew/bin/kubectl apply -f k8s/frontend.yaml'
                sh '/opt/homebrew/bin/kubectl apply -f k8s/ingress.yaml'

                sh '/opt/homebrew/bin/kubectl rollout status deployment/task-api'
                sh '/opt/homebrew/bin/kubectl rollout status deployment/task-frontend'
            }
        }
    }

    post {
        always {
            sh 'docker compose down --rmi local'
        }
    }
}