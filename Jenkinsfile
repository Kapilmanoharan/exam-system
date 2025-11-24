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
                        bat 'python -m venv venv'
                        bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {

                        bat 'venv\\Scripts\\python.exe -m pytest'
                    }
                }
            }
    }

    post {
        always {
            cleanWs()
        }
    }
}
