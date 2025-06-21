"""
Design Rules for Tables and Graphs
Comprehensive guidelines for effective data visualization design
"""

# TABLE DESIGN RULES
TABLE_RULES = {
    "use_cases": [
        "Look up individual items",
        "Compare individual values", 
        "Need precise values",
        "More than one unit of measure",
        "Need detail and summary values"
    ],
    
    "delineating_columns_rows": [
        "Use white space effectively",
        "When you can't use white space, use subtle fill colors",
        "When you can't use fill color, use subtle lines/borders",
        "Avoid grid lines"
    ],
    
    "arranging_data": [
        "Based on what facilitates meaningful analysis in business context",
        "Keep structure consistent from group to group",
        "Maintain hierarchical categorical subdivisions from left to right"
    ],
    
    "formatting": [
        "Right align numbers",
        "Center non-numeric data",
        "Maintain consistent number of characters (ex. decimals, dates)",
        "Use commas for larger numbers",
        "Do not exceed the required level of precision",
        "Use a consistent, legible font",
        "Use boldface, italics, or color to highlight"
    ],
    
    "summarizing_values": [
        "Add distinction to column/row summaries",
        "Place summaries in group header if data extends multiple pages"
    ],
    
    "multi_page": [
        "Repeat column headers at top of each page",
        "Repeat current row headers at top of each page"
    ]
}

# GRAPH DESIGN RULES
GRAPH_RULES = {
    "use_cases": [
        "Message is within patterns or trends",
        "Need to reveal relationships",
        "Share expectations/projections"
    ],
    
    "general_tips": [
        "Use a graphic that is appropriate for the data set",
        "Present data in substantive terms",
        "Use color with intention",
        "Add Labels: title, axes, data labels, units"
    ],
    
    "de_cluttering": [
        "Remove the chart border to increase white space",
        "Removing gridlines may help increase white space",
        "Remove data markers to reduce processing load",
        "Clean up the axis labels - remove trailing zeros and abbreviate",
        "Label the data directly, rather than using a legend",
        "Use color consistently throughout the graph"
    ]
}

# CHART TYPES TO AVOID
CHART_TYPES_TO_AVOID = [
    "pie charts",
    "donut charts", 
    "unit charts",
    "radar charts",
    "funnel charts"
]

# MISLEADING DESIGN ELEMENTS
MISLEADING_ELEMENTS = {
    "axis_and_scale": [
        "Using two separate axes for different data series",
        "Truncated axes that don't start at zero",
        "Inconsistent scaling between related charts"
    ],
    
    "visual_distortions": [
        "3D graphics that distort proportions",
        "Tall, narrow graphs that exaggerate trends",
        "Wide graphs that minimize trends",
        "Angles and shadows that make interpretation difficult"
    ],
    
    "data_issues": [
        "Insufficient data without context",
        "Raw numbers without percentages or rates",
        "Data not adjusted for relevant factors (e.g., PPP)",
        "Biased sampling methods",
        "Correlation vs causation confusion"
    ]
}

# DESIGN EVALUATION CRITERIA
EVALUATION_CRITERIA = {
    "clarity": [
        "Is the message clear and easy to understand?",
        "Are labels and titles descriptive?",
        "Is the chart type appropriate for the data?",
        "Is there sufficient context provided?"
    ],
    
    "accuracy": [
        "Are axes properly scaled?",
        "Do the visual elements accurately represent the data?",
        "Is the data source reliable and properly cited?",
        "Are there any visual distortions?"
    ],
    
    "effectiveness": [
        "Does the visualization support the intended message?",
        "Is it free of unnecessary clutter?",
        "Does it use color and formatting appropriately?",
        "Is it accessible to the target audience?"
    ]
}

def get_table_analysis_prompts():
    """Generate analysis prompts for table evaluation"""
    return [
        "Rate this table from 1-10 on readability and organization. Explain your rating.",
        "Evaluate the table formatting: Are numbers right-aligned? Is non-numeric data centered?",
        "Assess the use of white space and borders. Are they effective?",
        "Check if the data arrangement facilitates meaningful analysis.",
        "Suggest specific improvements for table design and clarity."
    ]

def get_graph_analysis_prompts():
    """Generate analysis prompts for graph evaluation"""
    return [
        "Rate this graph from 1-10 on clarity and effectiveness. Explain your rating.",
        "Is this chart type appropriate for the data being presented? Why or why not?",
        "Evaluate the use of color, labels, and formatting.",
        "Check for potential misleading elements or visual distortions.",
        "Assess if the graph is free of clutter and uses white space effectively.",
        "Suggest improvements for better data communication."
    ]

def get_design_scorecard():
    """Create a comprehensive design scorecard"""
    return {
        "table_scorecard": {
            "formatting": ["Number alignment", "Font consistency", "Precision level"],
            "organization": ["White space usage", "Border usage", "Data arrangement"],
            "clarity": ["Readability", "Logical structure", "Summary presentation"]
        },
        "graph_scorecard": {
            "appropriateness": ["Chart type selection", "Data suitability", "Message alignment"],
            "design": ["Color usage", "Labeling", "Clutter reduction"],
            "accuracy": ["Scale integrity", "Visual distortion", "Data representation"]
        }
    }

def get_improvement_suggestions(chart_type="table"):
    """Get specific improvement suggestions based on chart type"""
    if chart_type.lower() == "table":
        return [
            "Consider right-aligning numeric data",
            "Use consistent formatting for similar data types",
            "Add subtle borders or fill colors for better separation",
            "Ensure adequate white space between elements",
            "Use bold or color to highlight important values"
        ]
    else:  # graph
        return [
            "Remove unnecessary chart borders and gridlines",
            "Label data directly instead of using legends",
            "Use consistent color schemes throughout",
            "Clean up axis labels and remove trailing zeros",
            "Ensure the chart type matches the data and message",
            "Add proper context and units to all labels"
        ] 