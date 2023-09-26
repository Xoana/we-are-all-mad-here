'''
This script is used to parse a Tableau .twb file, extract various elements 
(worksheets, data sources, dashboards, filters, and calculations), and write
the data to an Excel spreadsheet.
'''
import logging
import pandas as pd
import xml.etree.ElementTree as ET
import click
logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_list_of_elements(datasources,columns_by_worksheet,worksheets_by_dashboard):
    ''' Returns a list of data sources, dashboards, and worksheets. '''
    element_data = []
    element_data = build_element_data(element_data,datasources.datasource_caption.dropna().unique(),'datasource')
    element_data = build_element_data(element_data,columns_by_worksheet.worksheet_name.unique(),'worksheet')
    element_data = build_element_data(element_data,worksheets_by_dashboard.dashboard_name.unique(),'dashboard')

    element_df = pd.DataFrame.from_records(element_data)   

    return element_df

def build_element_data(element_data,unique_list,type):
    ''' Builds a list of dictionaries for writing Summary to Excel. '''
    for item in unique_list:
        summary_dict = {}
        summary_dict['element_name'] = item
        summary_dict['element_type'] = type
        element_data.append(summary_dict)
    return(element_data)

def get_datasources(input_file):
    ''' Returns distinct data source name and caption. '''
    root = ET.parse(input_file).getroot()
    dashboard_data = []

    for element in root:
        if element.tag == 'datasources':
            for child in element:
                datasource_caption = child.attrib.get('caption')
                datasource_name = child.attrib.get('name')
                for child2 in child:
                    if 'connection' in child2.tag:
                        for connection_element in child2:
                            if '_.fcp.ObjectModelEncapsulateLegacy.true...relation' in connection_element.tag:
                                datasource_query = connection_element.text

                                element_dict = {}
                                element_dict['datasource_caption'] = datasource_caption
                                element_dict['datasource_name'] = datasource_name
                                element_dict['datasource_query'] = datasource_query
                                dashboard_data.append(element_dict)
                   
    datasources = pd.DataFrame.from_records(dashboard_data)   

    return datasources   

def get_columns_by_datasource(input_file):
    ''' Returns columns and calculations by data source. '''
    root = ET.parse(input_file).getroot()
    datasources_data = []

    for element in root:
        if element.tag == 'datasources':
            for child in element:
                datasource_name = child.attrib.get('caption')
                for child_element in child:
                    if child_element.tag == 'column':
                        column_caption = child_element.attrib.get('caption') if 'caption' in child_element.attrib else 'none'
                        column_name = child_element.attrib.get('name')
                        column_datatype = child_element.attrib.get('datatype')
                        column_hidden = child_element.attrib.get('hidden')
                        if len(list(child_element)) > 0:
                            for calculation in child_element:
                                column_calc = calculation.attrib.get('formula') if 'formula' in calculation.attrib else 'none'
                        else:
                            column_calc = 'none'

                        element_dict = {}

                        element_dict['datasource_name'] = datasource_name
                        element_dict['column_caption'] = column_caption
                        element_dict['column_name'] = column_name
                        element_dict['column_datatype'] = column_datatype
                        element_dict['column_hidden'] = column_hidden
                        element_dict['column_calc'] = column_calc
                        datasources_data.append(element_dict)
    datasources_df = pd.DataFrame.from_records(datasources_data)   

    return datasources_df

def get_datasources_by_worksheet(input_file): 
    ''' Returns data sources by worksheet. '''
    root = ET.parse(input_file).getroot()

    worksheet_data = []

    for element in root:
        if element.tag == 'worksheets':
            for child in element:
                worksheet_name = child.attrib.get('name')
                for child_element in child:
                    if child_element.tag == 'table':
                        for table_element in child_element:
                            if table_element.tag == 'view':
                                for view_element in table_element:
                                    if view_element.tag == 'datasources':
                                        for datasource_element in view_element:
                                            datasource_caption = datasource_element.attrib.get('caption')
                                            datasource_name = datasource_element.attrib.get('name')
                                            element_dict = {}
                                            element_dict['worksheet_name'] = worksheet_name
                                            element_dict['datasource_caption'] = datasource_caption
                                            element_dict['datasource_name'] = datasource_name
                                            worksheet_data.append(element_dict)
    columns_by_worksheet = pd.DataFrame.from_records(worksheet_data)   

    return columns_by_worksheet


