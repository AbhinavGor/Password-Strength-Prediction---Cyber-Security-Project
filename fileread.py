# # from time import time

# # with open('rockyou.txt',encoding='utf8') as f:
# #     lines = f.read().splitlines()
# # print(len(lines))
# import fileinput
# import time

# # time at the start of program is noted
# start = time.time()

# # keeps a track of number of lines in the file
# count = 0
# # for lines in fileinput.input(['rockyou.txt']):
# for lines in fileinput.input(['smallsample.txt']):
#     # print(lines)
#     count = count + 1

# # time at the end of program execution is noted
# end = time.time()


# print("Execution time in seconds: ", (end - start))
# print("No. of lines printed: ", count)
# import ftfy
# import resource
import os
import time
# import spacy
from leven import lev_dist
# nlp = spacy.load('en_core_web_lg')

# def getsimi(w1, w2):
#     words = w1+" "+w2
#     tokens = nlp(words)

#     for token in tokens:
#         # Printing the following attributes of each token.
#         # text: the word string, has_vector: if it contains
#         # a vector representation in the model,
#         # vector_norm: the algebraic norm of the vector,
#         # is_oov: if the word is out of vocabulary.
#         print(token.text, token.has_vector, token.vector_norm, token.is_oov)

#     token1, token2 = tokens[0], tokens[1]

#     print("Similarity:", token1.similarity(token2))


file_name = "smallsample.txt"
newpass = "alvin1"

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name)
z = []
count = 0
start = time.time()
for line in txt_file:
    # we can process file line by line here, for simplicity I am taking count of lines
    # print(len(line))
    # print(lev_dist("password", "adiy"))
    t = lev_dist(line, newpass="alvin1")
    z.append(t)
    count += 1

txt_file.close()
end = time.time()
print("Execution time in seconds: ", (end - start))

print(f'Number of Lines in the file is {count}')
print(min(z), max(z))
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)
# getsimi("password", "password1")
