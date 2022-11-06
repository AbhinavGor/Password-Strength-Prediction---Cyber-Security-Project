from pybktreespellchecker import BKTree
# bkt = BKTree()  # instance without dictionary and Levenshtein distance function
# instance with dictionary and Levenshtein distance function
# bkt = BKTree(words=['one', 'two', 'three'])

# custom words distance function


def length_distance(w1, w2):
    return abs(len(w1) - len(w2))


# instance with custom distance function and dictionary
# bkt = BKTree(words=['one', 'two', 'three'], distance_func=length_distance)

bkt = BKTree.from_file('smallsample.txt')
# bkt = BKTree.from_file('rockwell.txt')
# bkt = BKTree.from_file('rockyou.txt')
newpass = "aditya"
# newpass = 'jesuscristo'
result = bkt.search(newpass, 3)
for i in result:
    print(i[0], i[1].word)
print(result)