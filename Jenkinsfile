pipeline {
    agent any
    
    environment {
        PROJECT_ID = "iyaawu-platform"
        REPOSITORY_NAME = "cayvibes"
        IMAGE_NAME_1 = "gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}-api"
        IMAGE_NAME_2 = "gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}-celebrity"
        IMAGE_NAME_3 = "gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}-fan"
        IMAGE_NAME_4 = "gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}-ngo"
        IMAGE_NAME_5 = "gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}-notification"
        BITBUCKET_CREDENTIALS_ID = "bitbucket-oauth-token"
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    def repos = [
                        [url: 'https://bitbucket.org/Lafiyatelehealth/cayvibes-api-gateway.git', dir: 'workspace1'],
                        [url: 'https://bitbucket.org/Lafiyatelehealth/cayvibes-celebrity-service.git', dir: 'workspace2'],
                        [url: 'https://bitbucket.org/Lafiyatelehealth/cayvibes-fan-service.git', dir: 'workspace3'],
                        [url: 'https://bitbucket.org/Lafiyatelehealth/cayvibes-ngo-service.git', dir: 'workspace4'],
                        [url: 'https://bitbucket.org/Lafiyatelehealth/cayvibes-notification-service.git', dir: 'workspace5'],
                    ]

                    def branches = 'refs/heads/development/pipeline'

                    parallel repos.collectEntries { repo ->
                        ["Checkout ${repo.dir}": {
                            dir(repo.dir) {
                                checkout([$class: 'GitSCM',
                                    branches: [[name: branches]],
                                    userRemoteConfigs: [[
                                        url: repo.url,
                                        credentialsId: BITBUCKET_CREDENTIALS_ID
                                    ]]
                                ])
                            }
                        }]
                    }
                }
            }
        }
        stage('Image Build') {
            parallel {
                stage('Build Image 1') {
                    steps {
                        script {
                            dir('repo1') {
                                app = docker.build("${IMAGE_NAME_1}:${BUILD_NUMBER} .")
                            }
                        }
                    }
                }
                stage('Build Image 2') {
                    steps {
                        script {
                            dir('repo2') {
                                app = docker.build("${IMAGE_NAME_2}:${BUILD_NUMBER} .")
                            }
                        }
                    }
                }
                stage('Build Image 3') {
                    steps {
                        script {
                            dir('repo3') {
                                app = docker.build("${IMAGE_NAME_3}:${BUILD_NUMBER} .")
                            }
                        }
                    }
                }
                stage('Build Image 4') {
                    steps {
                        script {
                            dir('repo4') {
                                app = docker.build("${IMAGE_NAME_4}:${BUILD_NUMBER} .")
                            }
                        }
                    }
                }
                stage('Build Image 5') {
                    steps {
                        script {
                            dir('repo5') {
                                app = docker.build("${IMAGE_NAME_5}:${BUILD_NUMBER} .")
                            }
                        }
                    }
                }
            }

        }
        
        stage('Push to GCR') {
            parallel {
                stage('Push Image 1') {
                    steps {
                        script {
                            docker.withRegistry('https://gcr.io', 'gcr:jenkins-gcr-auth') {
                                docker.image("${IMAGE_NAME_1}:${BUILD_NUMBER}").push()
                            }
                        }
                    }
                }
                stage('Push Image 2') {
                    steps {
                        script {
                            docker.withRegistry('https://gcr.io', 'gcr:jenkins-gcr-auth') {
                                docker.image("${IMAGE_NAME_2}:${BUILD_NUMBER}").push()
                            }
                        }
                    }
                }
                stage('Push Image 3') {
                    steps {
                        script {
                            docker.withRegistry('https://gcr.io', 'gcr:jenkins-gcr-auth') {
                                docker.image("${IMAGE_NAME_3}:${BUILD_NUMBER}").push()
                            }
                        }
                    }
                }
                stage('Push Image 4') {
                    steps {
                        script {
                            docker.withRegistry('https://gcr.io', 'gcr:jenkins-gcr-auth') {
                                docker.image("${IMAGE_NAME_4}:${BUILD_NUMBER}").push()
                            }
                        }
                    }
                }
            }            
        }
        stage('Deploy on compose cluster'){
            steps{
                script{
                    def ShellCmd = "bash ./script.sh ${IMAGE_NAME}"
                    sshagent(['jenkins-ssh-key']) {
                        sh "scp -o StrictHostKeyChecking=no docker-compose.yml prosperagada@34.66.159.198:/home/prosperagada"
                        sh "scp -o StrictHostKeyChecking=no script.sh prosperagada@34.66.159.198:/home/prosperagada"
                        sh "ssh -o StrictHostKeyChecking=no prosperagada@34.66.159.198 ${ShellCmd}"
                        echo "SUCCESS"
                    }
                }
            }
        }


    }
}



