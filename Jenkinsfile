pipeline{
    agent any
    stages{
        stage('Setup'){
            steps{
                sh '/opt/homebrew/bin/python3.14 --version'
                sh '/opt/homebrew/bin/python3.14 -m venv .venv'
                sh '.venv/bin/python --version'
                sh '.venv/bin/python -m pip --version'
                sh '.venv/bin/python -m pip install --upgrade pip'
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