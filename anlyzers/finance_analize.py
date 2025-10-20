"""
@brief Finance department analysis module
Performs financial analysis of the PO department, including payroll (FOT), 
budget utilization, and top salary identification.
"""

import pandas as pd
from anlyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class FinanceAnalayzer(BaseAnalyzer):
    """
    @brief Analyzer for financial metrics of the PO department
    Calculates total payroll (FOT), compares it with department budget,
    and identifies top-paid employees.
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize Finance Analyzer
        Sets up data source and logger for financial analysis.
        """
        super().__init__(json_file_path, "Finance Departament")

    def execute_analysis(self):
        """
        @brief Execute financial analysis for PO department
        Computes total payroll (FOT), compares it with budget,
        and retrieves top 5 highest salaries.

        @return Dictionary containing financial statistics
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Finance Departament"))

        try:
            # calculate FOT for evrything employee
            FOT = self._FOT_departaments()

            #comparison Fot and budget
            comparison_FOT_budget = self._comparison_FOT_budget_departament()

            # search 5 employee with more salary
            top_salary = self._top_five_salary()

            # Return all statistics
            analysis_result = {
                "total_employees":  len(self.po_employee_dataframe),
                "FOT": FOT,
                "distribution_position": comparison_FOT_budget,
                "top_salary": top_salary,
            }

            self._generate_statistics_report(analysis_result)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Finance analyze"))

            return analysis_result

        except Exception as e:
            error_message = LogMessages.ANALYSIS_ERROR.format("Finance analyze", str(e))
            self.logger.error(error_message)
            raise e
        


    def _payroll_calculation(self, employee):
        """
        @brief Calculate individual payroll contribution (FOT) for reporting period
        If employee worked more than 1 year, FOT = 12 * salary.
        Otherwise, FOT = salary * full months worked.

        @param employee: Series containing employee data
        @return: Calculated FOT value (float)
        """
        hire = employee['hire_date']
        report = self.data_create

        if (report - hire).days > 365:
            return employee['salary'] * 12

        months = (report.year - hire.year) * 12 + (report.month - hire.month)
        if report.day < hire.day:
            months -= 1
        months = max(0, months)

        months = max(0, months)

        return employee['salary'] * months


    def _FOT_departaments(self):
        """
        @brief Perform parametrs analysis avarage for employees PO departments
        Calculates avarage salary, perfomance, experience

        @return Dataframe avarage meaning parametrs
        """

        self.logger.info(LogMessages.EMPLOYEE_PARAMETR_CALCULATION)

        self.po_employee_dataframe['FOT'] = self.po_employee_dataframe.apply(self._payroll_calculation, axis= 1)
        return self.po_employee_dataframe['FOT']
    
    def _comparison_FOT_budget_departament(self):
        """
        @brief Compare total FOT with department budget
        Calculates absolute and percentage usage of allocated budget.

        @return Dictionary with FOT, budget, and utilization percentage
        """

        self.logger.info(LogMessages.BUDGET_COMPARISON_START)

        budget = self.po_department_dataframe['budget'].iloc[0]
        total_fot = self.po_employee_dataframe['FOT'].sum()
        percent_used = round((total_fot / budget) * 100, 2) if budget > 0 else 0.0

        return {
            "total_fot": total_fot,
            "department_budget": budget,
            "budget_utilization_percent": percent_used
        }
    

    def _top_five_salary(self):
        """
        @brief Retrieve top 5 employees by salary
        Returns a DataFrame with key personal and position info.

        @return DataFrame with top 5 highest-paid employees
        """

        self.logger.info(LogMessages.TOP_SALARIES_RETRIEVAL)

        top_5 = self.po_employee_dataframe.nlargest(5, 'salary')
        return top_5[['full_name', 'position', 'salary']].copy()


    def _generate_statistics_report(self, analysis_results):
        """
        @brief Generate formatted financial analysis report
        Outputs key metrics to console.

        @param analysis_results: Dictionary containing financial analysis results
        """
        print("=" * 70)
        print(ReportMessages.FINANCE_HEADER)
        print("=" * 70)

        print(f"\n{ReportMessages.TOTAL_EMPLOYEES.format(analysis_results['total_employees'])}")
        print(f"{ReportMessages.FOT_TOTAL.format(analysis_results['distribution_position']['total_fot'])} RUB")
        print(f"{ReportMessages.BUDGET_ALLOCATED.format(analysis_results['distribution_position']["department_budget"])} RUB")
        print(f"{ReportMessages.BUDGET_UTILIZATION.format(analysis_results['distribution_position']["budget_utilization_percent"])}")
        print(self.po_employee_dataframe[["full_name", "position", "salary", "FOT"]].to_string(index=False))

        print("\n" + ReportMessages.TOP_SALARIES_HEADER)
        print(analysis_results['top_salary'].to_string(index=False))

