# Data Profiling with ydata-profiling

## What is Data Profiling?

Data profiling is the process of examining and analyzing datasets to understand their structure, content, and quality. It provides comprehensive insights into your data by automatically generating statistical summaries, identifying patterns, detecting anomalies, and highlighting potential data quality issues.

### Why is Data Profiling Important?

Data profiling helps data scientists and analysts to:

- **Understand data structure** - Get an overview of columns, data types, and relationships
- **Identify data quality issues** - Detect missing values, duplicates, and inconsistencies
- **Discover patterns and distributions** - Understand how data is distributed across variables
- **Find correlations** - Identify relationships between different variables
- **Detect outliers** - Spot unusual values that might need attention
- **Save time** - Quickly understand datasets without writing extensive exploratory code
- **Make informed decisions** - Base data cleaning and preprocessing decisions on comprehensive analysis

## ydata-profiling Tool

https://docs.profiling.ydata.ai/latest/

`ydata-profiling` (formerly known as `pandas-profiling`) is a powerful Python library that generates comprehensive data profiling reports from pandas DataFrames with just a single line of code.

### Key Features

- **Automated Analysis** - Generates detailed reports automatically
- **Interactive HTML Reports** - Beautiful, interactive web-based reports
- **Comprehensive Statistics** - Descriptive statistics for all data types
- **Data Quality Assessment** - Identifies missing values, duplicates, and data quality issues
- **Correlation Analysis** - Shows relationships between variables
- **Distribution Visualization** - Histograms, box plots, and other visualizations
- **Configurable** - Customizable analysis parameters
- **Integration Ready** - Works seamlessly with Jupyter notebooks and web applications

## Installation

### Method 1: Using pip (Recommended)

```bash
pip install ydata-profiling
```

### Method 2: Using conda

```bash
conda install -c conda-forge ydata-profiling
```

## Basic Usage

### Simple Profiling Report

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Generate the profiling report
profile = ProfileReport(df, title="Data Profiling Report")

# Save as HTML file
profile.to_file("data_profile_report.html")

# Display in Jupyter notebook
profile.to_notebook_iframe()
```

### Quick Example with Sample Data

```python
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# Create sample dataset
np.random.seed(42)
sample_data = {
    'numeric_col': np.random.randn(1000),
    'categorical_col': np.random.choice(['A', 'B', 'C'], 1000),
    'date_col': pd.date_range('2020-01-01', periods=1000, freq='D'),
    'binary_col': np.random.choice([0, 1], 1000),
    'missing_col': np.where(np.random.random(1000) < 0.1, np.nan, np.random.randn(1000))
}

df = pd.DataFrame(sample_data)

# Generate profiling report
profile = ProfileReport(
    df,
    title="Sample Data Profile",
    explorative=True
)

# Save the report
profile.to_file("sample_data_report.html")
```

## Advanced Configuration

### Customizing the Report

```python
from ydata_profiling import ProfileReport

# Configure the profiling report
profile = ProfileReport(
    df,
    title="Advanced Data Profile",
    explorative=True,  # Enable detailed analysis
    dark_mode=True,    # Use dark theme
    config_file="config.yaml"  # Use custom configuration
)

# Custom configuration parameters
profile_config = {
    "title": "Custom Data Profile",
    "dataset": {
        "description": "This dataset contains information about...",
        "creator": "Data Science Team",
        "author": "Your Name",
        "url": "https://github.com/your-repo"
    },
    "variables": {
        "descriptions": {
            "numeric_col": "This column represents...",
            "categorical_col": "This column contains categories..."
        }
    },
    "correlations": {
        "pearson": {"calculate": True},
        "spearman": {"calculate": True},
        "kendall": {"calculate": False}
    },
    "missing_diagrams": {
        "bar": True,
        "matrix": True,
        "heatmap": True
    }
}

# Apply custom configuration
profile = ProfileReport(df, **profile_config)
```

### Performance Optimization for Large Datasets

```python
# For large datasets, optimize performance
profile = ProfileReport(
    df,
    minimal=True,           # Generate minimal report
    samples={"head": 5, "tail": 5},  # Show fewer sample rows
    correlations={
        "pearson": {"calculate": False},
        "spearman": {"calculate": False}
    },
    interactions={"targets": []},  # Disable interactions analysis
    explorative=False       # Disable explorative analysis
)
```

## Different Output Formats

### HTML Report (Default)

```python
# Save as HTML file (interactive)
profile.to_file("report.html")
```

### JSON Output

```python
# Export as JSON for programmatic access
json_data = profile.to_json()

# Save JSON to file
with open("profile_data.json", "w") as f:
    f.write(json_data)
```

### Widget in Jupyter Notebook

```python
# Display as interactive widget in Jupyter
profile.to_widgets()

# Display as iframe in Jupyter
profile.to_notebook_iframe()
```

## Real-World Example

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load a real dataset (example with Titanic dataset)
def analyze_titanic_data():
    # Load Titanic dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    # Configure profiling
    profile = ProfileReport(
        df,
        title="Titanic Dataset Analysis",
        dataset={
            "description": "Analysis of the famous Titanic passenger dataset",
            "creator": "Data Science Team",
            "author": "Your Name"
        },
        variables={
            "descriptions": {
                "PassengerId": "Unique identifier for each passenger",
                "Survived": "Survival status (0 = No, 1 = Yes)",
                "Pclass": "Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)",
                "Name": "Passenger name",
                "Sex": "Passenger gender",
                "Age": "Age in years",
                "Fare": "Passenger fare"
            }
        },
        explorative=True,
        dark_mode=False
    )
    
    # Generate report
    profile.to_file("titanic_analysis.html")
    print("Titanic analysis report generated: titanic_analysis.html")
    
    return profile

# Run the analysis
titanic_profile = analyze_titanic_data()
```

