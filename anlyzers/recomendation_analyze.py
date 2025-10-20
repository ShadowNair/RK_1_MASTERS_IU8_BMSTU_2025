"""
@brief Recommendations analysis module
Generates actionable insights to improve PO department efficiency,
identifies training needs, and estimates financial impact of
productivity improvements.
"""

import pandas as pd
from anlyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class RecommendationsAnalayzer(BaseAnalyzer):
    """
    @brief Analyzer for strategic recommendations
    Leverages employee, finance, and skills data to propose
    efficiency improvements, training programs, and ROI estimates.
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize Recommendations Analyzer
        """
        super().__init__(json_file_path, "Recommendations")

    def execute_analysis(self, employee_data=None, finance_data=None, skills_data=None):
        """
        @brief Execute recommendations analysis using external data
        Requires results from other analyzers for comprehensive insights.

        @param employee_data: Result from BasicStaticAnalyzer
        @param finance_data: Result from FinanceAnalyzer
        @param skills_data: Result from SkillsAnalyzer
        @return Dictionary with recommendations
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("Recommendations"))

        try:
            efficiency_measures = self._generate_efficiency_recommendations(employee_data)

            training_needs = self._identify_training_needs(skills_data)

            productivity_impact = self._calculate_productivity_impact(finance_data, employee_data)

            analysis_result = {
                "efficiency_measures": efficiency_measures,
                "training_needs": training_needs,
                "productivity_impact": productivity_impact
            }

            self._generate_statistics_report(analysis_result)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Recommendations"))

            return analysis_result

        except Exception as e:
            error_message = LogMessages.ANALYSIS_ERROR.format("Recommendations", str(e))
            self.logger.error(error_message)
            raise e

    def _generate_efficiency_recommendations(self, employee_data):
        """
        @brief Generate efficiency improvement measures
        Based on performance distribution and role balance.
        """
        self.logger.info(LogMessages.EFFICIENCY_RECOMMENDATIONS)

        measures = []

        if employee_data:
            perf_avg = employee_data['average_parameters']['avarage_perfomance']
            high_performers_ratio = len(employee_data['high_performers']) / employee_data['total_employee_count']

            # average < 85 %
            if perf_avg < 85:
                measures.append("Повысить среднюю производительность через менторство и оптимизацию процессов")

            # Smoll count high performance
            if high_performers_ratio < 0.2:
                measures.append("Разработать программу по выявлению и удержанию талантов")

            # Disbalance level work
            pos_dist = employee_data['distribution_position']
            junior_ratio = pos_dist[pos_dist['Category'] == 'junior']['Count'].sum() / employee_data['total_employee_count']
            senior_ratio = pos_dist[pos_dist['Category'] == 'senior']['Count'].sum() / employee_data['total_employee_count']

            if junior_ratio > 0.4 and senior_ratio < 0.2:
                measures.append("Усилить наставничество: назначить менторов для стажёров и junior-специалистов")

        if not measures:
            measures.append("Текущая структура отдела сбалансирована. Рекомендуется поддерживать достигнутый уровень.")

        return measures

    def _identify_training_needs(self, skills_data):
        """
        @brief Identify training needs based on rare/missing critical skills
        """
        self.logger.info(LogMessages.TRAINING_NEEDS_IDENTIFICATION)

        needs = []

        if skills_data:
            rare_skills = skills_data['skill_statistics']['rare_skills']
            critical_skills = {'Docker', 'Kubernetes', 'Python', 'CI/CD', 'Cloud (AWS/Azure/GCP)'}

            missing_critical = [skill for skill in rare_skills if skill in critical_skills]
            if missing_critical:
                needs.append(f"Организовать обучение по дефицитным критическим навыкам: {', '.join(missing_critical)}")

            if len(skills_data['python_docker_experts']) == 0:
                needs.append("Провести кросс-обучение: Python-разработчикам — Docker, DevOps — Python")

        if not needs:
            needs.append("Потребность в массовом обучении не выявлена. Рекомендуется индивидуальное развитие.")

        return needs

    def _calculate_productivity_impact(self, finance_data, employee_data):
        """
        @brief Calculate financial impact of 10% productivity increase
        Assumption: higher productivity → higher project profit margin
        """
        self.logger.info(LogMessages.PRODUCTIVITY_IMPACT_CALCULATION)

        if not finance_data or not employee_data:
            return {"additional_profit": 0, "roi_improvement": 0.0}


        total_fot = finance_data['distribution_position']['total_fot']

        fot_savings = total_fot * 0.09

        return {
            "fot_savings_potential": round(fot_savings, 0),
            "productivity_increase": 10,
            "assumption": "10% рост производительности позволяет снизить фонд оплаты труда на 9% при сохранении объёма работ"
        }

    def _generate_statistics_report(self, analysis_results):
        """
        @brief Generate formatted recommendations report
        """
        print("=" * 70)
        print(ReportMessages.RECOMMENDATIONS_HEADER)
        print("=" * 70)

        # Efficiency Measures
        print(f"\n{ReportMessages.EFFICIENCY_MEASURES_HEADER}")
        for i, measure in enumerate(analysis_results['efficiency_measures'], 1):
            print(f"  {i}. {measure}")

        # Training Needs
        print(f"\n{ReportMessages.TRAINING_NEEDS_HEADER}")
        for i, need in enumerate(analysis_results['training_needs'], 1):
            print(f"  {i}. {need}")

        # Productivity Impact
        impact = analysis_results['productivity_impact']
        print(f"\n{ReportMessages.PRODUCTIVITY_IMPACT_HEADER}")
        if 'fot_savings_potential' in impact:
            print(f"  • Потенциальная экономия ФОТ при росте производительности на {impact['productivity_increase']}%: "
                f"{impact['fot_savings_potential']:,.0f} RUB")
            print(f"  • Допущение: {impact['assumption']}")
        else:
            print("  • Недостаточно данных для расчёта эффекта.")