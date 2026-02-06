This application is a backend that provides endpoints around Signals data. A tech enthusiast on the business side has been maintaining this application, now the IT department has been tasked with taking it over. 

Initial Assessment: 
The code quality is low, the previous developer was copying/pasting from tutorials.

Todo: 
- Productionalise this application (This is purposely vague, implement what you think is necessary for this small application to work on prod)
- Spend around 4-6 hours on this, document how you spent your time.

Steps taken to refactor the challenge

1 - Explore the repo  [ 1 hour ]

* Try to run it up to check what it does.
* Fix missing dependencies in order to run the server.
* Restructure the project to match a more classic FastApi approach.


2 - Modificate the configurations and structure  [ 1 hour ]

* Remove unused or deprecated config files.
* Remove unused folders and move actual used functions to files that contains the same logic.
* Add initial tests folder to add proper testing into the project.

3 - Remove all unused code [ 1 hour ]

* Track and delete all classes, imports and functions that are not used
* Simplify logic by deleting unused files after cleaning all camel case and uncalled functions
* Remove the logic of v2 and move it to v1 as it is registered
* Simplify routing schemas by putting the endpoitns in the same folder

4 - Start to add production missing code [ 1 hour ]

* Add a health endpoint to monitor once deployed that the service is up.
* Check for missing function calls into the classes that manages that mesurements and assets.
* Rename files to be concistent with the rest of the project.
* Add Logger to check what is happening.
* Not enable documentation endpoints when the environment is in production, is a security leak.

5 - Dockerization, github actions and missing tests [ 2 hour ]

* Dockerization of the application in an optimized docker image
* Add github actions to performe testing and linting checkings
* Add tests to check the service is properly working

