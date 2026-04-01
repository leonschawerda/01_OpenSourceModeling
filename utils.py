
"""
Celsius - Fahrenheit converter
"""

def celsius_to_fahrenheit(celsius):
    #Converts Celsius into Fahrenheit
    return (celsius * 9/5) + 32

"""
Filling Data Frame NaN - set missing Data Points in column to mean value
"""

def fill_missing_mean(df, column):
    df[column] = df[column].fillna(df[column].mean())
   
    return df

"""
Normalize Data Frame between -1 and 1 - USEFULL IF VALUES ARE >0
"""

def normalize_column(df, column):
    #rescaling by dividing by the maximum absolute value of the column
    max_val = df[column].abs().max()
    
    if max_val == 0:
        return df
    
    df[column] = df[column] / max_val
    return df
    
