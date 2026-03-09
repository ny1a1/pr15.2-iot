# Практична робота №15.2
## Варіант 1: GitHub Actions Pipeline

![Validate](https://github.com/ny1a1/pr15.2-iot/actions/workflows/validate.yml/badge.svg)
![Tests](https://github.com/ny1a1/pr15.2-iot/actions/workflows/test.yml/badge.svg)
![Build](https://github.com/ny1a1/pr15.2-iot/actions/workflows/build.yml/badge.svg)
![Deploy](https://github.com/ny1a1/pr15.2-iot/actions/workflows/deploy.yml/badge.svg)

### Опис проєкту
Мета роботи — створити CI/CD pipeline для OpenHAB з використанням **GitHub Actions**.  
Pipeline автоматично виконує:
- Валідацію конфігурацій (YAML/JSON).
- Запуск тестів (unit та integration).
- Збірку Docker-образу.
- Деплой (симуляція або запуск через `docker-compose`).

Проєкт демонструє повний цикл: *валидація -> тести -> збірка -> деплой*.  

---

### Структура репозиторію
├── .github/workflows/  
│   ├── validate.yml  
│   ├── test.yml  
│   ├── build.yml  
│   └── deploy.yml  
├── openhab_conf/  
├── tests/  
│   ├─ unit/  
│   │    └── test_rule_example.py  
│   └─ integration/  
│        └── test_integration.py  
├── Dockerfile  
└── README.md  

---

### Workflows
- Validate OpenHAB Config -> перевіряє синтаксис YAML/JSON.  
- Run Tests -> запускає unit та integration тести.  
- Build Docker Image -> збирає Docker-образ на основі конфігів.  
- Deploy -> симулює деплой або запускає `docker-compose up`.

---

### Тести
- Unit tests: прості перевірки логіки (`1+1==2`, рядки тощо).  
- Integration tests: перевірка структури проєкту (наявність `openhab_conf`, `Dockerfile`).  
Усі тести виконуються через **pytest**.

---

### Результати
- Усі jobs успішно виконуються у вкладці **Actions**.  
- Pytest знаходить і виконує всі тести (unit + integration).  
- Docker-образ збирається без помилок.  
- Deploy job завершується успішно.