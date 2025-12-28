# config/pages.py

"""
Page mappings for ESG indicators per company.

Each company maps:
- "__pdf_path__" → PDF file path
- Indicator name → (start_page, end_page)
"""

PAGE_MAPPING = {
    "AIB": {
        "__pdf_path__": "data/aib-group-plc-afr-report-2024.pdf",

        "Total Scope 1 GHG Emissions": (63, 75),
        "Total Scope 2 GHG Emissions": (63, 75),
        "Total Scope 3 GHG Emissions": (70, 90),
        "GHG Emissions Intensity": (75, 85),
        "Total Energy Consumption": (65, 75),
        "Renewable Energy Percentage": (70, 80),
        "Net Zero Target Year": (120, 125),
        "Green Financing Volume": (63, 70),

        "Total Employees": (83, 90),
        "Female Employees": (85, 95),
        "Gender Pay Gap": (90, 100),
        "Training Hours per Employee": (95, 105),
        "Employee Turnover Rate": (85, 95),
        "Work-Related Accidents": (100, 110),
        "Collective Bargaining Coverage": (105, 115),

        "Board Female Representation": (128, 132),
        "Board Meetings": (138, 145),
        "Corruption Incidents": (99, 105),
        "Avg Payment Period to Suppliers": (170, 180),
        "Suppliers Screened for ESG": (99, 110),
    },

    "BPCE": {
        "__pdf_path__": "data/bpce-urd-2024.pdf",

        "Total Scope 1 GHG Emissions": (50, 90),
        "Total Scope 2 GHG Emissions": (50, 90),
        "Total Scope 3 GHG Emissions": (50, 90),
        "GHG Emissions Intensity": (85, 95),
        "Total Energy Consumption": (60, 75),
        "Renewable Energy Percentage": (70, 85),
        "Net Zero Target Year": (395, 405),
        "Green Financing Volume": (50, 70),

        "Total Employees": (50, 55),
        "Female Employees": (55, 70),
        "Gender Pay Gap": (70, 85),
        "Training Hours per Employee": (85, 100),
        "Employee Turnover Rate": (65, 75),
        "Work-Related Accidents": (95, 110),
        "Collective Bargaining Coverage": (110, 120),

        "Board Female Representation": (412, 420),
        "Board Meetings": (461, 470),
        "Corruption Incidents": (496, 505),
        "Avg Payment Period to Suppliers": (519, 525),
        "Suppliers Screened for ESG": (396, 410),
    },

    "BBVA": {
        "__pdf_path__": "data/consolidated_management_report.pdf",

        "Total Scope 1 GHG Emissions": (120, 140),
        "Total Scope 2 GHG Emissions": (120, 140),
        "Total Scope 3 GHG Emissions": (140, 170),
        "GHG Emissions Intensity": (145, 155),
        "Total Energy Consumption": (130, 145),
        "Renewable Energy Percentage": (135, 150),
        "Net Zero Target Year": (200, 205),
        "Green Financing Volume": (125, 140),

        "Total Employees": (210, 220),
        "Female Employees": (215, 225),
        "Gender Pay Gap": (220, 230),
        "Training Hours per Employee": (225, 235),
        "Employee Turnover Rate": (215, 225),
        "Work-Related Accidents": (230, 240),
        "Collective Bargaining Coverage": (235, 245),

        "Board Female Representation": (260, 270),
        "Board Meetings": (275, 285),
        "Corruption Incidents": (290, 300),
        "Avg Payment Period to Suppliers": (305, 315),
        "Suppliers Screened for ESG": (295, 310),
    },
}
