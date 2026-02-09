

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
    Emit a table in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))



class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')



def create_formatter(fmt):
    '''
    Factory function to create a formatter based on the specified format.
    
    :param fmt: A string indicating the desired format ('txt', 'csv', 'html').
    :return: An instance of a TableFormatter subclass corresponding to the specified format.
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format: {fmt}')
    


def print_table(data, cols, fmt):
    '''
    Print a table of data using the specified format.
    
    :param data: A list of stock objects containing the table data.
    :param cols: A list of column names to be used as headings in the table.
    :param fmt: A string indicating the desired format ('txt', 'csv', 'html').
    '''
    
    fmt.headings(cols)
    
    for d in data:
        rowdata = [str(getattr(d, colname)) for colname in cols] # ['AA', 100]
        # rowdata = [str(item) for item in rowdata]  # ['AA', '100']
        
        fmt.row(rowdata)


