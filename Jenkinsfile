pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'                // Nom de l'image Docker
        CONTAINER_NAME = 'flask-app-container'    // Nom du conteneur Docker
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/donatienne29/Testrepo.git', credentialsId: 'token-credentials-for-jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'docker --version'
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter les tests dans le conteneur
                sh '''
                docker run --rm ${DOCKER_IMAGE} pytest tests/ > test_results.txt
                cat test_results.txt
                '''
            }
        }

        stage('Deploy to Docker') {
            steps {
                script {
                    // Arrêter et supprimer le conteneur en cours d'exécution, le cas échéant
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // Démarrer un nouveau conteneur pour déployer l'application
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
