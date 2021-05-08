
from datetime import datetime


def open_file(file_name='input.txt'):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return data


def create_list_of_dicts(data):
    headers = data[0].strip(' ').strip('\n').split(',')
    data = data[1:]
    data_str_dic = []
    for data_row in data:
        data_str_dic.append(dict(zip(headers, data_row.split(','))))
    for i in range(len(data_str_dic)):
        data_str_dic[i]['date'] = datetime.strptime(data_str_dic[i]['date'], '%Y-%M')
    return data_str_dic


def filter_data(data, key, value):
    return list(filter(lambda elem: elem[key] == value, data))


def sort_data(data, sort_key):
    return sorted(data, key=lambda k: k[sort_key])

def main(file_name):
    data = open_file(file_name)
    data_str_dic = create_list_of_dicts(data)
    filtered_data = filter_data(data_str_dic, 'resource', '118')
    sorted_data = sort_data(data_str_dic, 'date')
    print(data)
    print(data_str_dic)
    print(filtered_data)
    print(sorted_data)


if __name__ == '__main__':
    main('input.txt')