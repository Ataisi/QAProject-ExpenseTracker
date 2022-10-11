pipeline {
    agent any
    environment {
        dockerImage = ''
        registry = 'fubara/qaprojectexpensetracker'
        registryCredential = 'Dockerhub'
	img = "$registry" + ":${env.BUILD_ID}"
    }
    stages {
         stage('check out') {
            steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github', url: 'https://github.com/Ataisi/QAProject-ExpenseTracker']]])
        }
    }
	stage("stop running Container")
        {
            steps {
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force'
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
            }
        }


        stage('Build Image') {
            steps {
             script {
                    dockerImage = docker.build("${img}")
            }
        }
    }
        stage('Test') {
            steps {
                echo "Testing..."
            }
       
        }
        stage('DockerHub Upload') {
            steps {
             script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
            }
        }
    }
}
       
    // Running Docker container
    stage('Docker Run') {
	steps {
                echo "image run"
                sh returnStdout: true,
                script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
           }
        }
    }
}


