'''
有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
'''
def dict_type(list):
    list_dict={}
    dict_d2_key=['姓名','年龄','性别','编号','任职公司','薪资','部门编号']
    for i in range(len(list)):
        list_dict.update({list[i][0]:{}})
        for j in range(len(list[i])):
            list_dict[list[i][0]].update({dict_d2_key[j]:list[i][j]})
    return list_dict

names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]

a=dict_type(names)
for i in a:
    print(i)
    print(a[i])