# fileparse.py
#
# Exercise 3.3
import csv

from pyparsing import And

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=None):
    '''
    Parse a CSV file ito a list of records
    select is a list containing the subset of columns to be returned
    types is a list containing the types each column should be converted to
    has_headers indicates if the file has headers with column names
    delimiter allows to indicate a different delimiter vs the comma
    '''
    #Checking for parameter "sanity"
    #Can't parse selected columns if the file has no headers
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    
    if delimiter:
        rows = csv.reader(lines, delimiter=delimiter)
    else:    
        rows = csv.reader(lines)

    #Get headers
    if has_headers:
        headers = next(rows)
    if select:
        #validating that select contains valid columns
        test_select = [x in headers for x in select]
        if sum(test_select) == len(select):
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            raise RuntimeError('invalid column selection. choose among the following values: ' + str(headers))
    else:
        indices=[]
    
    records = []
    for rowno, row in enumerate(rows, start=1):
        #skipping rows with no data
        if not row:
            continue 
        
        #subsetting rows picking relevant the columns
        if select: 
            row = [row[index] for index in indices]
        
        #converting variables to the types indicated by the function call
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as ve:
                print(f'Row {rowno}: Could not convert {row}')
                print(f'Row {rowno}: Reason: ', ve)
                continue
        
        #preparing the record to be appended
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)
    return records