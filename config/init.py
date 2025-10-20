"""
@brief Configuration package for IT infrastructure analysis
Contains enums and message templates for system configuration
"""

from .messages import LogMessages, ReportMessages, ErrorMessages

__all__ = [
    'LogMessages',
    'ReportMessages',
    'ErrorMessages'
]