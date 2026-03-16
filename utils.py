"""
Celsius - Fahrenheit converter
"""

def celsius_to_fahrenheit(celsius):
    """Converts Celsius into Fahrenheit"""
    return (celsius * 9/5) + 32


"""
Filling Data Frame NaN - set missing Data Points in column to mean value
"""
import pandas as pd

def fill_missing_mean(df, column):
    df[column] = df[column].fillna(df[column].mean())
    return df