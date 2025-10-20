import pandas as pd
import json

with open('company.json', "r", encoding='utf-8') as json_file:
    data = json.load(json_file)

department_records = []
for department in data.get("departments", []):
    department_record = {
        "id":       department["id"],
        "name":     department["name"],
        "type":     department["type"],
        "budget":   department["budget"]
    }
    if department_record['id'] == 1:
        department_records.append(department_record)
        break

department_dataframe = pd.DataFrame(department_records)

employee_records = []
for employee in data.get("employees", []):
    employee_record = {
        "employee_id":          employee["employee_id"],
        "full_name":            employee["personal_info"]["full_name"],
        "gender":               employee["personal_info"]["gender"],
        "birth_date":           employee['personal_info']['birth_date'],
        "email":                employee['personal_info']['email'],
        "phone":                employee['personal_info']['phone'],
        "address":              employee['personal_info']['address'],
        "department_id":        employee['work_info']['department_id'],
        "department_name":      employee['work_info']['department_name'],
        "position":             employee['work_info']['position'],
        'salary':               employee['work_info']['salary'],
        'hire_date':            employee['work_info']['hire_date'],
        'experience_years':     employee['work_info']['experience_years'],
        'performance_score':    employee['work_info']['performance_score'],
        "skills":               employee['work_info']["skills"],
        "is_team_lead":         employee['work_info']['is_team_lead']
    }
    if employee_record['department_id'] == 1:
        employee_records.append(employee_record)

employee_dataframe = pd.DataFrame(employee_records)

employee_dataframe['hire_date'] = pd.to_datetime(employee_dataframe['hire_date'])
employee_dataframe['birth_date'] = pd.to_datetime(employee_dataframe['birth_date'])

project_records = []
for project in data.get("projects", []):

    dept_ids = [d['department_id'] for d in project['participating_departments']]

    if 1 in dept_ids:
        project_record = {
            "project_id":       project['project_id'],
            "department_id":    dept_ids,
            "name":             project['name'],
            "description":      project['description'],
            "status":           project['status'],
            "budget":           project['financials']['budget'],
            "profit":           project['financials']['profit'],
            "roi_percentage":   project['financials']['roi_percentage']
        }
        project_records.append(project_record)

def map_to_category(pos):
    pos_lower = pos.lower()
    
    if 'стажер' in pos_lower:
        return 'trainee'
    
    if any(kw in pos_lower for kw in ['junior', 'младший']):
        return 'junior'
    
    if any(kw in pos_lower for kw in ['team lead', 'технический руководитель', 'head of', 'руководитель']):
        return 'teamlead'
    
    if any(kw in pos_lower for kw in ['инженер-программист', 'разработчик']) and not any(
        s in pos_lower for s in ['старший', 'ведущий', 'главный', 'архитектор']
    ):
        return 'middle'
    
    if any(kw in pos_lower for kw in [
        'старший', 'ведущий', 'архитектор', 'devops', 'senior'
    ]):
        return 'senior'
    
    return 'senior'

project_dataframe = pd.DataFrame(project_records)
employee_dataframe['categiry'] = employee_dataframe['position'].apply(map_to_category)

print(employee_dataframe["hire_date"])
print(department_dataframe)
print(project_dataframe)