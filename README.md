# Как захостить проект

## На windows

1. Запустить скрипт `compile_pars.ps1` (для этого нужно открыть PowerShell и ввести `.\compile_pars.ps1`).
2. Создать файл .env `New-Item -Path .env -ItemType file` и внести в него свои данные по примеру .env.example.
3. Запуск `python manage.py runserver`

## На linux
1. Использовать makefile, для этого нужно ввести в терминале `make build`
2. Создать файл .env (`touch .env`) по примеру .env.example. внеся в него свои данные.
3. Запуск `make run`

## На docker

1. Создать файл .env по примеру .env.example. внеся в него свои данные.
2. Запустите `docker-compose build`
3. Запуск `docker-compose up`
