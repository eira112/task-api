pipeline{
    agent any
    stages{
        stage('Setup'){
            steps{
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Test'){
            steps{
                sh 'python -m pytest'
            }
        }
    }
}