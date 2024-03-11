pipeline {
    agent any

    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SaniaArshad/MLOPS-i202425-Activity2.git']])
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Execute Test') {
            steps {
                script {
                    bat 'python test.py'
                }
            }
        }

        stage('Deploying') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}