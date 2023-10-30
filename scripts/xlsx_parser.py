import pandas as pd
from typing import Dict, List
import datetime
from project.schemes.schemes import ProjectScheme


class FileParser:
    """
    Parser xlsx files.
    """

    def __init__(self):
        self.projects_list: List[ProjectScheme] = []
        self.__file_data_dict: Dict = {}

    def get_file_data(self, file, json=False) -> dict:
        # create DataFrame
        df = pd.read_excel(file)
        date_dict = {}
        # get all the dates
        for date in df:
            if type(date) == datetime.datetime:
                datetime_object = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
                formatted_date = datetime_object.strftime('%Y-%m-%d')
                date_dict[formatted_date] = []

        project_data_dict = {}
        # create Dictionary with full file data
        for item in df.values[1:]:
            project_data_dict[item[1]] = {
                'Code': item[0],
                'Name': item[1]
            }
            for num, date in enumerate(date_dict.keys()):
                if not project_data_dict[item[1]].get('data'):
                    project_data_dict[item[1]]['data'] = {}
                project_data_dict[item[1]]['data'][date] = {'plan': item[2 + num * 2],
                                                            'fact': item[3 + num * 2]}
        if json:
            return project_data_dict
        # save the dictionary to class object
        self.__file_data_dict = project_data_dict

    def create_file_objects(self) -> None:
        for project_name in self.__file_data_dict.keys():
            # create list off ProjectSchema
            self.projects_list.append(ProjectScheme(code=self.__file_data_dict[project_name]['Code'],
                                                    project_name=self.__file_data_dict[project_name]['Name'],
                                                    project_data=self.__file_data_dict[project_name]['data']))
