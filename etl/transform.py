import pandas as pd
import random

def transform_data():
    print()
    print('🧹✨ Let’s go to Data Cleaning! 🧼📊')
    print()
    input_file = input('📥 Enter your extracted file path: ').strip('"')
    df = pd.read_csv(input_file)

    print('\n🧼 This is BEFORE cleaning:')
    print('======================================')
    print(df.head(5))

    # Remove duplicates
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset=['Email'], inplace=True)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean full name and email
    df['Full_Name'] = df['Full_Name'].str.strip().str.title()
    df['Email'] = df['Email'].str.strip().str.lower()
    df['Email'] = df['Email'].str.replace('_','').str.replace('example','gmail')
    df['Email'] = df['Email'].apply(lambda x: x.replace('.', '_', 1) if x.count('.') > 1 else x)

    # Region and City
    df['Region'] = df['Region'].str.title().str.strip()
    df['City'] = df['City'].str.strip().str.title()

    # Age
    df['Age'] = df['Age'].str.replace('years', '', regex=False).str.strip()
    df['Age'] = df['Age'].astype(int)

    # Handle missing Regions
    region_vals = df['Region'].dropna().tolist()
    df['Region'] = df['Region'].apply(lambda x: random.choice(region_vals) if pd.isna(x) else x)

    # Salary
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    df['Salary'] = df['Salary'].round(2)

    # Split name
    df[['First_Name', 'Last_Name']] = df['Full_Name'].str.split(' ', n=1, expand=True)
    df['First_Name'] = df['First_Name'].str.strip()
    df['Last_Name'] = df['Last_Name'].str.strip()

    # Final columns
    df = df[['First_Name', 'Last_Name', 'Age', 'Email', 'Salary', 'Region', 'City']]
    df.reset_index(drop=True, inplace=True)
    df.index += 1

    print('\n✅ This is AFTER cleaning:')
    print('======================================')
    print(df.head(5))

    print('\n🎉 Transformation and data cleaning done!')
    
    # Save the cleaned DataFrame
    output_file = input('\n💾 Enter the path to save the cleaned data (e.g., cleaned_data.csv): ').strip('"')
    df.to_csv(output_file, index=False)

    print('\n✅ Cleaned data has been saved successfully!')
    print('\n🚀 Now heading to Snowflake to load and push this data!')
    print('========================================================')
