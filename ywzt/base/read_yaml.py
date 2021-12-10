import yaml


class ReadYaml:
    # case_path =''
    def readyaml(self, data_path, data_odd: dict):
        if data_path is '':
            return {}
        with open(data_path, encoding='utf-8') as f:
            data_1: dict = yaml.safe_load(f)
        if data_odd is None:
            return data_1
        else:
            for key, value in data_odd.items():
                data_1[key] = value
            return data_1
