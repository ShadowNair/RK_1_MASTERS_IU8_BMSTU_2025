"""
@brief Base analyzer class for technical department performance analysis
Provides common functionality and interface for all analyzers
"""

import pandas as pd
import json
from utils.logger import analysis_logger
from config.messages import LogMessages

class BaseAnalysis:
    """
    @brief Base class for all technical department performance analysis
    Implements common data loading and processing functionality
    """

    def __init__(self, json_file_path, analysis_name):
        """
        @brief Initialize base analyzer with data source
        Sets up data loading and logger configuretion

        @param json_file_path: Path to JSON data file
        @param analysis_name: Name of the analysis for logging
        """

        self.json_file_path = json_file_path
        self.analysis_name = analysis_name
        self.logger = analysis_logger.get_analysis_logger(analysis_name)
        self.data = None
        self.po_department_dataframe = None
        self.po_employee_dataframe = None
        self.po_project_dataframe = None

        self.logger.info(LogMessages.SYSTEM_START)
        self._load_data()
        self._setup_dataframes()

    def _load_data(self):
        """
        @brief Load JSON data from specified file path
        Handles file reading and JSON parsing with error handling
        """
        self.logger.info(LogMessages.DATA_LOAD_START)
        try:
            with open(self.json_file_path, "r", encoding='utf-8') as json_file:
                self.data = json.load(json_file)
            self.logger.info(LogMessages.DATA_LOAD_SUCCESS)
        except Exception as loading_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format(self.json_file_path, str(loading_error))
            self.logger.error(error_message)
            raise loading_error


    def _setup_dataframes(self):
        """
        @brief Create pandas DataFrames from loaded JSON data
        Processes equipment, departments, and employees data
        """
        self.logger.info(LogMessages.DATA_PROCESSING_START.format(self.analysis_name))

        if not self.data:
            return
        
        try:
            self.logger.info(LogMessages.START_CREATE_DATAFRAME.format("department PO"))
            department_records = []
            for department in self.data.get("departments", []):
                department_record = {
                    "id":       department["id"],
                    "name":     department["name"],
                    "type":     department["type"],
                    "budget":   department["budget"]
                }
                if department_record['id'] == 1:
                    department_records.append(department_record)
                    break

            self.po_department_dataframe = pd.DataFrame(department_records)
        except Exception as dataframe_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format("department", str(dataframe_error))
            self.logger.error(error_message)
            raise dataframe_error
        
        try:
            self.logger.info(LogMessages.START_CREATE_DATAFRAME.format("employees PO"))
            employee_records = []
            for employee in self.data.get("employees", []):
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

            self.po_employee_dataframe = pd.DataFrame(employee_dataframe)
        except Exception as dataframe_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format("employee", str(dataframe_error))
            self.logger.error(error_message)
            raise dataframe_error
        
        try:
            self.logger.info(LogMessages.START_CREATE_DATAFRAME.format("project PO"))
            project_records = []
            for project in self.data.get("projects", []):

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

            self.po_project_dataframe = pd.DataFrame(project_records)

        except Exception as dataframe_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format("project", str(dataframe_error))
            self.logger.error(error_message)
            raise dataframe_error
    

    def execute_analysis(self):
        """
        @brief Execute the analysis (to be implemented by subclasses)
        Template method for analysis execution
        """
        raise NotImplementedError("Subclasses must implement execute_analysis method")


