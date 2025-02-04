#Imports
import pandas as pd
import re

# Function to perform preliminary Exploratory Data Analysis (EDA)
def eda_preliminar(df):
    # Display the first few rows of the DataFrame
    display(df.head())
    print("--------------")
    
    # Display general information about the DataFrame (e.g., column types, non-null counts)
    print("\nGeneral Information")
    display(df.info())
    print("--------------")
    
    # Display the count of missing (null) values in each column
    print("\nMissing Values")
    display(df.isnull().sum())
    print("--------------")
    
    # Display the count of duplicated rows in the DataFrame
    print("\nDuplicated Rows")
    display(df.duplicated().sum())
    print("--------------")
    
    # Display the unique values for each textual column (object data type)
    print("\nTextual Values")
    for col in df.select_dtypes(include='O').columns:  # Select columns with object data type (text)
        display(df[col].value_counts())  # Show value counts for each text column
    print("--------------")
    
    # Display summary statistics (mean, std, min, max, etc.) for numerical columns
    print("\nNumerical Values")
    display(df.describe().T)  # Transpose the result for better readability

# Function to convert a specified column to datetime format
def column_to_datetime(df, column):
    # Convert the specified column to datetime format using pd.to_datetime()
    df[column] = pd.to_datetime(df[column])
    display(df.info())

# Function to change the column name in a DataFrame
def change_column_name(df, col, newcol):
    # Rename the column by assigning the values of the old column to the new column
    df[newcol] = df[col]
    
    # Drop the old column
    df.drop(columns=[col], inplace=True)
    
    # Display the updated column names
    display(df.columns)

# Function to split an address into its components, applied to a DataFrame column
def separate_address(df, column):
    # Define the regular expression pattern to capture address components
    pattern = r'(?P<Address_Number>\d+)\s+(?P<Address_Street>[\w\s]+),\s*(?P<Address_City>[\w\s]+),\s*(?P<Address_State>[A-Z]{2})\s+(?P<Address_Zip_Code>\d{5})'
    
    # Apply the regex pattern to each row in the specified column
    # The function returns a dictionary of address components if a match is found
    def extract_address(address):
        match = re.match(pattern, address)
        return match.groupdict() if match else {"Address_Number": None, "Address_Street": None, "Address_City": None, "Address_State": None, "Address_Zip_Code": None}
    
    # Apply the function to the specified column, then convert the resulting dictionaries to separate columns
    separated_columns = df[column].apply(extract_address).apply(pd.Series)
    
    # Join the separated columns with the original DataFrame
    df = df.join(separated_columns)
    
    # Return the updated DataFrame with the new columns
    return df