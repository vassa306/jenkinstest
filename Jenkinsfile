pipeline {
    agent { 
        node {
            label 'docker-agent-alpine'
        }
    }
    tools {
        dockerTool 'docker'  // Musí odpovídat názvu v tool konfiguraci
    }
    environment {
        DOCKER_BIN = tool 'docker'
        PATH = "/home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker:${env.PATH}"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Build Name: ${env.JOB_NAME}, Build ID: ${env.BUILD_ID}"
                    echo "Building.."
                }
                sh '''
                    echo "doing build stuff.."
                    java --version
                    DOCKER_HOST="tcp://host.docker.internal:2375"
                    echo "PATH: $PATH"
                    chmod +x /home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker

                    echo "Checking Docker version..."
                    /home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker/docker --version || {
                        echo "Docker binary not found or not executable."
                        exit 1
                    }

                    echo "Running docker ps..."
                    /home/jenkins/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/docker/docker/docker ps -a || {
                        echo "docker ps' failed – check if Docker daemon is working properly."
                        exit 1
                    }

                    echo "Docker is working correctly."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                    echo "doing test stuff.."
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo "Build Name: ${env.JOB_NAME}, Build ID: ${env.BUILD_ID}"
                echo "Delivering.."
                sh '''
                    echo "doing delivery stuff.."
                '''
            }
        }
    }
}