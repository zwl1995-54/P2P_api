import json
import os

import pytest

import app


# fileName: str
def json_util(fileName: str, methodName: str, paramNames: str):
    # fileName = "img_verify_code.json"
    # 判断传过来的字符串
    if fileName is not None:
        # 判断是不是json文件
        if fileName.endswith(".json"):
            filePath = app.BASE_PATH + "%s%s%s" % (os.sep, "data", os.sep) + fileName
            # print("xxxxxxxxxx", filePath)
            # 判断文件是否存在
            if os.path.exists(filePath):
                data_list = []
                with open(filePath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    data_case = data.get(methodName)
                    for ele in data_case:
                        params_list = []
                        for param in paramNames.split(","):
                            params_list.append(ele.get(param))
                        data_list.append(params_list)
                    # print(data_list)
                    return data_list
            else:
                raise ("文件不存子")
        else:
            raise ("请传入.json格式的文件")

    else:
        raise ("请传需解析json文件的名称")


if __name__ == '__main__':
    pytest.main()
