pipeline {
  agent any
  options {
      // Will set the build timeout at 5 minutes and disable concurrent builds.
      timeout(time: 5, unit: 'MINUTES')
      disableConcurrentBuilds()
  }
  triggers {
      // All builds will happen upon github push
      githubPush()
  }
  stages {
      /*
        Initialize all the pipline parameters and thresholds.
      */
      stage("Initialize") {
        steps {
          initialize()
        }
      }
      /*
        The pre checks will spit out all the pipeline envs and parameters (This stage is added for debugging within Jenkins).
      */
      stage("Pre-Checks") {
        steps {
          sh 'docker images'
        }
      }
      /*
        Will take the files from repo and will run them with a docker container at the root level. (If passes, will cache deps and destory container)
        If no database is required use the following for testing.
        ----------
        withDockerContainer(image: "python:3.7-alpine", args: "-u root:root") {
          sh "python --version"
          sh "pip install --no-cache-dir pipenv"
          sh "pipenv install --dev"
          sh "pipenv run pytest"
        }
      */
      stage('Testing') {
        steps {
          withDockerContainer(image: env.DOCKER_PYTHON_NAME, args: "-u root:root") {
            sh "python --version"
            sh "pip install --no-cache-dir pipenv"
            sh "pipenv install --dev"
            sh "pipenv run pytest"
          }
        }
      }
  }
}

def initialize() {
    // Docker Defs
    env.DOCKER_PYTHON_NAME = 'python:3.7-slim'
}
