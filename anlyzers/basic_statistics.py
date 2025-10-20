"""
@brief Employee analysis module
Generates basic employee statistics for salary, experience, etc.
"""

import pandas as pd
from anlyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class BasicStaticAnalayzer(BaseAnalyzer):
    """
    @brief Analyzer for basic statistics all employees PO department
    Implements common data loading and processing
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize Basic Statisrics Analyzer
        Sets up specific parametr configuration
        """
        super().__init__(json_file_path, "Basic Statistics")

    def execute_analysis(self):
        """
        @brief Execute Basic Statistics Analyze
        Check avarage salary, perfomance, experience, work level, employees with perfomance > 90

        @return Dictionary basic statistics
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Basic statics"))

        try:
            # parametrs: salary, perfomance, experience employees
            avarage_parametrs = self._avarage_parametrs_analysis()

            #Check level position: Junior/Middle/Senior/TeamLead
            destribution_position = self._analize_distribution_position()

            # Check employees with performance > 90
            high_performers = self._analyze_high_performers()

            # Return all statistics
            analysis_result = {
                "average_parameters": avarage_parametrs,
                "distribution_position": destribution_position,
                "high_performers": high_performers,
                "total_employee_count": len(self.po_employee_dataframe)
            }

            self._generate_statistics_report(analysis_result)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Basic Statistics"))

            return analysis_result

        except Exception as e:
            error_message = LogMessages.ANALYSIS_ERROR.format("Basic Statistics", str(e))
            self.logger.error(error_message)
            raise e
        

    def map_to_category(self, pos):
        """
        @brief Alghoritm for definition cetegory position
        Position have different title, but for analisys required category

        @param pos: Position employee
        @return category employee
        """
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

    def _avarage_parametrs_analysis(self):
        """
        @brief Perform parametrs analysis avarage for employees PO departments
        Calculates avarage salary, perfomance, experience

        @return Dataframe avarage meaning parametrs
        """

        self.logger.info(LogMessages.EMPLOYEE_PARAMETR_CALCULATION)

        avarage_salary = self.po_employee_dataframe["salary"].mean()
        avarage_perfomance = self.po_employee_dataframe["performance_score"].mean()
        avarage_experience = self.po_employee_dataframe["experience_years"].mean()

        avarage_parametrs = {
            "avarage_salary":       avarage_salary,
            "avarage_perfomance":   avarage_perfomance,
            "avarage_experience":   avarage_experience
        }

        return avarage_parametrs
    
    def _analize_distribution_position(self):
        """
        @brief Perform count the quantity work level
        Calculates count employees every work level

        @return Dataframe with two colomn: work level : count : percentage
        """

        self.logger.info(LogMessages.EMPLOYEE_WORK_LEVEL)
        self.logger.info(LogMessages.EMPLOYEE_CATEGORY)

        self.po_employee_dataframe['category'] = self.po_employee_dataframe['position'].apply(self.map_to_category)

        distribution_position = self.po_employee_dataframe['category'].value_counts().reset_index()
        distribution_position.columns = ['Category', 'Count']
        distribution_position['Percentage'] = (distribution_position['Count']/len(self.po_employee_dataframe)*100).round(2)
        
        return distribution_position
    

    def _analyze_high_performers(self):
        """
        @brief Perform search employees with high perfomance(>90)
        Create dataframe with employees where perfomance_score > 90

        @return Dataframe with persenal information
        """

        self.logger.info(LogMessages.EMPLOYEE_PERFOMANCE)

        return self.po_employee_dataframe[self.po_employee_dataframe['performance_score']>90
                                        ][[
                                            'full_name',
                                            'gender',
                                            'birth_date',
                                            'phone',
                                            'email',
                                            'position'
                                            ]]


    def _generate_statistics_report(self, analysis_results):
        """
        @brief Generate formatted inventory analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.STATIC_HEADER)
        print("=" * 70)

        total_employee_count = analysis_results['total_employee_count']
        total_employee_top = len(analysis_results['high_performers'])

        print(f"\n{ReportMessages.TOTAL_EMPLOYEES.format(total_employee_count)}")
        print(f"{ReportMessages.TOP_EMPLOYEE_COUNT.format(total_employee_top)}")

        print("\nAverage Parameters Employee:")
        avg = analysis_results['average_parameters']
        for key, value in avg.items():
            print(f'  {key}\t:\t{value:.2f}')

        print("\nDepartment Distribution Position Category:")
        department_position = analysis_results['distribution_position']
        print(department_position.to_string(index=False))

        print("\nPersonal info employees with performance > 90:")
        personal_info = analysis_results['high_performers']
        print(personal_info.to_string(index = False))

