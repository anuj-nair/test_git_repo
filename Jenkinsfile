pipeline {
    agent any
    // Add a tool configuration here...
    stages {
        stage('Source') {
            steps {
                git branch: 'main',
                    changelog: false,
                    poll: false,
                    url: 'https://github.com/anuj-nair/test_git_repo.git'
            }
        }
        stage('Build Environment') {
            steps {
                dir("${env.WORKSPACE}/Jenkins/Python"){
                  sudo apt install python3
                }
            }
        }
        stage('Clean') {
            steps {
                dir("${env.WORKSPACE}/Jenkins/Python"){
                    echo "Cleaning the workspace..."
                }
            }
        }
        stage('Test') {
            steps {
                dir("${env.WORKSPACE}/Jenkins/Python"){
                    echo "Running tests..."
                    // Uncomment the following line after Maven is configured as a global tool
                    // sh 'mvn test'
                }
            }
        }
        stage('Package') {
            steps {
                dir("${env.WORKSPACE}/Jenkins/Python"){
                    echo "Creating the JAR file..."
                    // Uncomment the following line after Maven is configured as a global tool
                    // sh 'mvn package -DskipTests'
                }
            }
        }
    }
//    post {
//        always {
//            echo "Collecting jUnit test results..."
//            // Add jUnit report collection here...
//
//            echo "Archiving the JAR file..."
//            // Add artifact archiving here...
//        }
//    }
}
