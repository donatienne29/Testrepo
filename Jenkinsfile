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
                // Installer le validateur HTML et vérifier le fichier HTML
                sh 'npm install -g htmlhint'        // Installer htmlhint
                sh "htmlhint ${HTML_FILE}"          // Valider le fichier HTML
            }
        }

        stage('Approval for Deployment') {
            steps {
                script {
                    def userInput = input(
                        message: 'Souhaitez-vous déployer l\'application sur le serveur Apache ?',
                        parameters: [
                            choice(name: 'DEPLOY', choices: ['Oui', 'Non'], description: 'Sélectionnez Oui pour déployer ou Non pour annuler')
                        ]
                    )
                    if (userInput == 'Non') {
                        echo 'Déploiement annulé par l\'utilisateur.'
                        currentBuild.result = 'SUCCESS'  // Laisse le pipeline en succès même si le déploiement est annulé
                        return
                    }
                }
            }
        }

        stage('Deploy to Apache') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
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
