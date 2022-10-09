#tableformat.py

#Parent TableFormatter class
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        tr = '<tr>'
        end_tr = '</tr>'
        th = '<th>'
        end_th = '</th>'
        print(tr, end='')
        for heading in headers:
            print(th, end='')
            print(heading, end='')
            print(end_th, end='')
        print(end_tr)

    def row(self, rowdata):
        tr = '<tr>'
        end_tr = '</tr>'
        td = '<td>'
        end_td = '</td>'
        print(tr, end='')
        for d in rowdata:
            print(td, end='')
            print(d, end='')
            print(end_td, end='')
        print(end_tr)

class FormatError(Exception):
    pass

def create_formatter(fmt):
    '''
    Creates a formatter that outputs data in the format selected by fmt
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')

def print_table(portfolio, headings, formatter):
    '''
    Prints a table with user selected headings
    '''
    formatter.headings(headings)
    for x in portfolio:
        rowdata = []
        for heading in headings:
            rowdata.append(str(getattr(x, heading)))
        formatter.row(rowdata)