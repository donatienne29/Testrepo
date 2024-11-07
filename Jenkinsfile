pipeline {
    agent any

    environment {
        APACHE_HTML_DIR = '/var/www/html'       // Répertoire HTML Apache
        HTML_FILE = 'index.html'                 // Nom du fichier HTML à déployer
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/donatienne29/Testrepo.git', credentialsId: 'token-credentials-for-jenkins'
            }
        }

        stage('Build and Test') {
            steps {
                // Si tu as des étapes de build ou de test, tu peux les ajouter ici
                echo 'Build and test steps (if any) go here'
            }
        }

        stage('Deploy to Apache') {
            steps {
                script {
                    // Copier le fichier HTML vers le répertoire d'Apache
                    sh "sudo cp ${HTML_FILE} ${APACHE_HTML_DIR}/"
                    sh "sudo systemctl restart httpd"  // Redémarrer Apache pour appliquer les changements
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
