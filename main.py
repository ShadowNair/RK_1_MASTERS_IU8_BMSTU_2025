"""
@brief Main execution script for IT Infrastructure Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
import tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

from utils.logger import analysis_logger
from anlyzers.basic_statistics import BasicStaticAnalayzer
from anlyzers.finance_analize import FinanceAnalayzer
from anlyzers.project_analyze import ProjectAnalayzer
from anlyzers.skills_analyzer import SkillsAnalayzer
from anlyzers.recomendation_analyze import RecommendationsAnalayzer
from config.messages import LogMessages, ReportMessages
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import XPos, YPos

class POInfrastructureAnalysisOrchestrator:
    """
    @brief Main orchestrator for PO infrastructure analysis system
    Coordinates execution of all analysis modules and compiles results
    """
    
    def __init__(self, json_data_file_path):
        """
        @brief Initialize analysis orchestrator with data source
        Sets up all analyzer instances and configuration
        
        @param json_data_file_path: Path to company data JSON file
        """
        self.json_data_file_path = json_data_file_path
        self.analysis_results_collection = {}
        self.logger = analysis_logger.get_analysis_logger("POInfrastructureAnalysisOrchestrator")

        self.logger.info(LogMessages.ORCHESTRATOR_INIT.format(json_data_file_path))
        
        # Verify file exists before initializing analyzers
        self._verify_data_file_exists()

        # Initialize analyzer instances
        self.basic_static_analysis_module = BasicStaticAnalayzer(json_data_file_path)
        self.finance_analize_module = FinanceAnalayzer(json_data_file_path)
        self.project_analize_module = ProjectAnalayzer(json_data_file_path)
        self.skills_analize_module = SkillsAnalayzer(json_data_file_path)
        self.recomendation_analuze_module = RecommendationsAnalayzer(json_data_file_path)

        self.logger.info(LogMessages.DATA_FILE_VERIFIED)

    def _verify_data_file_exists(self):
        """
        @brief Verify that the data file exists before analysis
        Provides clear error message if file is not found
        """
        if not os.path.exists(self.json_data_file_path):
            error_msg = LogMessages.FILE_NOT_FOUND.format(self.json_data_file_path)
            self.logger.error(error_msg)
            raise FileNotFoundError(error_msg)

    def execute_comprehensive_analysis(self):
        """
        @brief Execute complete PO infrastructure analysis
        Runs all analysis modules and compiles comprehensive results

        @return: Dictionary containing all analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("comprehensive PO infrastructure"))
        print("INITIATING COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS")
        print("=" * 70)

        try:
            # Execute all analysis modules
            self.logger.info(LogMessages.ANALYSIS_MODULE_START.format("Employee Static"))
            print("\nEXECUTING EMPLOYEES STATIC ANALYSIS...")
            basic_static_analysis_results = self.basic_static_analysis_module.execute_analysis()
            self.analysis_results_collection['basic_static'] = basic_static_analysis_results
            self.logger.info(LogMessages.ANALYSIS_MODULE_SUCCESS.format("Employee Static"))

            self.logger.info(LogMessages.ANALYSIS_MODULE_START.format("Finance"))
            print("\nEXECUTING FINANCE ANALYSIS...")
            finance_analysis_results = self.finance_analize_module.execute_analysis()
            self.analysis_results_collection['finance'] = finance_analysis_results
            self.logger.info(LogMessages.ANALYSIS_MODULE_SUCCESS.format("Finance"))

            self.logger.info(LogMessages.ANALYSIS_MODULE_START.format("Project"))
            print("\nEXECUTING PROJECT ANALYSIS...")
            project_analysis_results = self.project_analize_module.execute_analysis()
            self.analysis_results_collection['project'] = project_analysis_results
            self.logger.info(LogMessages.ANALYSIS_MODULE_SUCCESS.format("Project"))

            self.logger.info(LogMessages.ANALYSIS_MODULE_START.format("Skills"))
            print("\nEXECUTING SKILLS ANALYSIS...")
            skills_analysis_results = self.skills_analize_module.execute_analysis()
            self.analysis_results_collection['skills'] = skills_analysis_results
            self.logger.info(LogMessages.ANALYSIS_MODULE_SUCCESS.format("Skills"))

            self.logger.info(LogMessages.ANALYSIS_MODULE_START.format("Strategic Recommendations"))
            print("\nGENERATING STRATEGIC RECOMMENDATIONS...")
            recommendation_analysis_results = self.recomendation_analuze_module.execute_analysis(basic_static_analysis_results,finance_analysis_results,skills_analysis_results)
            self.analysis_results_collection['recommendation'] = recommendation_analysis_results
            self.logger.info(LogMessages.ANALYSIS_MODULE_SUCCESS.format("Strategic Recommendations"))

            # Generate final comprehensive report
            self.logger.info(LogMessages.GENERATING_SUMMARY_REPORT)
            summary_text = self._generate_comprehensive_summary_report()
            self.analysis_results_collection['summary_text'] = summary_text
            self.logger.info(LogMessages.SUMMARY_REPORT_SAVED)

            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Comprehensive PO Infrastructure"))
            return self.analysis_results_collection

        except Exception as comprehensive_analysis_error:
            self.logger.error(LogMessages.ANALYSIS_ERROR.format("comprehensive", str(comprehensive_analysis_error)))
            print(f"\nCOMPREHENSIVE ANALYSIS FAILED: {str(comprehensive_analysis_error)}")
            raise comprehensive_analysis_error

    def _generate_comprehensive_summary_report(self):
        """
        @brief Generate final comprehensive summary report as a string
        Compiles key findings and recommendations from all analyses
        """
        report_lines = []
        report_lines.append("=" * 70)
        report_lines.append("COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS SUMMARY")
        report_lines.append("=" * 70)

        # Employee Statistics
        basic = self.analysis_results_collection['basic_static']
        report_lines.append("\nEMPLOYEE OVERVIEW:")
        report_lines.append(f"• Total Employees: {basic['total_employee_count']}")
        report_lines.append(f"• High Performers (>90%): {len(basic['high_performers'])}")
        report_lines.append(f"• Avg. Salary: {basic['average_parameters']['avarage_salary']:,.0f} RUB")
        report_lines.append(f"• Avg. Performance: {basic['average_parameters']['avarage_perfomance']:.1f}%")
        report_lines.append(f"• Avg. Experience: {basic['average_parameters']['avarage_experience']:.1f} years")

        # Position distribution
        pos_dist = basic['distribution_position']
        report_lines.append("\nPOSITION DISTRIBUTION:")
        for _, row in pos_dist.iterrows():
            report_lines.append(f"• {row['Category']}: {row['Count']} ({row['Percentage']}%)")

        # Finance
        finance = self.analysis_results_collection['finance']
        budget_info = finance["distribution_position"]
        report_lines.append(f"\nFINANCIAL METRICS:")
        report_lines.append(f"• Total FOT (Payroll): {budget_info['total_fot']:,.0f} RUB")
        report_lines.append(f"• Department Budget: {budget_info['department_budget']:,.0f} RUB")
        report_lines.append(f"• Budget Utilization: {budget_info['budget_utilization_percent']}%")

        report_lines.append(f"\nTOP 5 HIGHEST SALARIES:")
        report_lines.append(finance['top_salary'].to_string(index=False))

        # Project Analysis
        project = self.analysis_results_collection['project']
        top_proj = project['top_project']
        report_lines.append(f"\nPROJECT METRICS:")
        report_lines.append(f"• Total Projects: {project['total_projects']}")
        report_lines.append(f"• Average ROI: {project['average_ROI_project']:.2f}%")

        report_lines.append(f"\nPROJECT STATUS DISTRIBUTION:")
        report_lines.append(project['status_project'].to_string(index=False))

        report_lines.append(f"\nMOST PROFITABLE PROJECT:")
        if top_proj is not None:
            report_lines.append(f"• ID: {top_proj['project_id']}")
            report_lines.append(f"• Name: {top_proj['name']}")
            report_lines.append(f"• Status: {top_proj['status']}")
            report_lines.append(f"• Profit: {top_proj['profit']:,.0f} RUB")
            report_lines.append(f"• Description: {top_proj['description']}")
        else:
            report_lines.append("• No projects found.")

        # Skills
        skills = self.analysis_results_collection['skills']
        report_lines.append(f"\nSKILLS OVERVIEW:")
        report_lines.append(f"• Total Employees: {skills['total_employees']}")
        report_lines.append(f"• Python + Docker Experts: {len(skills['python_docker_experts'])}")

        # Recommendations
        recommendations = self.analysis_results_collection['recommendation']
        report_lines.append(f"\nSTRATEGIC RECOMMENDATIONS:")

        report_lines.append(f"\nMeasures to Improve Efficiency:")
        for i, measure in enumerate(recommendations['efficiency_measures'], 1):
            report_lines.append(f"  {i}. {measure}")

        report_lines.append(f"\nTraining Needs:")
        for i, need in enumerate(recommendations['training_needs'], 1):
            report_lines.append(f"  {i}. {need}")

        impact = recommendations['productivity_impact']
        report_lines.append(f"\nPotential Impact of +10% Productivity:")
        if 'fot_savings_potential' in impact:
            report_lines.append(f"  • Estimated FOT savings: {impact['fot_savings_potential']:,.0f} RUB")
            report_lines.append(f"  • Assumption: {impact['assumption']}")
        else:
            report_lines.append("  • Insufficient data for impact calculation.")

        full_report = "\n".join(report_lines)
        
        print(full_report)
        
        with open("logs/analysis_summary.txt", "w", encoding="utf-8") as f:
            f.write(full_report)
        
        return full_report

