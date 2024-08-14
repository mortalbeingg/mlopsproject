echo [$(date)]: "START"

echo [$(date)]: "creating virtual env with python 3.11.0"

conda create --prefix ./env python==3.11.0 -y

echo [$(date)]: "activating the environment"

source activate ./env

echo [$(date)]: "installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)]: "END"