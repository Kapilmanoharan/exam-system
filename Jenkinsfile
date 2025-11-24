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
                        // Windows
                        bat 'python -m venv venv'
                        bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
                    
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
            // clean workspace if you like
            cleanWs()
        }
    }
}
