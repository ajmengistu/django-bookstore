#!groovy

node {
   stage ('Set up project virtual environment') {
        def pythonVirtualEnvInstalled = fileExists 'bin/activate'
        
        // Django Documentation recommends to run django projects inside python virtual environments.
        // This allows you to manage your project dependencies without affecting the rest of your system.
        if (!pythonVirtualEnvInstalled) {
            sh 'virtualenv env -p python3.8.1'
        }
   }

    // Checkout the latest version of your project source code.
    // Save the last git commit SHA, author, and message into a file (LAST_GIT_COMMIT).
    // Send a notification to Slack.
   stage ('Checkout the latest source code & Send a notification to Slack') {
       checkout scm

       sh 'git log --pretty="[%h] %an: %s" -1 HEAD > LAST_GIT_COMMIT'
       def lastGitCommit = readFile('LAST_GIT_COMMIT')
       slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\N\N_The changes:_\n${lastGitCommit}"
   }

   stage ('Install Application Dependencies') {
       sh 'source bin/activate'
       sh 'pip install -r requirements.txt'
       sh 'deactivate'
   }

   stage ('Run unit tests & Send test results to Slack') {
       try {
           sh 'source bin/activate'
           sh 'python manage.py test'
           slackSend color: "good", message: "Tests successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
       } catch (err) {
           slackSend color: "danger", message: "Build failed: face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins"
           throw err
       }
   }

//    stage ('Deploy application to Heroku') {
//    }

   stage ('Publish results to Slack') {
       slackSend color: "good", message: "Deployment to Heroku successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
   }
}