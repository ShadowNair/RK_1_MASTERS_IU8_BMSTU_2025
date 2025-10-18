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
        self.