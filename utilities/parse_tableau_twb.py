import sys
import glob
import logging
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import click

logging.basicConfig(level=logging.INFO, format='%(message)s')

LIST_TWB_ELEMENTS = ["worksheet", "dashboard"]

LIST_OUTPUT_FILES = ["combined_fields_by_data_source.csv",
                   "combined_sources_by_dashboard.csv",
                   "combined_sources_by_worksheet.csv"]


def get_datasources(twb_element, template_file, template_name):
    """ Returns csv file of data sources used for each worksheet. """
    column_headers = [twb_element, "data_source", "dependency"]
    root = ET.parse(template_file).getroot()
    list_elements = []
    for root_element in root.iter():
        if root_element.tag == twb_element:
            # Name based on twb_element (worksheet or dashboard)
            element_name = root_element.attrib["name"]

            datasource = root_element.iter(tag="datasource")

            for data in datasource:

                element_details_lst = []
                element_details_lst.append(element_name)

                if "caption" in data.attrib:
                    data_source = data.attrib["caption"]
                    element_details_lst.append(data_source)

                if "name" in data.attrib:
                    dependency_name = data.attrib["name"]
                    element_details_lst.append(dependency_name)
                list_elements.append(element_details_lst)

    datasource_df = pd.DataFrame(list_elements)

    datasource_df.to_csv(f"datasource_by_{twb_element}_{template_name}.csv", sep=',', index=False, header=column_headers)


def get_fields(twb_element, template_file, template_name):
    """ Returns csv file of data sources used for each worksheet. """
    column_headers = [twb_element, "remote_field_name",
                      "tableau_field_name",
                      "datatype", "data_source",
                      "dependency"]

    root = ET.parse(template_file).getroot()

    list_elements = []

    for element in root.iter():
        if element.tag == twb_element:
            worksheet_name = element.attrib["name"]

            for root_element in element.iter():

                if root_element.tag == "datasource-dependencies":

                    dependency = root_element.attrib["datasource"]

                    columns = element.iter(tag="column")

                    for data in columns:
                        element_details_lst = []
                        element_details_lst.append(worksheet_name)

                        if "name" in data.attrib:
                            remote_field_name = data.attrib["name"].strip("[]")

                            if "Parameter" in remote_field_name or "Calculation_" in remote_field_name:
                                remote_field_name = f"Tableau ({remote_field_name})"
                            element_details_lst.append(remote_field_name)

                        if "caption" in data.attrib:
                            tableau_field_name = data.attrib["caption"]
                            element_details_lst.append(tableau_field_name)
                        if "caption" not in data.attrib:
                            tableau_field_name = "Remote field used in Tableau calculation."
                            element_details_lst.append(tableau_field_name)

                        if "datatype" in data.attrib:
                            xml_datatype = data.attrib["datatype"]
                            element_details_lst.append(xml_datatype)

                        datasource_df = pd.read_csv(f"datasource_by_{twb_element}_{template_name}.csv")
                        datasource_dependency = datasource_df[datasource_df["dependency"] == dependency]
                        try:
                            datasource_name = datasource_dependency.iloc[0]["data_source"]
                        except Exception:
                            datasource_name = "Parameters"

                        if len(element_details_lst) > 3:
                            element_details_lst.append(datasource_name)
                            element_details_lst.append(dependency)
                            list_elements.append(element_details_lst)

    field_df = pd.DataFrame(list_elements)
    field_df.to_csv(f"fields_by_{twb_element}_{template_name}.csv", sep=',', index=False, header=column_headers)


def create_fields_by_data_source_csv():
    """ Reads output files from previous functions to consolidate and deduplicate information regarding fields used from each data source. """
    all_filenames = [i for i in glob.glob("fields_by_worksheet_*.csv")]
    combined_df = pd.concat([pd.read_csv(file_name) for file_name in all_filenames])
    combined_df = combined_df[["remote_field_name", "tableau_field_name",
                               "datatype", "data_source"]]
    combined_df = combined_df.dropna()

    combined_df = combined_df[~combined_df["remote_field_name"].str.contains("Calculation")]
    combined_df = combined_df[~combined_df["data_source"].str.contains("Parameters")]
    # combined_df = combined_df[~combined_df["remote_field_name"].str.contains("Parameter")]
    # combined_df = combined_df[~combined_df["tableau_field_name"].str.contains("Calculation")]
    # combined_df = combined_df[~combined_df["data_source"].str.contains("Parameters")]

    # combined_df["remote_field_name"] = combined_df.loc[combined_df["remote_field_name"].str.contains("Calculation_")] = f"Tableau {combined_df['remote_field_name']}"
    # combined_df['source_location'] = np.where(combined_df["data_source"].str.contains("Parameters") | combined_df["remote_field_name"].str.contains("Calculation_"), "tableau", "external")
    # combined_df['location'] = np.where(combined_df["remote_field_name"].str.contains("Calculation_"), "tableau", "hadoop")

    combined_df = combined_df.drop_duplicates()
    combined_df.to_csv(LIST_OUTPUT_FILES[0], sep=',', index=False)


def create_data_sources_by_dashboard_csv():
    all_filenames = [i for i in glob.glob("datasource_by_dashboard_*.csv")]
    combined_df = pd.concat([pd.read_csv(file_name) for file_name in all_filenames])
    combined_df = combined_df[["dashboard", "data_source"]]
    combined_df = combined_df[~combined_df["dashboard"].str.contains("pptx_")]
    combined_df.to_csv(LIST_OUTPUT_FILES[1], sep=',', index=False)


def create_data_sources_by_worksheet_csv():
    all_filenames = [i for i in glob.glob("datasource_by_worksheet_*.csv")]
    combined_df = pd.concat([pd.read_csv(file_name) for file_name in all_filenames])

    combined_df = combined_df[["worksheet", "data_source"]]
    combined_df = combined_df[~combined_df["data_source"].str.contains("Parameters")]

    combined_df.to_csv(LIST_OUTPUT_FILES[2], sep=',', index=False)


def combine_csv_files(output_filename):
    """ Combine csv files into one Excel sheet with separate tabs. """

    with pd.ExcelWriter(output_filename) as writer:  

        for csv_file in LIST_OUTPUT_FILES:
            csv_df = pd.read_csv(csv_file)
            sheet_name = csv_file.strip("combined_").replace(".csv", "")
            print(sheet_name)

            csv_df.to_excel(writer, sheet_name=sheet_name, index=False)
            
@click.command()
@click.option("--template_file", default="", show_default=True,
              help="Name of the file to parse.")
@click.option("--output_filename", default="final_data_sources_and_fields.xlsx", show_default=True,
              help="Name of the file to parse.")              
def main(template_file, output_filename):
    """ Parses a Tableau twb file and extracts the fields and data sources used on each worksheet and data source. """
    logging.info('Processing %s...',template_file)
    template_name = template_file.strip(".twb")

    for twb_element in LIST_TWB_ELEMENTS:

        get_datasources(twb_element, template_file, template_name)
        if twb_element == "worksheet":
            get_fields(twb_element, template_file, template_name)

    create_fields_by_data_source_csv()
    create_data_sources_by_dashboard_csv()
    create_data_sources_by_worksheet_csv()
    combine_csv_files(output_filename)


if __name__ == "__main__":
    main()

