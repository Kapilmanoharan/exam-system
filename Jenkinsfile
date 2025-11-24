pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv venv'
                        sh './venv/bin/pip install -r requirements.txt'
                    } else {
                        // Windows
                        bat 'python -m venv venv'
                        bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh './venv/bin/python -m pytest'
                    } else {
                        bat 'venv\\Scripts\\python.exe -m pytest'
                    }
                }
            }
        }
    }

    post {
        always {
            // clean workspace if you like
            cleanWs()
        }
    }
}
