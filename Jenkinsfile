pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                echo 'This is Anubhav!'
            }
        }
     stages {
        stage('test') { 
            steps { 
                input('Do you want to proceed?')
            }
        }
    }
}
}
