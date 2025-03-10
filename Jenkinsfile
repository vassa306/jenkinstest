pipeline {
    agent {
        node {
            label 'docker-agent-alpine'
        }
    }
    tools {
        dockerTool 'docker'
    }
    environment {
        DOCKER_BIN = tool 'docker'      
        DOCKER_HOST="tcp://host.docker.internal:2375"
        IMAGE_NAME="hello-python"
        PATH = "/home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker:${env.PATH}"
        DOCKER_CREDENTIALS_ID = "fe9f411c-2291-41e0-92e3-450f19b3cbbb"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Build Name: ${env.JOB_NAME}, Build ID: ${env.BUILD_ID}"
                    echo "Building.."
                }
                sh '''
                    image_name="hello-python"
                    echo "Using docker from: $(which docker)"
                    echo "Doing build stuff..."
                    echo $PATH
                    echo $DOCKER_HOST
                   
                    echo "Building Docker image '$image_name'..."
                    docker build -t $IMAGE_NAME . || {
                        echo "Docker build failed"
                        exit 1
                    }

                    echo "Docker image built successfully."
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Testing.."
                sh 'echo "Doing test stuff..."'
            }
        }

        stage('Deliver') {
            steps {
                echo "Delivering.."
                sh '''
                    echo "running docker container"
                    echo "Pushing Docker image '$IMAGE_NAME'..."
                    docker rm -f test || true
                    docker run -d --name test $IMAGE_NAME || {
                        echo "Docker is running successfully"
                        exit 1
                    }
                    echo "Docker contaier is running successfully."
                '''
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    def dockerRepo = "vassa306/${env.IMAGE_NAME}"
                    withCredentials([usernamePassword(
                        credentialsId: DOCKER_CREDENTIALS_ID,
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh """
                            echo 'Logging in to Docker Hub...'
                            echo 'Pushing to Docker Hub...'
                            docker push ${dockerRepo}:latest || {
                                echo 'Docker push failed'
                                exit 1
                            }
                        """
                    }
                }
            }
        }
    }
}