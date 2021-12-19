import yaml


class ReadYaml:
    # case_path =''
    def readyaml(self, data_path, args):
        if data_path is '':
            return {}
        with open(data_path, encoding='utf-8') as f:
            data_1: dict = yaml.safe_load(f)
        if len(args) == 0:
            return data_1
        else:
            # for key, value in data_odd.items():
            for i in range(len(args)):
                data_1['odd%s' % (i+1)] = args[i]
            return data_1
