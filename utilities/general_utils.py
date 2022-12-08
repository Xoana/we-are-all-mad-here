import yaml
import json

def get_config(config_file):
    ''' Returns a dictionary of the specified config file. '''
    file_type = config_file.split('.')[1]

    if file_type == 'json':
        with open(config_file, 'r') as file_config:
            config_data = json.load(file_config)
    else:
        with open(config_file) as file_config:
            config_data = yaml.load(file_config, Loader=yaml.FullLoader)

    return config_data