import yaml


class ReadYaml:
    def readyaml(self, data_path, args):
        if data_path is '':
            return {}
        with open(data_path, encoding='utf-8') as f:
            data_1: dict = yaml.safe_load(f)
        if len(args) == 0:
            # print(data_1)
            return data_1
        else:
            for i in range(len(args[0])):
                data_1['odd%s' % (i+1)] = args[0][i]
            # print(data_1)
            return data_1
