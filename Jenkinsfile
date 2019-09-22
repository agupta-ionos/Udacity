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
                python demo.py
                input('Do you want to proceed') 
            }
        }
        stage('Deploy') {
            steps {
                echo 'Anubhav publish'
            }
        }
    }
}
