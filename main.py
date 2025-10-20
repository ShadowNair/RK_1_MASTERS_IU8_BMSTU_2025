"""
@brief Main execution script for IT Infrastructure Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
from anlyzers.basic_statistics import BasicStaticAnalayzer
from anlyzers.finance_analize import FinanceAnalayzer
from anlyzers.project_analyze import ProjectAnalayzer
from anlyzers.skills_analyzer import SkillsAnalayzer
from anlyzers.recomendation_analyze import RecommendationsAnalayzer
from config.messages import LogMessages, ReportMessages

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
        
        # Verify file exists before initializing analyzers
        self._verify_data_file_exists()

        # Initialize analyzer instances
        self.basic_static_analysis_module = BasicStaticAnalayzer(json_data_file_path)
        self.finance_analize_module = FinanceAnalayzer(json_data_file_path)
        self.project_analize_module = ProjectAnalayzer(json_data_file_path)
        self.skills_analize_module = SkillsAnalayzer(json_data_file_path)
        self.recomendation_analuze_module = RecommendationsAnalayzer(json_data_file_path)

    def _verify_data_file_exists(self):
        """
        @brief Verify that the data file exists before analysis
        Provides clear error message if file is not found
        """
        if not os.path.exists(self.json_data_file_path):
            error_message = f"Data file not found: {self.json_data_file_path}"
            print(f"ERROR: {error_message}")
            print("Please ensure the JSON data file exists in the specified path")
            raise FileNotFoundError(error_message)

    def execute_comprehensive_analysis(self):
        """
        @brief Execute complete PO infrastructure analysis
        Runs all analysis modules and compiles comprehensive results

        @return: Dictionary containing all analysis results
        """
        print("INITIATING COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS")
        print("=" * 70)

        try:
            # Execute all analysis modules
            print("\nEXECUTING EMPLOYEES STATIC ANALYSIS...")
            basic_static_analysis_results = self.basic_static_analysis_module.execute_analysis()
            self.analysis_results_collection['basic_static'] = basic_static_analysis_results

            print("\nEXECUTING FINANCE ANALYSIS...")
            finance_analysis_results = self.finance_analize_module.execute_analysis()
            self.analysis_results_collection['finance'] = finance_analysis_results

            print("\nEXECUTING PROJECT ANALYSIS...")
            project_analysis_results = self.project_analize_module.execute_analysis()
            self.analysis_results_collection['project'] = project_analysis_results

            print("\nEXECUTING SKILLS ANALYSIS...")
            skills_analysis_results = self.skills_analize_module.execute_analysis()
            self.analysis_results_collection['skills'] = skills_analysis_results

            print("\nGENERATING STRATEGIC RECOMMENDATIONS...")
            recommendation_analysis_results = self.recomendation_analuze_module.execute_analysis(basic_static_analysis_results,finance_analysis_results,skills_analysis_results)
            self.analysis_results_collection['recommendation'] = recommendation_analysis_results

            # Generate final comprehensive report
            self._generate_comprehensive_summary_report()

            return self.analysis_results_collection

        except Exception as comprehensive_analysis_error:
            print(f"\nCOMPREHENSIVE ANALYSIS FAILED: {str(comprehensive_analysis_error)}")
            raise comprehensive_analysis_error

    def _generate_comprehensive_summary_report(self):
        """
        @brief Generate final comprehensive summary report
        Compiles key findings and recommendations from all analyses
        """
        print("\n" + "=" * 70)
        print("COMPREHENSIVE PO INFRASTRUCTURE ANALYSIS SUMMARY")
        print("=" * 70)

        #Employee Statistics
        basic = self.analysis_results_collection['basic_static']
        print(f"\nEMPLOYEE OVERVIEW:")
        print(f"• Total Employees: {basic['total_employee_count']}")
        print(f"• High Performers (>90%): {len(basic['high_performers'])}")
        print(f"• Avg. Salary: {basic["average_parameters"]["avarage_salary"]:,.0f} RUB")
        print(f"• Avg. Performance: {basic["average_parameters"]["avarage_perfomance"]:.1f}%")
        print(f"• Avg. Experience: {basic["average_parameters"]["avarage_experience"]:.1f} years")

        # Position distribution
        pos_dist = basic['distribution_position']
        print("\nPOSITION DISTRIBUTION:")
        for _, row in pos_dist.iterrows():
            print(f"• {row['Category']}: {row['Count']} ({row['Percentage']}%)")

        #Finance
        finance = self.analysis_results_collection['finance']
        budget_info = finance["distribution_position"]
        print(f"\nFINANCIAL METRICS:")
        print(f"• Total FOT (Payroll): {budget_info['total_fot']:,.0f} RUB")
        print(f"• Department Budget: {budget_info['department_budget']:,.0f} RUB")
        print(f"• Budget Utilization: {budget_info['budget_utilization_percent']}%")

        print(f"\nTOP 5 HIGHEST SALARIES:")
        print(finance['top_salary'].to_string(index=False))

        #Project Analysis
        project = self.analysis_results_collection['project']
        top_proj = project['top_project']

        print(f"\nPROJECT METRICS:")
        print(f"• Total Projects: {project['total_projects']}")
        print(f"• Average ROI: {project['average_ROI_project']:.2f}%")

        print(f"\nPROJECT STATUS DISTRIBUTION:")
        print(project['status_project'].to_string(index=False))

        print(f"\nMOST PROFITABLE PROJECT:")
        if top_proj is not None:
            print(f"• ID: {top_proj['project_id']}")
            print(f"• Name: {top_proj['name']}")
            print(f"• Status: {top_proj['status']}")
            print(f"• Profit: {top_proj['profit']:,.0f} RUB")
            print(f"• Description: {top_proj['description']}")
        else:
            print("• No projects found.")

        #Skills
        skills = self.analysis_results_collection['skills']
        print(f"\nSKILLS OVERVIEW:")
        print(f"• Total Employees: {skills['total_employees']}")
        print(f"• Python + Docker Experts: {len(skills['python_docker_experts'])}")

        #Recommendations
        recommendations = self.analysis_results_collection['recommendation']
        print(f"\nSTRATEGIC RECOMMENDATIONS:")

        print(f"\nMeasures to Improve Efficiency:")
        for i, measure in enumerate(recommendations['efficiency_measures'], 1):
            print(f"  {i}. {measure}")

        print(f"\nTraining Needs:")
        for i, need in enumerate(recommendations['training_needs'], 1):
            print(f"  {i}. {need}")

        impact = recommendations['productivity_impact']
        print(f"\nPotential Impact of +10% Productivity:")
        if 'fot_savings_potential' in impact:
            print(f"  • Estimated FOT savings: {impact['fot_savings_potential']:,.0f} RUB")
            print(f"  • Assumption: {impact['assumption']}")
        else:
            print("  • Insufficient data for impact calculation.")

def main():
    """
    @brief Main execution function for IT Infrastructure Analysis
    Handles command line arguments and orchestrates analysis execution
    """
    # Configuration - update this path to match your JSON file
    company_data_json_file_path = "company.json"  # Changed from company_data_detailed.json

    try:
        # Initialize and execute analysis
        analysis_orchestrator = POInfrastructureAnalysisOrchestrator(company_data_json_file_path)
        analysis_orchestrator.execute_comprehensive_analysis()

        print(f"\nANALYSIS COMPLETED SUCCESSFULLY!")
        print(f"Log files generated in 'logs/' directory")

    except FileNotFoundError as file_error:
        print(f"\nFILE ERROR: {str(file_error)}")
        print("Please check the file path and ensure the JSON file exists")
        sys.exit(1)
    except Exception as main_execution_error:
        print(f"\nCRITICAL ERROR DURING ANALYSIS EXECUTION: {str(main_execution_error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()