## Integration with Data Science Workflow

### Using with Data Cleaning Pipeline

```python
def profile_before_after_cleaning(df_raw, df_cleaned):
    """Compare data before and after cleaning."""
    
    # Profile raw data
    raw_profile = ProfileReport(
        df_raw,
        title="Raw Data Profile",
        explorative=True
    )
    raw_profile.to_file("raw_data_profile.html")
    
    # Profile cleaned data
    cleaned_profile = ProfileReport(
        df_cleaned,
        title="Cleaned Data Profile",
        explorative=True
    )
    cleaned_profile.to_file("cleaned_data_profile.html")
    
    print("Generated comparison reports:")
    print("- Raw data: raw_data_profile.html")
    print("- Cleaned data: cleaned_data_profile.html")

# Example usage
# profile_before_after_cleaning(df_original, df_processed)
```

### Automated Quality Checks

```python
def automated_data_quality_check(df, quality_threshold=0.8):
    """Perform automated data quality assessment."""
    
    profile = ProfileReport(df, explorative=True)
    
    # Extract key metrics
    missing_percentage = profile.get_description()["table"]["n_cells_missing"] / profile.get_description()["table"]["n_cells"]
    duplicate_percentage = profile.get_description()["table"]["n_duplicates"] / profile.get_description()["table"]["n"]
    
    quality_score = 1 - missing_percentage - duplicate_percentage
    
    print(f"Data Quality Assessment:")
    print(f"- Missing data: {missing_percentage:.2%}")
    print(f"- Duplicate rows: {duplicate_percentage:.2%}")
    print(f"- Quality score: {quality_score:.2%}")
    
    if quality_score >= quality_threshold:
        print("✅ Data quality meets threshold!")
    else:
        print("❌ Data quality below threshold - review needed")
    
    return profile, quality_score

# Example usage
# profile, score = automated_data_quality_check(df, 0.85)
```

## Best Practices

### 1. Start with Minimal Reports for Large Datasets

```python
# For datasets > 100MB, start minimal
profile = ProfileReport(df, minimal=True)
```

### 2. Use Descriptive Titles and Metadata

```python
profile = ProfileReport(
    df,
    title="Customer Database - Q3 2023",
    dataset={
        "description": "Quarterly customer analysis",
        "creator": "Analytics Team",
        "copyright_holder": "Company Name",
        "copyright_year": "2023"
    }
)
```

### 3. Save Configuration for Consistency

```python
# Save your preferred configuration
config = {
    "title": "Standard Data Profile",
    "explorative": True,
    "dark_mode": False,
    "correlations": {
        "pearson": {"calculate": True},
        "spearman": {"calculate": True}
    }
}

# Reuse configuration
profile = ProfileReport(df, **config)
```

### 4. Automate Report Generation

```python
def generate_monthly_profile(data_path, output_dir):
    """Generate monthly data profiling reports."""
    import os
    from datetime import datetime
    
    df = pd.read_csv(data_path)
    current_date = datetime.now().strftime("%Y-%m")
    
    profile = ProfileReport(
        df,
        title=f"Monthly Data Profile - {current_date}",
        explorative=True
    )
    
    output_path = os.path.join(output_dir, f"profile_{current_date}.html")
    profile.to_file(output_path)
    
    print(f"Profile generated: {output_path}")

# Schedule this function to run monthly
```

## Troubleshooting

### Common Issues and Solutions

1. **Memory Issues with Large Datasets**
   ```python
   # Use minimal mode
   profile = ProfileReport(df, minimal=True)
   ```

2. **Slow Performance**
   ```python
   # Disable expensive computations
   profile = ProfileReport(
       df,
       correlations={"pearson": {"calculate": False}},
       interactions={"targets": []},
       explorative=False
   )
   ```

3. **HTML Report Not Opening**
   ```python
   # Ensure file path is correct and accessible
   import os
   profile.to_file(os.path.abspath("report.html"))
   ```

## Additional Resources

- **Official Documentation**: https://ydata-profiling.ydata.ai/
- **GitHub Repository**: https://github.com/ydataai/ydata-profiling
- **Examples and Tutorials**: https://ydata-profiling.ydata.ai/docs/master/rtd/pages/examples.html
- **Configuration Reference**: https://ydata-profiling.ydata.ai/docs/master/rtd/pages/advanced_usage/available_settings.html

## Conclusion

ydata-profiling is an essential tool for any data science project. It provides comprehensive insights into your datasets quickly and efficiently, helping you make informed decisions about data cleaning, preprocessing, and analysis strategies. By integrating data profiling into your workflow, you can:

- Reduce time spent on initial data exploration
- Identify data quality issues early
- Make data-driven decisions about preprocessing steps
- Create professional reports for stakeholders
- Ensure consistent data analysis across projects

Start incorporating ydata-profiling into your data science workflow today to enhance your data understanding and improve project outcomes!