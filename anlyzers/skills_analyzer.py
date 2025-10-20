"""
@brief Skills analysis module
Analyzes employee skill sets to identify technology coverage,
most in-demand and rare skills, and employees with specific tech combinations.
"""

import pandas as pd
from anlyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class SkillsAnalayzer(BaseAnalyzer):
    """
    @brief Analyzer for employee technical skills in PO department
    Builds skill matrix, identifies key competencies, and finds specialists
    with specific technology combinations (e.g., Python + Docker).
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize Skills Analyzer
        Sets up data source and logger for skills analysis.
        """
        super().__init__(json_file_path, "Skills")

    def execute_analysis(self):
        """
        @brief Execute comprehensive skills analysis
        Generates skill matrix, identifies top/rare skills,
        and finds employees with Python + Docker.

        @return Dictionary containing skills analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Skills"))

        try:
            skill_matrix = self._build_skill_matrix()

            skill_stats = self._analyze_skill_demand()

            python_docker_experts = self._find_python_docker_experts()

            analysis_result = {
                "total_employees": len(self.po_employee_dataframe),
                "skill_matrix": skill_matrix,
                "skill_statistics": skill_stats,
                "python_docker_experts": python_docker_experts
            }

            self._generate_statistics_report(analysis_result)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Skills"))

            return analysis_result

        except Exception as e:
            error_message = LogMessages.ANALYSIS_ERROR.format("Skills", str(e))
            self.logger.error(error_message)
            raise e

    def _build_skill_matrix(self):
        """
        @brief Build a human-readable skill matrix: employees vs technologies
        Uses '+' for skill present, '-' for absent.
        
        @return DataFrame with 'full_name' as first column, then skill columns with '+'/'-'
        """
        self.logger.info(LogMessages.SKILL_MATRIX_BUILDING)

        if self.po_employee_dataframe.empty:
            return pd.DataFrame()

        all_skills = set()
        for skills in self.po_employee_dataframe['skills']:
            if isinstance(skills, list):
                all_skills.update(skills)
        
        if not all_skills:
            return pd.DataFrame()

        all_skills = sorted(all_skills)

        matrix_rows = []
        for _, emp in self.po_employee_dataframe.iterrows():
            full_name = emp['full_name']
            skill_set = set(emp['skills']) if isinstance(emp['skills'], list) else set()
            row = {'ФИО': full_name}
            for skill in all_skills:
                row[skill] = '+' if skill in skill_set else '-'
            matrix_rows.append(row)

        return pd.DataFrame(matrix_rows)

    def _analyze_skill_demand(self):
        """
        @brief Analyze skill popularity: most common and rarest skills
        Counts how many employees have each skill.

        @return Dictionary with 'most_in_demand' and 'rare_skills' lists
        """
        self.logger.info(LogMessages.SKILL_DEMAND_ANALYSIS)

        if self.po_employee_dataframe.empty:
            return {"most_in_demand": [], "rare_skills": []}

        all_skills = []
        for skills in self.po_employee_dataframe['skills']:
            if isinstance(skills, list):
                all_skills.extend(skills)

        skill_counts = pd.Series(all_skills).value_counts()

        most_in_demand = skill_counts.head(5).index.tolist()

        rare_skills = skill_counts[skill_counts <= 1].index.tolist()

        return {
            "most_in_demand": most_in_demand,
            "rare_skills": rare_skills,
            "skill_counts": skill_counts.to_dict()
        }

    def _find_python_docker_experts(self):
        """
        @brief Find employees who know both Python and Docker
        Case-insensitive search in skill lists.

        @return DataFrame with matching employees
        """
        self.logger.info(LogMessages.PYTHON_DOCKER_EXPERTS_SEARCH)

        required = {'python', 'docker'}
        experts = []

        for _, emp in self.po_employee_dataframe.iterrows():
            skills = emp['skills']
            if not isinstance(skills, list):
                continue
            skill_set = {s.lower() for s in skills}
            if required.issubset(skill_set):
                experts.append({
                    'employee_id': emp['employee_id'],
                    'full_name': emp['full_name'],
                    'position': emp['position'],
                    'skills': ', '.join(skills)
                })

        return pd.DataFrame(experts) if experts else pd.DataFrame()

    def _generate_statistics_report(self, analysis_results):
        """
        @brief Generate formatted skills analysis report with skill matrix
        """
        print("=" * 70)
        print(ReportMessages.SKILLS_HEADER)
        print("=" * 70)

        print(f"\n{ReportMessages.TOTAL_EMPLOYEES_SKILLS.format(analysis_results['total_employees'])}")

        skill_matrix = analysis_results['skill_matrix']
        if not skill_matrix.empty:
            print(f"\n{ReportMessages.SKILL_MATRIX_HEADER}")
            print(skill_matrix.to_string(index=False))
        else:
            print("\nNo skill data available.")

        print(f"\n{ReportMessages.MOST_IN_DEMAND_SKILLS}")
        for i, skill in enumerate(analysis_results['skill_statistics']['most_in_demand'], 1):
            print(f"  {i}. {skill}")

        print(f"\n{ReportMessages.RARE_SKILLS}")
        rare = analysis_results['skill_statistics']['rare_skills']
        if rare:
            for skill in rare:
                print(f"  • {skill}")
        else:
            print("  No rare skills found.")

        experts = analysis_results['python_docker_experts']
        print(f"\n{ReportMessages.PYTHON_DOCKER_EXPERTS_COUNT.format(len(experts))}")
        if not experts.empty:
            print(experts[['full_name', 'position']].to_string(index=False))
        else:
            print("  No employees found with both Python and Docker skills.")