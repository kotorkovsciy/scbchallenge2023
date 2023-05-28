path=$(pwd)
pathVenv=$path"/venv"
pathEnv=$path"/env"
pathRequirements=$path"/requirements.txt"

if [ ! -d "$pathVenv" ] && [ ! -d "$pathEnv" ]; then
    python -m venv venv
    if [ ! -f "$pathRequirements" ]; then
        echo "requirements.txt not found."
        exit
    fi
fi

source venv/bin/activate

pip install -r requirements.txt

cd ./jobportal/utils
python setup.py build_ext --inplace
cd ../..
