pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/mohsinrao51/weatherapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t weatherapp:latest ."
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f namespace.yaml"
                    sh "kubectl apply -f deployment.yaml"
                    sh "kubectl apply -f hpa.yaml"
                }
            }
        }
    }
}

