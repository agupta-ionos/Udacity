pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                echo 'make' 
            }
        }
        stage('Test'){
            steps {
                
                input('Do you want to proceed') 
                sh health.sh
            }
        }
        stage('Deploy') {
            steps {
                echo 'Anubhav publish'
            }
        }
    }
}
