
import yaml


class ReadYaml:
    # data_path =''
    def readyaml(self, data_path):
        if data_path is '':
            return {}
        else:
            with open(data_path,  encoding='utf-8') as f:
                return yaml.safe_load(f)[0]

