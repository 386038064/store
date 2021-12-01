def repeat_num(_list):
    result={}
    for i in range(len(_list)):
        time=0
        for j in range(len(_list)):
            if _list[i]==_list[j]:
                time+=1
        result.update({_list[i]:time})
    return result
_list=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
print(repeat_num(_list))
