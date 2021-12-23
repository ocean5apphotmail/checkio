#  尼古拉喜欢对一切看到的东西进行分类。 有一次，斯蒂芬送了他一个标签机作为他的生日礼物， 机器人把在船上的每个面的标签撕了几个星期。 从那时起，他归类在他的实验室的所有试剂， 图书馆的书和在桌子上笔记。 但后来他得知 python 字典 ，并分类所有索菲亚的机器人的可能的配置。 现在，这些文件被组织在一个很深的嵌套结构， 但索菲亚并不喜欢这样。让我们帮助索菲亚扁平化这些字典。
#
# Python字典是一种可以用来方便地存储和处理配置的数据类型。它允许你通过键来创建嵌套结构来存储数据。您将得到一个字典，其中的键是字符串，值是字符串或字典。我们的目标是使字典扁平化，但保存的结构中的键。其结果应该是一个字典没有嵌套的字典。键应包含原来的字典中的父键的路径。在路径中的键是由以“/”分开。如果值是一个空的字典，那么它应该由一个空字符串（""）所取代。让我们来看一个例子：
# {
#     "name": {
#         "first": "One",
#         "last": "Drone"
#     },
#     "job": "scout",
#     "recent": {},
#     "additional": {
#         "place": {
#             "zone": "1",
#             "cell": "2"}
#     }
# }
#  其结果将是:
#  {"name/first": "One",  # one parent
#   "name/last": "Drone",
#   "job": "scout",  # root key
#   "recent": "",  # empty dict
#   "additional/place/zone": "1",  # third level
#   "additional/place/cell": "2"}
#  1
#  2
#  3
#  4
#  5
#  6
#
#  输入: 作为字典的一个原始字典。
#
#  输出: 作为字典的一个扁平化字典。
#
#  范例:
#  flatten({"key": "value"}) == {"key": "value"}
#  flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
#  flatten({"empty": {}}) == {"empty": ""}
#
#  1
#  2
#  3
#  4
#
#  如何使用： 这个概念在你需要为保持系统和文件结构原状而分析配置文件，简化结构时会有用。 您可以用自己的规格轻松地修改这个想法。 除此之外，它是一个能让你读懂代码和查找漏洞的有用的技能，。
#
#  前提:
#  字典中的
#  Keys
#  是非空的字符串
#  字典中的
#  Values
#  是字典或者字符串
#  root_dictionary != {}
def flatten(dictionary):
    # your code here
    return {}


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