def get_columns_by_worksheet(input_file):
    ''' Returns columns and calculations by worksheet. '''
    root = ET.parse(input_file).getroot()

    worksheet_data = []

    for element in root:
        if element.tag == 'worksheets':
            for child in element:
                worksheet_name = child.attrib.get('name')
                for child_element in child:
                    if child_element.tag == 'table':
                        for table_element in child_element:
                            if table_element.tag == 'view':
                                for view_element in table_element:
                                    if view_element.tag == 'datasource-dependencies':
                                        for column_element in view_element:
                                            if column_element.tag == 'column':
                                                column_caption = column_element.attrib.get('caption') if 'caption' in column_element.attrib else 'none'
                                                column_name = column_element.attrib.get('name')
                                                column_datatype = column_element.attrib.get('datatype')
                                                if len(list(column_element)) > 0:
                                                    for calculation in column_element:
                                                        if 'formula' in calculation.attrib:
                                                            column_calc = calculation.attrib.get('formula')
                                                else:
                                                    column_calc = 'none'

                                                element_dict = {}
                                                element_dict['worksheet_name'] = worksheet_name
                                                element_dict['column_caption'] = column_caption
                                                element_dict['column_name'] = column_name
                                                element_dict['column_datatype'] = column_datatype
                                                element_dict['column_calc'] = column_calc
                                                worksheet_data.append(element_dict)

    columns_by_worksheet = pd.DataFrame.from_records(worksheet_data)   

    return columns_by_worksheet

def get_filters_by_worksheet(input_file): 
    ''' Returns data sources by worksheet. '''
    root = ET.parse(input_file).getroot()

    sar_values = ['[',']','none:','rank:',':nk',':ok',':qk','usr:',':tqr',':']
    element_data = []

    for element in root:
        if element.tag == 'worksheets':
            for child in element:
                worksheet_name = child.attrib.get('name')
                for child_element in child:
                    if child_element.tag == 'table':
                        for table_element in child_element:
                            if table_element.tag == 'view':
                                for view_element in table_element:
                                    if view_element.tag == 'filter':
                                        filter_datasource = view_element.attrib.get('column').split('].[')[0]
                                        filter_name = view_element.attrib.get('column').split('].[')[1]
                                        for value in sar_values:
                                            filter_datasource = filter_datasource.replace(value,'')
                                            filter_name = filter_name.replace(value,'')
                                        filter_notes = '' if filter_name != 'Measure Names' else 'This filter is used to display specific values and will show as a column on the worksheet; see Columns by Worksheet.'

                                        element_dict = {}
                                        element_dict['worksheet_name'] = worksheet_name
                                        element_dict['filter_datasource'] = filter_datasource
                                        element_dict['filter_name'] = filter_name
                                        element_dict['filter_notes'] = filter_notes
                                        element_data.append(element_dict)

    filters_by_worksheet = pd.DataFrame.from_records(element_data)   

    return filters_by_worksheet

def get_worksheets_by_dashboard(input_file):
    ''' Get worksheets by dashboard. '''
    root = ET.parse(input_file).getroot()
    element_data = []
    
    for element in root:
        if element.tag == 'windows':
            for child in element:
                if child.tag == 'window':
                    dashboard_name = child.attrib.get('name')
                for child_element in child:
                    if child_element.tag == 'viewpoints':
                        for viewpoint_element in child_element:
                            worksheet_name = viewpoint_element.attrib.get('name')

                            element_dict = {}
                            element_dict['dashboard_name'] = dashboard_name
                            element_dict['worksheet_name'] = worksheet_name
                            element_data.append(element_dict)

    dashboard_ws_df = pd.DataFrame.from_records(element_data)   

    return dashboard_ws_df    


def write_excel(output_file,element_df,datasources,columns_by_datasource,datasources_by_worksheet,columns_by_worksheet,worksheets_by_dashboard,filters_by_worksheet):
    ''' Write dataframes to Excel. '''
    with pd.ExcelWriter(output_file) as writer:
        element_df.to_excel(writer, sheet_name='Workbook Elements', index=False)
        datasources.to_excel(writer, sheet_name='Datasources & Tableau Queries', index=False)
        datasources_by_worksheet.to_excel(writer, sheet_name='Datasources by Worksheet', index=False)
        worksheets_by_dashboard.to_excel(writer, sheet_name='Worksheets by Dashboard', index=False)
        columns_by_datasource.to_excel(writer, sheet_name='Columns by Datasource', index=False)
        columns_by_worksheet.to_excel(writer, sheet_name='Columns by Worksheet', index=False)
        filters_by_worksheet.to_excel(writer, sheet_name='Filters by Worksheet', index=False)


@click.command()
@click.option('--input_file', default='input_file.twb', show_default=True,
              help='Name of the file to parse.')
@click.option('--output_file', default='output_file.xlsx', show_default=True,
              help='Name of the file to parse.')
def main(input_file,output_file):
    ''' Parses a Tableau twb file and extracts the fields and data sources used on each worksheet and data source. '''
    logging.info('>>>> Processing %s...',input_file)

    datasources = get_datasources(input_file)
    columns_by_datasource = get_columns_by_datasource(input_file)
    datasources_by_worksheet = get_datasources_by_worksheet(input_file)
    columns_by_worksheet = get_columns_by_worksheet(input_file)
    worksheets_by_dashboard = get_worksheets_by_dashboard(input_file)
    element_df = get_list_of_elements(datasources,columns_by_worksheet,worksheets_by_dashboard)
    filters_by_worksheet = get_filters_by_worksheet(input_file)
    write_excel(output_file,element_df,datasources,columns_by_datasource,datasources_by_worksheet,columns_by_worksheet,worksheets_by_dashboard,filters_by_worksheet)


if __name__ == '__main__':
    main()

