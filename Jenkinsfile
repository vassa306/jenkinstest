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
        IMAGE_NAME="vassa306/hello-python"
        PATH = "/home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker:${env.PATH}"
        DOCKER_CREDENTIALS_ID = "fe9f411c-2291-41e0-92e3-450f19b3cbbb"
        TAG_NAME = "${BUILD_NUMBER}"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Build Name: ${env.JOB_NAME}, Build ID: ${env.BUILD_ID}"
                    echo "Building.."
                }
                sh '''
                    echo "Building Docker image '$image_name'..."
                    docker build -t $IMAGE_NAME:$TAG_NAME . || {
                        echo "Docker build failed"
                        exit 1
                    }

                    echo "Docker image built successfully."
                '''
            }
        }

        

        stage('creating and running container') {
            steps {
                echo "Delivering.."
                sh '''
                    echo "running docker container"
                    echo "Pushing Docker image '$IMAGE_NAME'..."
                    docker rm -f test || true
                    docker run -d --name test $IMAGE_NAME:$TAG_NAME || {
                        echo "Docker is running successfully"
                        exit 1
                    }
                    echo "Docker contaier is running successfully."
                '''
            }
        }


        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "Running containers:" 

                echo "Checking if our image is present in the list of images"
                docker images --format "{{.Repository}}:{{.Tag}}" | grep vassa306 || {
                    echo "Image not found"
                    exit 1
                    }
                '''   
            }
        }

        stage('Login & Push to Docker Hub') {
            steps {
                script {
                    def dockerRepo = "${env.IMAGE_NAME}"
                    withCredentials([usernamePassword(
                        credentialsId: DOCKER_CREDENTIALS_ID,
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh """
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            echo 'Pushing image: ${dockerRepo}:${env.TAG_NAME}'
                            docker push ${dockerRepo}:${env.TAG_NAME}
                        """
                    }
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    echo "🧹 Cleaning up Docker images related to vassa306..."

                    sh """
                        docker images --format "{{.Repository}}:{{.Tag}}" | grep vassa306 || true
                        docker images --format "{{.Repository}}:{{.Tag}}" | grep vassa306 | xargs -r docker rmi || true
                    """
                }
            }
        }
    }
}