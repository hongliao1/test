import os


class GetPath:

    def get_itme_path(self):
        try:
            path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # print(path1)
            return path1
        except Exception as f:
            print('error:%s' % f)


path = GetPath().get_itme_path()
# base路径
base_path = os.path.join(path, 'base')
# print(base_path)

# case路径
case_path = os.path.join(path, 'case')

# config路径
config_path = os.path.join(path, 'config')

# data_files路径
data_files_path = os.path.join(path, 'data_files')

# pages路径
pages_path = os.path.join(path, 'pages')

# report路径
report_path = os.path.join(path, 'report')

