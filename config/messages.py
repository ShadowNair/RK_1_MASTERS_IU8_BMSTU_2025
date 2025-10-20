"""
@brief Message templates for IT Infrastructure Analysis
Contains all user-facing messages and logging templates
"""

class LogMessages:
    """
    @brief Log message templates for analysis operations
    Standardized messages for different logging levels and operations
    """


    # Project analysis messages
    PROJECT_STATUS_ANALYSIS = "Analyzing project status distribution"
    PROJECT_ROI_CALCULATION = "Calculating average ROI for all projects"
    TOP_PROFIT_PROJECT_IDENTIFICATION = "Identifying project with highest profit"

    # Orchestrator
    ORCHESTRATOR_INIT = "Orchestrator initialized with data file: {}"
    DATA_FILE_VERIFIED = "Data file verification successful"
    ANALYSIS_START = "Comprehensive {} analysis started"
    ANALYSIS_COMPLETE = "Comprehensive {} analysis completed successfully"
    ANALYSIS_MODULE_START = "{} analysis module execution started"
    ANALYSIS_MODULE_SUCCESS = "{} analysis module executed successfully"
    GENERATING_SUMMARY_REPORT = "Generating comprehensive summary report"
    SUMMARY_REPORT_SAVED = "Summary report saved to logs/analysis_summary.txt"
    
    # PDF Generator
    PDF_GENERATION_STARTED = "PDF report generation started"
    PDF_PAGE_ADDED = "{} page added to PDF"
    PDF_SAVED = "PDF report saved successfully to {}"
    PDF_GENERATION_ERROR = "Error during PDF generation: {}"
    TEMP_FILES_CLEANED = "Temporary chart files cleaned up"
    
    # Errors
    FILE_NOT_FOUND = "Data file not found: {}"
    ANALYSIS_ERROR = "Error during {} analysis: {}"
    MAIN_EXECUTION_ERROR = "Critical error in main execution: {}"


    # System initialization messages
    SYSTEM_START = "Software Infrastructure Analysis System initialization started"
    SYSTEM_READY = "Software Infrastructure Analysis System ready"
    DATA_LOAD_START = "Starting data loading process from JSON file"
    DATA_LOAD_SUCCESS = "Data successfully loaded from file: {}"
    DATA_LOAD_ERROR = "Error loading data from file: {} - {}"
    START_CREATE_DATAFRAME = "Start create dataframe {}"
    SUCCESS_CREATE_DATAFRAME = "Success create dataframe {}"
    ERROR_CREATE_DATAFRAME = "Erro create dataframe {} - {}"

    # Recommendations analysis messages
    EFFICIENCY_RECOMMENDATIONS = "Generating efficiency improvement recommendations"
    TRAINING_NEEDS_IDENTIFICATION = "Identifying employee training needs"
    PRODUCTIVITY_IMPACT_CALCULATION = "Calculating financial impact of productivity increase"

    # Skills analysis messages
    SKILL_MATRIX_BUILDING = "Building employee skill matrix"
    SKILL_DEMAND_ANALYSIS = "Analyzing skill demand and rarity"
    PYTHON_DOCKER_EXPERTS_SEARCH = "Searching for Python + Docker experts"

    # Analysis process messages
    ANALYSIS_START = "Starting {} analysis"
    ANALYSIS_COMPLETE = "{} analysis completed successfully"
    ANALYSIS_ERROR = "Error during {} analysis: {}"

    # Data processing messages
    DATA_PROCESSING_START = "Starting data processing for {}"
    DATA_FILTERING_START = "Filtering Software equipment from dataset"
    DATA_TRANSFORMATION_START = "Starting data transformation"

    # Finance analysis messages
    EFOT_CALCULATION_START = "Calculating Fund of Wages (FOT) for all employees"
    BUDGET_COMPARISON_START = "Comparing FOT with department budget"
    TOP_SALARIES_RETRIEVAL = "Retrieving top 5 highest salaries"

    # Employees analisis messages
    EMPLOYEE_PARAMETR_CALCULATION = "Calculating avarage parametrs"
    EMPLOYEE_WORK_LEVEL = "Count Junior/Middle/Senior/TeamLead level"
    EMPLOYEE_PERFOMANCE = "Define employees with perfomance_score > 90"
    EMPLOYEE_CATEGORY = "Create column for category employee from position"

