import pandas as pd
import json

with open('company.json', "r", encoding='utf-8') as json_file:
    data = json.load(json_file)

# { пример из company.json
#       "employee_id": 148,
#       "personal_info": {
#         "first_name": "Максим",
#         "last_name": "Лебедев",
#         "middle_name": "Михайлович",
#         "full_name": "Лебедев Максим Михайлович",
#         "gender": "male",
#         "birth_date": "1967-05-27",
#         "email": "максим.лебедев@technopro.ru",
#         "phone": "8 (572) 415-3745",
#         "address": "г. Шаховская, наб. Моховая, д. 657 к. 7/7, 383818"
#       },
#       "work_info": {
#         "department_id": 5,
#         "department_name": "Отдел кибербезопасности",
#         "position": "Главный архитектор",
#         "salary": 102986,
#         "hire_date": "2024-07-20T22:30:00.768035",
#         "experience_years": 15,
#         "performance_score": 88.6,
#         "skills": [
#           "Kubernetes",
#           "C++",
#           "Linux"
#         ],
#         "is_team_lead": false,
#         "work_schedule": "удаленная работа"
#       },
#       "additional_info": {
#         "education": "Высшее",
#         "language_skills": [
#           "Французский",
#           "Китайский",
#           "Немецкий"
#         ],
#         "certifications": 4,
#         "has_company_car": true,
#         "security_clearance": true
#       }
#     },
employee_records = []
for employee in data.get("employees", []):
    employee_record = {
        "employee_id": employee["employee_id"],
        "full_name": employee["personal_info"]["full_name"]
    }