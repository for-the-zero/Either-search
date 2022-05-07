'''
def find(lf_link,l1,l2):
    lf = [lf_link,[]]
    l1_title = l1[1]
    l2_title = l2[1]
    #将lf_link中的链接按照索引寻找到对应的标题和文本，如果在l1_title与l2_title冲突，则选择字数多者，并输出[链接,标题]
    for i in lf_link:
        if i in l1_title:
            lf[1].append([i,l1_title[l1_title.index(i)]])
        elif i in l2_title:
            lf[1].append([i,l2_title[l2_title.index(i)]])
        else:
            lf[1].append([i,None])
    return lf
'''


def inone(l1,l2):
    l1_link = l1[0]
    l2_link = l2[0]
    #将l1_link和l2_link去重
    l1_link = list(set(l1_link))
    l2_link = list(set(l2_link))
    #将l1_link和l2_link用字典存储从1开始的索引
    l1_link_dict = {}
    l2_link_dict = {}
    for i in range(len(l1_link)):
        l1_link_dict[l1_link[i]] = i+1
    for i in range(len(l2_link)):
        l2_link_dict[l2_link[i]] = i+1
    #将l1_link和l2_link的键合并至lf_link一个字典，如果键有重复，则取两个索引的平均值作为索引，否则将索引乘以1.5作为索引
    lf_link = {}
    for i in l1_link:
        if i in l2_link:
            lf_link[i] = (l1_link_dict[i]+l2_link_dict[i])/2
        else:
            lf_link[i] = l1_link_dict[i]*1.5
    for i in l2_link:
        if i in l1_link:
            continue
        else:
            lf_link[i] = l2_link_dict[i]*1.5
    #将lf_link按照索引排序，从小到大，如果有相同则按l1_link_dict中顺序排序，如果l1_link_dict没有相同则按l2_link_dict中顺序排序
    lf_link = sorted(lf_link.items(),key=lambda x:x[1])
    lf_link = [i[0] for i in lf_link]
    #return find(lf_link,l1,l2)
    return [lf_link]

'''
#测试上面的程序
l1 = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','l','m','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','l']]]
#乱序的l1
l2 = [['a','d','e','f','u','c','k','y','o','u','m','a','n'],[['1','2','3','4','5','6','7','8','9','10','11','12','13'],['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','l','m']]]
print(inone(l1,l2))
'''

def debuglist(list):
    # list[0]和list[1]的项目数中如果不相同，将数量多的列表从后面删除到相同项目数
    list_link = list[0]
    list_title = list[1]
    if len(list_link) != len(list_title):
        if len(list_link) > len(list_title):
            list_link = list_link[:len(list_title)]
        else:
            list_title = list_title[:len(list_link)]
    return [list_link,list_title]