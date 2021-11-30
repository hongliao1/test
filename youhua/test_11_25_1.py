def dameps():
    data = {'name': "laio", 'passwd': '00'}
    a = 'xxxxx${name}llll'
    for key, value in data.items():
        str = a.replace(f'${{{key}}}', value)
        print(str)
dameps()