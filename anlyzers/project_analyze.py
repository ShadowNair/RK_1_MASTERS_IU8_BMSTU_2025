"""
@brief Project analysis module
Analyzes PO department projects by status, ROI, and profitability.
Identifies the most profitable project and provides key metrics.
"""

import pandas as pd
from anlyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class ProjectAnalayzer(BaseAnalyzer):
    """
    @brief Analyzer for PO department project performance
    Evaluates project statuses, average ROI, and identifies the top-profit project.
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize Project Analyzer
        Sets up data source and logger for project analysis.
        """
        super().__init__(json_file_path, "Project")

    def execute_analysis(self):
        """
        @brief Execute comprehensive project analysis
        Computes project status distribution, average ROI,
        and identifies the most profitable project.

        @return Dictionary containing project analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Project"))

        try:
            # status: active, completed
            status_project = self._status_project_check()

            #Mean ROI projects
            average_ROI_project = self._average_ROI_check()

            # Search top project: max profit
            top_project = self._search_top_benefit_project()

            # Return all statistics
            analysis_result = {
                "total_projects":  len(self.po_project_dataframe),
                "status_project": status_project,
                "average_ROI_project": average_ROI_project,
                "top_project": top_project,
            }

            self._generate_statistics_report(analysis_result)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Project"))

            return analysis_result

        except Exception as e:
            error_message = LogMessages.ANALYSIS_ERROR.format("Project", str(e))
            self.logger.error(error_message)
            raise e
        

    def _status_project_check(self):
        """
        @brief Analyze distribution of project statuses
        Counts projects by status (e.g., Active, Completed, On Hold).

        @return DataFrame with columns: 'Status', 'Count'
        """
        self.logger.info(LogMessages.PROJECT_STATUS_ANALYSIS)

        stat_projects = self.po_project_dataframe['status'].value_counts().reset_index()
        stat_projects.columns = ['Status', 'Count']
        stat_projects = stat_projects[stat_projects['Status'] != 'planning']
        return stat_projects
    
    def _average_ROI_check(self):
        """
        @brief Calculate average ROI across all PO projects
        ROI is expected to be stored as a percentage (e.g., 25.5 for 25.5%).

        @return Average ROI as float
        """
        self.logger.info(LogMessages.PROJECT_ROI_CALCULATION)

        return self.po_project_dataframe['roi_percentage'].mean()
    

    def _search_top_benefit_project(self):
        """
        @brief Identify the project with the highest absolute profit
        Returns key details of the top-profit project.

        @return Series with fields: project_id, name, description, profit, status
        """
        self.logger.info(LogMessages.TOP_PROFIT_PROJECT_IDENTIFICATION)

        idx_max = self.po_project_dataframe['profit'].idxmax()

        top_profit_project = self.po_project_dataframe.loc[idx_max, ['project_id', 'name', 'description', 'profit', 'status']]
        return top_profit_project


    def _generate_statistics_report(self, analysis_results):
        """
        @brief Generate formatted project analysis report
        Outputs key project metrics to console.

        @param analysis_results: Dictionary containing project analysis results
        """
        print("=" * 70)
        print(ReportMessages.PROJECT_HEADER)
        print("=" * 70)

        print(f"\n{ReportMessages.TOTAL_PROJECTS.format(analysis_results['total_projects'])}")

        print(f"\n{ReportMessages.AVERAGE_ROI.format(analysis_results['average_ROI_project'])}%")

        print(f"\n{ReportMessages.PROJECT_STATUS_DISTRIBUTION}")
        print(analysis_results['status_project'].to_string(index=False))

        print(f"\n{ReportMessages.TOP_PROFIT_PROJECT}")
        top_proj = analysis_results['top_project']
        if top_proj is not None:
            print(f"  ID: {top_proj['project_id']}")
            print(f"  Name: {top_proj['name']}")
            print(f"  Status: {top_proj['status']}")
            print(f"  Profit: {top_proj['profit']:,.0f} RUB")
            print(f"  Description: {top_proj['description']}")
        else:
            print("  No projects found.")

