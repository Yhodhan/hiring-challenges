# Setup project 

**Requisites**
- Python 3.11.8
- Using pyenv to set it up locally is recommended

**Building**
    
1. Create and activate venv:
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run can be done with:
```bash
    python -m app.main
```
or
```bash
    uvicorn app.main:app --reload
```
if you want reload or you can skip the flag if not wanted, it is suggested to have it on for development and testing enviroments


**Testing**

Testing can be done by simple running the next command inside the virtual venv:
```bash
    pytest tests/
```
  
**Docker**

Docker container can be run with 
```bash
    docker build -t signals .
```
then
```bash
    docker run -p 8000:8000 signals
```
Name of the image is optional and up to the user, use what is more confortable.


# Steps taken to refactor the challenge
 - Explore the repo to check what contains and how can be build [ 30 mins ]:
 - Modificate the structure and packages names[ 30 mins ]:
 - Remove all unused code, including redundant or mispelled functions and classes [ 2 hours ]:
 - add logging and configurations files for production environment [ 30 mins ]
 - add missing calls into the router like displaying the index page and the mesurements [ 30 mins ]
 - Dockerization, github actions and missing tests [ 1 hour ]
 - Polish documentation [ 1 hour ]

# Decisions 

- Restructure the project to match a more classic FastApi approach.
- Remove unused folders and move actual used functions to files that contains the same logic.
- Add a health endpoint to monitor the service once deployed.
- Rename files to be concistent with the rest of the project.
- Add Logger to check track activity.
- Not enable documentation endpoints when the environment is in production.
- Remove the logic of v2 and move it to v1 as it is registered
- Simplify routing schemas by putting the endpoitns in the same folder
- Dockerization of the application in an optimized docker image
- Add github actions to performe testing and linting checkings when submitting a pull request
- Add tests to check the service is properly working

# Missing features

- Tests for the mesurements service to check its proper behaviour. 
- Configuration to connect it to Datadog/Graphana or other monitoring systems 
- Restructure some of the logics as there yet files that only contains one function.
- Better management of the dependencies versions to avoid errors. 
