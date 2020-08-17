# Input = [
#             {'item': 'apple', 'count': 2},
#             {'item': 'apple', 'count': 3},
#             {'item': 'mango', 'count': 2},
#             {'item': 'orange', 'count': 2}
#         ]
# #Output = [{'item' : 'apple', 'count': 5}, {'item' : 'mango', 'count': 2}]
#
# output = set()
# dict = {}
#
# for i in range(len(Input)):
#     output.add(Input[i]['item'])
#
# for i in range(len(Input)):
#     if Input[i]['item'] not in output:
#         dict['item'] = Input[i]['item']
#         dict['count'] = Input[i]['count']
#         output.append(dict)
#     else:
#         dict['count'] += Input[i]['count']
#         output.append(dict)
#
# print(output)

#----------------- akanksha -----------------------
# my_input = [{"item" : "apple", "count": 2}, {"item" : "apple", "count": 3}, {"item" : "mango", "count": 2}]
# my_output = [{"item" : "apple", "count": 5}, {"item" : "mango", "count": 2}]
#
# already_present = []
# new = {}
# for  i in my_input:
#     if i["item"] not in already_present:
#         already_present.append(i["item"])
#         new[i["item"]] = i["count"]
#     else:
#         print (new[i["item"]])
#         new[i["item"]] = new[i["item"]] + i["count"]
#
# print (already_present)
# print (new)
#
# final = []
# for i in new:
#     final.append({"item":i,"count":new[i]})
#
# print (final)


#------------------------------------rohit -----------------------
Input = [{'item' : 'apple', 'count': 2}, {'item' : 'apple', 'count': 3}, {'item' : 'mango', 'count': 2}]
Output = [{'item' : 'apple', 'count': 5}, {'item' : 'mango', 'count': 2}]

item_name_map = {}
for data in Input:
    item_name = data['item']
    item_count = data['count']
    if item_name in item_name_map:
        item_name_map[item_name]['count'] += item_count
    else:
        item_name_map[item_name] = data
print(list(item_name_map.values()))