# Реализация взаимодействия с моделью в Docker через API

### ML задача — предсказать дефолт по кредиту

Flask обвязка и шаблон Docker на базе https://github.com/fimochka-sudo/GB_docker_flask_example

__Структура проекта:__
1. __./data/__ директорий с датасетом и преобразованными данными
2. __./models/__ директорий с моделью
3. __./app/__ директорий с flask приложением
4. __ml_credits.ipynb__ блокнот с поисковым анализом EDA, пайплайном и сравнением двух моделей
5. __ml_cr_pipeline.py__ пайплайн для формирования модели
6. __ml_credits_evaluation.ipynb__ блокнот с тестом готового приложения
7. __./app/run_server.py__ код flask приложения
8. __requirements.txt__ зависимости для формирования venv проекта
9. __Dockerfile__ 
10. __docker-entrypoint.sh__
