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
                sh "htmlhint ${HTML_FILE}"          // Valider le fichier HTML
            }
        }

        stage('Deploy to Apache') {
            steps {
                script {
                    sh "sudo cp ${HTML_FILE} ${APACHE_HTML_DIR}/"
                    sh "sudo systemctl restart httpd"  // Redémarrer Apache
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