class ReportMessages:
    """
    @brief Report message templates for analysis results
    Standardized output messages for different analysis sections
    """

    # Project report messages
    PROJECT_HEADER = "PO DEPARTMENT PROJECT ANALYSIS"

    TOTAL_PROJECTS = "Total projects analyzed: {}"
    AVERAGE_ROI = "Average ROI across projects: {:.2f}"
    PROJECT_STATUS_DISTRIBUTION = "Project Status Distribution:"
    TOP_PROFIT_PROJECT = "Most Profitable Project:"

    # Skills report messages
    SKILLS_HEADER = "EMPLOYEE SKILLS ANALYSIS"
    SKILL_MATRIX_HEADER = "Skill Matrix (+: has skill, -: no skill):"
    TOTAL_EMPLOYEES_SKILLS = "Total employees analyzed for skills: {}"
    MOST_IN_DEMAND_SKILLS = "Most In-Demand Skills (Top 5):"
    RARE_SKILLS = "Rare Skills (≤1 employee):"
    PYTHON_DOCKER_EXPERTS_COUNT = "Employees with Python and Docker: {}"

    # Section headers
    INVENTORY_HEADER = "EQUIPMENT INVENTORY ANALYSIS"
    UTILIZATION_HEADER = "EQUIPMENT UTILIZATION ANALYSIS"
    COST_HEADER = "COST ANALYSIS"
    REPLACEMENT_HEADER = "EQUIPMENT REPLACEMENT PLANNING"
    OPTIMIZATION_HEADER = "INFRASTRUCTURE OPTIMIZATION"
    STATIC_HEADER = "EMPLOYEE BASIC STATIC ANALYSIS"

    # Recommendations report messages
    RECOMMENDATIONS_HEADER = "STRATEGIC RECOMMENDATIONS FOR PO DEPARTMENT"

    EFFICIENCY_MEASURES_HEADER = "Measures to Improve Department Efficiency:"
    TRAINING_NEEDS_HEADER = "Identified Training Needs:"
    PRODUCTIVITY_IMPACT_HEADER = "Potential Impact of +10% Productivity:"

    # Results messages
    AVERAGE_UTILIZATION = "Average equipment utilization rate: {:.1f}%"
    ANNUAL_MAINTENANCE_COST = "Annual maintenance costs: {:,.0f}"
    TOP_EMPLOYEE_COUNT = "Count employees with performance > 90%: {} employees"

    # Finance report headers and messages
    FINANCE_HEADER = "FINANCE DEPARTMENT ANALYSIS"

    TOTAL_EMPLOYEES = "Total PO employees: {}"
    FOT_TOTAL = "Total Fund of Wages (FOT): {:,.0f}"
    BUDGET_ALLOCATED = "Department budget allocated: {:,.0f}"
    BUDGET_UTILIZATION = "Budget utilization: {:.2f}"

    TOP_SALARIES_HEADER = "Top 5 Highest Salaries:"

    # Recommendation messages
    CONSOLIDATION_RECOMMENDATION = "Recommended consolidation measures"
    COST_SAVINGS_POTENTIAL = "Potential annual savings: {:,.0f} RUB"
    REPLACEMENT_PRIORITY = "Equipment replacement priority list generated"

class ErrorMessages:
    """
    @brief Error message templates
    Standardized error messages for exception handling
    """

    FILE_NOT_FOUND = "Configuration file not found: {}"
    INVALID_JSON = "Invalid JSON format in file: {}"
    DATA_VALIDATION_ERROR = "Data validation error: {}"
    CALCULATION_ERROR = "Calculation error in {}: {}"