import os


def get_path():
    path_list = os.path.split(os.path.realpath(__file__))[0]
    path = os.path.join(path_list + "/" + "testcase.xlsx")
    return path


def get_path_list():
    path_list = os.path.abspath(os.path.dirname(os.getcwd()))
    return path_list


if __name__ == "__main__":
    print("路径为:", get_path())
    print("路径为:", get_path_list())
