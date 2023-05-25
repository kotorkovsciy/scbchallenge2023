$path = Get-Location
$pathVenv = $path.tostring() + "\venv"
$pathEnv = $path.tostring() + "\env"
$pathRequirements = $path.tostring() + "\requirements.txt"

if (-not ((Test-Path $pathVenv -PathType Container) -or (Test-Path $pathEnv -PathType Container))){
    python -m venv venv
    
    if (-not (Test-Path -Path $pathRequirements -PathType leaf)){
        throw [System.IO.FileNotFoundException] "requirements.txt not found."
        exit
    }
}

venv\scripts\activate
pip install -r requirements.txt

cd .\jobportal\utils

python setup.py build_ext --inplace

cd ..
cd ..
