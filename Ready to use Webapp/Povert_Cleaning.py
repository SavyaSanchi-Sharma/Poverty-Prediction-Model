import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
def clean_data(file):
    df = pd.read_csv(file,parse_dates=True)
    df.drop_duplicates()
    # Check for missing values and their counts
    missing_values = df.isnull().sum()

    # Drop columns with a high percentage of missing values (e.g., more than 50% missing)
    threshold = 0.5 * len(df)
    data_cleaned = df.dropna(thresh=threshold, axis=1)

    # Recheck missing values after dropping
    remaining_missing_values = data_cleaned.isnull().sum()

    # Convert 'year' and 'survey_year' to integer for consistency (fill missing with mode or median)
    data_cleaned['year'] = data_cleaned['year'].fillna(data_cleaned['year'].median()).astype(int)
    data_cleaned['survey_year'] = data_cleaned['survey_year'].fillna(data_cleaned['survey_year'].median()).astype(int)

    # Check column names for possible renaming
    columns_before_rename = data_cleaned.columns
    data_cleaned_renamed = data_cleaned.rename(columns={
    'headcount_ratio_international_povline': 'hc_ratio',
    'gini': 'gini_index',
    'mld': 'mean_log_deviation',
    'palma_ratio': 'palma_index',
    's80_s20_ratio': 's80_s20_index',
    'p90_p10_ratio': 'p90_p10_index',
    'p90_p50_ratio': 'p90_p50_index',
    'p50_p10_ratio': 'p50_p10_index',
    'poverty_gap_index_international_povline':'international_poverty_gap',
    'poverty_gap_index_100':'$1_poverty_gap'
    })

    # Dropping columns with more than 50% missing values if requested by user (already kept those with fewer missing values)
    data_final = data_cleaned_renamed.dropna(subset=['reporting_level', 'welfare_type'])

    # Checking the final cleaned dataframe's structure
    cleaned_columns = data_final.columns
    final_info = data_final.info()
    # Drop duplicate rows
    data_final_no_duplicates = data_final.drop_duplicates()

    # Standardize categorical variables (lowercase and strip whitespace)
    data_final_no_duplicates['country'] = data_final_no_duplicates['country'].str.lower().str.strip()
    data_final_no_duplicates['reporting_level'] = data_final_no_duplicates['reporting_level'].str.lower().str.strip()
    data_final_no_duplicates['welfare_type'] = data_final_no_duplicates['welfare_type'].str.lower().str.strip()

    # Check the final cleaned dataframe's structure and any duplicates
    final_no_duplicates_info = data_final_no_duplicates.info()
    duplicates_count = data_final.shape[0] - data_final_no_duplicates.shape[0]
    data_final.dropna(inplace=True)
    keep_cols=['headcount_international_povline',
    'total_shortfall_international_povline',
    'income_gap_ratio_international_povline',
     'decile1_avg',
     'decile2_avg',
     'decile3_avg',
     'poverty_gap_index_international_povline',
     'poverty_gap_index_100',
    ]
    headcount=[col for col in data_final if "headcount" in col]
    totalShort=[col for col in data_final if "total_shortfall" in col]
    IncomeGap=[col for col in data_final if "income_gap_ratio" in col]
    dec=[col for col in data_final if "decile" in col]
    avg=[col for col in data_final if "avg_shortfall_" in col]
    pgi=[col for col in data_final if "poverty_gap_index" in col]
    columns_to_drop = list(set(IncomeGap + dec + headcount + totalShort+avg+pgi)-set(keep_cols))+[
                                                                                            'survey_year',
                                                                                          'ppp_version',
                                                                                          'survey_comparability',
                                                                                          'welfare_type','mean',
                                                                                          'mean_log_deviation',
                                                                                          'median',
                                                                                          'p50_p10_index',
                                                                                          'p90_p10_index',
                                                                                          'p90_p50_index',
                                                                                          's80_s20_index'
                                                                                          ]
    data_final.drop(columns=columns_to_drop,inplace=True)
    NumVal=data_final.select_dtypes(int and float)
    FilteredData=data_final
    FilteredData.reset_index()
    FilteredData['decile']=FilteredData[['decile1_avg','decile2_avg','decile3_avg']].mean(axis=1)
    FilteredData.drop(['decile1_avg','decile2_avg','decile3_avg'],axis=1,inplace=True)
    FilteredData.sort_values(by='reporting_level',inplace=True)
    FilteredData.reset_index()
    return FilteredData
