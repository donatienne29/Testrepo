pipeline {
    agent any

    environment {
        APACHE_HTML_DIR = '/var/www/html'       
        HTML_FILE = 'index.html'                 
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/donatienne29/Testrepo.git', credentialsId: 'token-credentials-for-jenkins'
            }
        }

        stage('Build and Test') {
            steps {
                sh "htmlhint ${HTML_FILE}"         
            }
        }

        stage('Deploy to Apache') {
            steps {
                script {
                    sh "sudo cp ${HTML_FILE} ${APACHE_HTML_DIR}/"
                    sh "sudo systemctl restart httpd"  
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
