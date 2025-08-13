# IF Function that fills a new columns value based on condition/values from other columns.

def process_order(row):   #establishing your functon
    internal_order = row['Internal Order']     #next three lines are assigning column values to objects
    partner_order_no = row['Partner order no.']
    mr9_line = row['MR9 Line']

    if pd.notna(internal_order):  # Check if internal_order is not None or NaN
        return internal_order[-7:]
    elif pd.notna(partner_order_no):  # Check if partner_order_no is not None or NaN
        return partner_order_no
    else:
        return mr9_line

# Apply the function to each row and create a new column with the results
act['IO_Clean'] = act.apply(process_order, axis=1)

## Anothe example with AND in the condition.


def process_order(row):
    name = row['Name']
    purchasing_document = row['Purchasing Document']
    mr9_line = row['MR9 Line']
    purchase_order_text = row['Purchase order text']

    if pd.isna(name) and pd.notna(purchasing_document):  # Check if name is an and purchasing documnet is not
        return purchase_order_text                      # if both conditionds are validated return purcahse order text value
    elif pd.isna(name) and pd.isna(purchasing_document):  # Check if name is na and purchasing dicumnet is not
        return mr9_line                                  # if both conditionds are validated return purcahse order text value
    else:
        return name

# Apply the function to each row and create a new column with the results
act['Name_Clean'] = act.apply(process_order, axis=1)



#IF function to change values based on a contains function




## Function that promotes row headers based off a one of the column names. 
def promote_row_to_header(df, search_headers):       #function for promoting headers based on a specific keyword.
    """
    Promotes a row within a DataFrame that contains specific headers to the header of the DataFrame.

    Parameters:
    - df: The DataFrame which contains the data with a changing header row.
    - search_headers: A list of expected header titles to look for in the rows.

    Returns:
    - A DataFrame with the correct header row promoted.
    """
    # Iterate through each row to find the header
    for i, row in df.iterrows():
        if set(search_headers).issubset(set(row)):
            # Set this row as the header
            df.columns = row
            # Drop the original header row
            break

    # Reset index after row removal
    df.reset_index(drop=True, inplace=True)

    return df
  
search_headers = ['Project Name']    #where you put a column name that will promote all rows.
categorical_df = promote_row_to_header(df, search_headers)
