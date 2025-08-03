pipeline {
    agent any

    environment {
        IMAGE_NAME = "weatherapp"
        CONTAINER_NAME = "weatherapp-container"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/mohsinrao51/weatherapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Test App') {
            steps {
                sh 'curl -I http://localhost:5000 || true'
            }
        }
    }

    post {
        always {
            echo "Cleaning up exited containers..."
            sh "docker ps -a"
        }
    }
}