class PDFReportGenerator:
    """
    @brief Generates a professional PDF report with charts and analysis summary.
    """

    def __init__(self, analysis_results, employee_df, project_df):
        """
        @brief Initialize this function. Need results analyzers

        @param analysis_results: results analysis
        @param employee_df: Dataframe employees with data
        @param project_df: Dataframe projects data
        """
        self.analysis_results = analysis_results
        self.employee_df = employee_df
        self.logger = analysis_logger.get_analysis_logger("PDFReportGenerator")
        self.project_df = project_df
        
        self.pdf = FPDF()
        self.pdf.add_font("DejaVu", "", "DejaVuSans.ttf")
        self.pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf")
        
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.temp_files = []

    def _create_temp_file(self, suffix=".png"):
        """
        @brief Create a temporary file for chart.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
            path = f.name
        self.temp_files.append(path)
        return path

    def _add_page_with_title(self, title):
        """
        @brief Generate new page PDF with title

        @param title: How you wont named this page
        """
        self.pdf.add_page()
        self.pdf.set_font("DejaVu", "B", 30) 
        x_pos = 1
        self.pdf.set_x(x_pos)
        self.pdf.cell(0, 10, title, ln=True, align="C")
        self.pdf.ln(10)

    def _add_chart(self, fig, title, hight):
        """
        @brief Create image in PDF

        @param fig: Your image, whish you use
        @param title: Name this image
        @param hight: Hight this image
        """
        temp_path = self._create_temp_file()
        fig.savefig(temp_path, bbox_inches="tight", dpi=150)
        plt.close(fig)

        self.pdf.set_font("DejaVu", "B", 9)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.ln(2)
        self.pdf.image(temp_path,h= hight, w=180)
        self.pdf.ln(10)

    def generate_summary_analysis(self):
        """
        @brief Generate print from terminal in PDF
        """
        self._add_page_with_title("0. Executive Summary (Text)")
        self.pdf.set_font("DejaVu", size=12)
        
        summary = self.analysis_results['summary_text']
        for line in summary.split("\n"):
            self.pdf.multi_cell(0, 5, line)
            self.pdf.ln(1)
        self.logger.info(LogMessages.PDF_PAGE_ADDED.format("Executive Summary"))

    def generate_basic_statistics_charts(self):
        """
        @brief Generate charts for Basic Statistics.
        """
        self._add_page_with_title("1. Employee Statistics")

        # Grafic experience, performance, salary
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        params = [
            ("Experience (years)", "experience_years"),
            ("Performance (%)", "performance_score"),
            ("Salary (RUB)", "salary")
        ]
        for ax, (label, col) in zip(axes, params):
            data = self.employee_df[col].dropna()
            ax.hist(data, bins=15, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {label}")
            ax.set_xlabel(label)
            ax.set_ylabel("Frequency")
        self._add_chart(fig, "Distributions: Experience, Performance, Salary", 60)

        # Grafic work level
        pos_dist = self.analysis_results['basic_static']['distribution_position']
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(pos_dist['Count'], labels=pos_dist['Category'], autopct='%1.1f%%', startangle=90)
        ax.set_title("Position Distribution")
        self._add_chart(fig, "Position Distribution (Junior/Middle/Senior/TeamLead)", 120)
        self.logger.info(LogMessages.PDF_PAGE_ADDED.format("Employee Statistics"))

    def generate_finance_charts(self):
        """
        @brief Generate charts for Finance.
        """
        self._add_page_with_title("2. Financial Analysis")

        # Grafic FOT budget
        finance = self.analysis_results['finance']
        budget_info = finance["distribution_position"]
        fot = budget_info['total_fot']
        budget = budget_info['department_budget']
        if fot > budget:
            sizes = [budget, fot - budget]
            labels = ['Remaining Budget' ,'FOT (exceeds budget)']
            colors = ['#ff9999', '#66b3ff']
        else:
            sizes = [fot, budget - fot]
            labels = ['FOT', 'Remaining Budget']
            colors = ['#ff9999', '#66b3ff']
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.set_title("Budget Utilization")

        self._add_chart(fig, "Department Budget Allocation", 120)

        # Grafic top 5 employees
        top5 = finance['top_salary']
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(top5['full_name'], top5['salary'], color='green')
        ax.set_xlabel("Salary (RUB)")
        ax.set_title("Top 5 Highest Salaries")
        ax.ticklabel_format(style='plain', axis='x')
        self._add_chart(fig, "Top 5 Highest Paid Employees", 80)
        self.logger.info(LogMessages.PDF_PAGE_ADDED.format("Financial Analysis"))

    def generate_project_charts(self):
        """
        @brief Generate charts for Projects.
        """
        self._add_page_with_title("3. Project Analysis")

        # Grafic status project
        project = self.analysis_results['project']
        status_df = project['status_project']
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(status_df['Count'], labels=status_df['Status'], autopct='%1.1f%%', startangle=90)
        ax.set_title("Project Status Distribution")
        self._add_chart(fig, "Project Status: Active vs Closed", 120)

        # roi
        if not self.project_df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            roi_data = self.project_df['roi_percentage'].dropna()
            ax.hist(roi_data, bins=15, color='orange', edgecolor='black')
            ax.set_title("Distribution of Project ROI (%)")
            ax.set_xlabel("ROI (%)")
            ax.set_ylabel("Number of Projects")
            self._add_chart(fig, "ROI Distribution Across Projects", 80)
        self.logger.info(LogMessages.PDF_PAGE_ADDED.format("Project Analysis"))

    def generate_recommendations_page(self):
        """
        @brief Generate reccommendation in PDF
        """
        self._add_page_with_title("4. Strategic Recommendations")
        rec = self.analysis_results['recommendation']

        self.pdf.set_font("DejaVu", "B", 10)
        self.pdf.cell(0, 10, "Efficiency Improvement Measures:", ln=True)
        self.pdf.set_font("DejaVu", size=8)
        for measure in rec['efficiency_measures']:
            self.pdf.multi_cell(0, 6, f"• {measure}")
        self.pdf.ln(5)

        self.pdf.set_font("DejaVu", "B", 10)
        self.pdf.cell(0, 10, "Training Needs:", ln=True)
        self.pdf.set_font("DejaVu", size=8)
        for need in rec['training_needs']:
            self.pdf.multi_cell(0, 6, f"• {need}")
        self.pdf.ln(5)

        self.pdf.set_font("DejaVu", "B", 10)
        self.pdf.cell(0, 10, "Productivity Impact (+10%):", ln=True)
        self.pdf.set_font("DejaVu", size=8)
        impact = rec['productivity_impact']
        if 'fot_savings_potential' in impact:
            self.pdf.cell(0, 6, f"• Estimated FOT savings: {impact['fot_savings_potential']:,.0f} RUB")
        else:
            self.pdf.multi_cell(0, 6, "• Insufficient data for impact calculation.")
        self.logger.info(LogMessages.PDF_PAGE_ADDED.format("Strategic Recommendations"))

    def save_pdf(self, output_path="PO_Analysis_Report.pdf"):
        """
        @brief Save this beatifully PDF
        """
        try:
            self.pdf.add_page()
            self.pdf.set_font("DejaVu", size=30)
            title = "PO Department Analysis Report"
            title_width = self.pdf.get_string_width(title)
            x_pos = (self.pdf.w - title_width) / 2
            self.pdf.set_x(x_pos)
            self.pdf.cell(0, 30, title, ln=True)

            self.pdf.set_font("DejaVu", size=10)
            subtitle = "Comprehensive analysis of employees, finances, projects, and skills"
            subtitle_width = self.pdf.get_string_width(subtitle)
            x_pos = (self.pdf.w - subtitle_width) / 2
            self.pdf.set_x(x_pos)
            self.pdf.cell(0, 10, subtitle, ln=True)

            self.pdf.ln(10)
            date_str = f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}"
            date_width = self.pdf.get_string_width(date_str)
            x_pos = (self.pdf.w - date_width) / 2
            self.pdf.set_x(x_pos)
            self.pdf.cell(0, 10, date_str, ln=True)

            self.pdf.ln(20)

            # All generation
            self.generate_summary_analysis()
            self.generate_basic_statistics_charts()
            self.generate_finance_charts()
            self.generate_project_charts()
            self.generate_recommendations_page()

            self.pdf.output(output_path)
            self.logger.info(LogMessages.PDF_SAVED.format(output_path))
            print(f"\nPDF report saved as: {output_path}")

        finally:
            for path in self.temp_files:
                if os.path.exists(path):
                    os.remove(path)
            self.logger.info(LogMessages.TEMP_FILES_CLEANED)

def main():
    """
    @brief Main execution function for IT Infrastructure Analysis
    Handles command line arguments and orchestrates analysis execution
    """
    # Configuration - update this path to match your JSON file
    logger = analysis_logger.get_analysis_logger("main")
    company_data_json_file_path = "company.json"  # Changed from company_data_detailed.json
    with open("DejaVuSans.ttf", "rb") as f:
        print("Font file readable, size:", len(f.read()))

    try:
        # Initialize and execute analysis
        analysis_orchestrator = POInfrastructureAnalysisOrchestrator(company_data_json_file_path)
        results = analysis_orchestrator.execute_comprehensive_analysis()

        pdf_gen = PDFReportGenerator(
            analysis_results=results,
            employee_df=analysis_orchestrator.basic_static_analysis_module.po_employee_dataframe,
            project_df=analysis_orchestrator.project_analize_module.po_project_dataframe
        )
        pdf_gen.save_pdf("PO_Analysis_Report.pdf")

        print(f"\nANALYSIS COMPLETED SUCCESSFULLY!")
        print(f"Log files generated in 'logs/' directory")

    except FileNotFoundError as file_error:
        logger.error(LogMessages.FILE_NOT_FOUND.format(company_data_json_file_path))
        print(f"\nFILE ERROR: {str(file_error)}")
        print("Please check the file path and ensure the JSON file exists")
        sys.exit(1)
    except Exception as main_execution_error:
        logger.critical(LogMessages.MAIN_EXECUTION_ERROR.format(str(main_execution_error)))
        print(f"\nCRITICAL ERROR DURING ANALYSIS EXECUTION: {str(main_execution_error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()