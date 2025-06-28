# File: task4_advanced_api.py
import requests
import time


class IndonesianDataCollector:
    def safe_api_call(self, url, max_retries=3):
        """API call with exponential backoff"""
        # TODO: Implement retry logic with delays
        pass

    def get_regional_data(self):
        """Collect provinces and cities data"""
        pass

    def get_economic_indicators(self):
        """Simulated economic data (GDP, inflation, exchange rate)"""
        pass

    def integrate_all_data(self):
        """Combine data from multiple sources"""
        pass

# TODO: Collect from 3+ sources, generate JSON/CSV reports