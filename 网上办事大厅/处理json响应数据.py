import json
import os

# 读取JSON文件并指定编码格式为'utf-8'
with open('7-4数据.json', 'r', encoding='utf-8') as file:
    response_data = json.load(file)

# 提取name完整属性
names = []
stay_names = []  # 存储满足条件的名称
code_names = []
account_names = []

for entity in response_data['entities']:
    if 'name' in entity:
        name = entity['name']
        names.append(name)
        if name.startswith('寒暑假留校申请_'):
            stay_names.append(name)

# 保存提取的值到新文件
with open('网上办事大厅填写名单.txt', 'w', encoding='utf-8') as file:
    for name in names:
        file.write(name + '\n')

# 将满足条件的名称保存在留校名单文件中
if len(stay_names) > 0:
    with open('2023暑假留校申请名单.txt', 'w', encoding='utf-8') as outfile:
        for name in stay_names:
            outfile.write(name + '\n')

# 只提取事件+姓名
# with open('事件+姓名.txt', 'w', encoding='utf-8') as outfile:
#     # 遍历entities列表
#     for entity in response_data['entities']:
#         # 提取code的name属性
#         code_name = entity['app']['name']
#         # 提取account的name属性
#         account_name = entity['owner']['name']
#
#         # 打印code的name属性和account的name属性
#         output = f"{code_name}   {account_name}\n"
#         print(output)
#
#         # 将数据写入txt文件
#         outfile.write(output)
