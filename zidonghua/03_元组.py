

tuple1 = ()
tuple2 = (1, "a", '你好', ["哈哈", "嘻嘻"], {"hello", "hi"}, (2, 3, 4))

tuple3 = (3,)
print(tuple1, tuple2)
print(type(tuple3))
print(len(tuple2))
print(tuple2.index("你好"))
print(tuple2[3])
print(tuple2[-2])
print(tuple2[0:3])
print(tuple2[0:5:2])
