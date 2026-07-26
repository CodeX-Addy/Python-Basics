example = [4, 378, 33, 37]

greater_than_four = (temp for temp in example if temp > 4)

print(greater_than_four)

## output: <generator object <genexpr> at 0x7d7ec2679d80> ..... it is basically stream of elements
