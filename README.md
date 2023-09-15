# Machine Learning Assignment2 : Car Price Prediction (from scratch)
### Name: Sitthiwat Damrongpreechar
### Student ID: st123994

### Deployed website URL: https://st123994_a2.ml2023.cs.ait.ac.th/

#### Required applications:
1. Visual Studio Code (VScode)
2. Docker Desktop
   
#### Required VScode extensions:
1. JupyterNoteBook
2. Python
3. Docker
4. Remote Development packages (optional)
5. Dev Containers (optional)

#### How to use:
1. Download or gitclone this repository.
2. Open your Docker Desktop for building images and composing.
3. Get into the folder 'app' and check the Docker files (.Dockerfile for python, mlflow.Dockerfile for Mlflow).
4. After building, to operate only local website, compose up the 'docker-compose.yaml' .
   -  To operated the 'assignment2.ipynb' and local website, compose up the file 'docker-compose_arch.yaml' (move file into './app/code' first). 
   - 'docker-compose-deploy.yaml' is the outline for deploying a docker compose in server.
5. Drive into remoted docker container name:
   - 'sittiwat555/dash-a2' for 'docker-compose.yaml', select 'open in browser'
   - 'assignment2' for 'docker-compose_arch.yaml', select 'attach in vscode'
   - 'assignment2-mlflow' for 'docker-compose_arch.yaml', select 'open in browser'
6. Run the 'index.py' file in folder 'code' to run the local website (for the 'docker-compose_arch.yaml')
7. Install extensions that VScode suggests.
8. Enjoy your prediction and Website! 
