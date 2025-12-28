"""
Indicator configuration for CSRD ESG data extraction.

This file defines WHAT the system extracts, not HOW.

Design principles:
- Single source of truth for indicators
- No extraction logic here
- Used by:
  - extraction loop
  - LLM prompt construction
  - page reference mapping
  - database & CSV schema

If indicators change, only this file should need updating.
"""

INDICATORS = [
    # ------------------------------------------------------------------
    # Environmental Indicators (ESRS E1 – Climate Change)
    # ------------------------------------------------------------------
    {
        "name": "Total Scope 1 GHG Emissions",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Direct greenhouse gas emissions from owned or controlled sources.",
        "expected_unit": "tCO2e",
        "value_type": "number",
    },
    {
        "name": "Total Scope 2 GHG Emissions",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Indirect greenhouse gas emissions from the generation of purchased energy.",
        "expected_unit": "tCO2e",
        "value_type": "number",
    },
    {
        "name": "Total Scope 3 GHG Emissions",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "All other indirect greenhouse gas emissions occurring in the value chain.",
        "expected_unit": "tCO2e",
        "value_type": "number",
    },
    {
        "name": "GHG Emissions Intensity",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Greenhouse gas emissions per unit of revenue.",
        "expected_unit": "tCO2e per €M revenue",
        "value_type": "number",
    },
    {
        "name": "Total Energy Consumption",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Total energy consumed by the organization across operations.",
        "expected_unit": "MWh or GJ",
        "value_type": "number",
    },
    {
        "name": "Renewable Energy Percentage",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Percentage of total energy consumption derived from renewable sources.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
    {
        "name": "Net Zero Target Year",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Year by which the organization commits to achieving net zero emissions.",
        "expected_unit": "year",
        "value_type": "year",
    },
    {
        "name": "Green Financing Volume",
        "category": "Environmental",
        "esrs": "E1",
        "definition": "Total volume of financing allocated to green or sustainable activities.",
        "expected_unit": "€ millions",
        "value_type": "number",
    },

    # ------------------------------------------------------------------
    # Social Indicators (ESRS S1 – Own Workforce)
    # ------------------------------------------------------------------
    {
        "name": "Total Employees",
        "category": "Social",
        "esrs": "S1",
        "definition": "Total number of employees, typically expressed as full-time equivalents (FTE).",
        "expected_unit": "FTE",
        "value_type": "number",
    },
    {
        "name": "Female Employees",
        "category": "Social",
        "esrs": "S1",
        "definition": "Percentage of employees who identify as female.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
    {
        "name": "Gender Pay Gap",
        "category": "Social",
        "esrs": "S1",
        "definition": "Difference in average pay between male and female employees.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
    {
        "name": "Training Hours per Employee",
        "category": "Social",
        "esrs": "S1",
        "definition": "Average number of training hours completed per employee during the reporting year.",
        "expected_unit": "hours",
        "value_type": "number",
    },
    {
        "name": "Employee Turnover Rate",
        "category": "Social",
        "esrs": "S1",
        "definition": "Percentage of employees who left the organization during the reporting year.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
    {
        "name": "Work-Related Accidents",
        "category": "Social",
        "esrs": "S1",
        "definition": "Number of work-related accidents recorded during the reporting year.",
        "expected_unit": "count",
        "value_type": "number",
    },
    {
        "name": "Collective Bargaining Coverage",
        "category": "Social",
        "esrs": "S1",
        "definition": "Percentage of employees covered by collective bargaining agreements.",
        "expected_unit": "%",
        "value_type": "percentage",
    },

    # ------------------------------------------------------------------
    # Governance Indicators (ESRS G1 & ESRS 2)
    # ------------------------------------------------------------------
    {
        "name": "Board Female Representation",
        "category": "Governance",
        "esrs": "G1",
        "definition": "Percentage of board members who identify as female.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
    {
        "name": "Board Meetings",
        "category": "Governance",
        "esrs": "G1",
        "definition": "Total number of board meetings held during the reporting year.",
        "expected_unit": "count/year",
        "value_type": "number",
    },
    {
        "name": "Corruption Incidents",
        "category": "Governance",
        "esrs": "G1",
        "definition": "Number of confirmed corruption or bribery incidents during the reporting year.",
        "expected_unit": "count",
        "value_type": "number",
    },
    {
        "name": "Avg Payment Period to Suppliers",
        "category": "Governance",
        "esrs": "ESRS 2",
        "definition": "Average number of days taken to pay suppliers.",
        "expected_unit": "days",
        "value_type": "number",
    },
    {
        "name": "Suppliers Screened for ESG",
        "category": "Governance",
        "esrs": "ESRS 2",
        "definition": "Percentage of suppliers screened using environmental, social, or governance criteria.",
        "expected_unit": "%",
        "value_type": "percentage",
    },
]
