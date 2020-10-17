pipeline {
	agent {
		label generic
	}//label
	stages {
        stage("Run the code") {
            steps { 
 				sh """
					python3 calculator.py
				"""
          	} //steps
        } //stage
		stage("Run Unit tests") {
			steps {
				sh """
					python3 -m pytest
				"""
			} //steps
		} //stage
	} //stages
} //pipeline
