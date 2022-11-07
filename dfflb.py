from difflib import get_close_matches
import time
from leven import lev_dist

def difflibScore(newpass):
    # file_name = "smallsample.txt"
    file_name = "passwords.txt"
    txt_file = open(file_name)
    z = set()
    z = []
    count = 0
    # print("difflib appraoch")
    start = time.time()
    for line in txt_file:
        # we can process file line by line here, for simplicity I am taking count of lines
        # print(len(line))
        # print(lev_dist("password", "adiy"))
        # t = lev_dist(line, "adiy")
        z.append(line.strip())
        # z.add(line.strip())
        count += 1

    txt_file.close()

    end = time.time()
    print("Execution time in seconds: ", (end - start))
    a = get_close_matches(newpass, z, 5)
    print("Entered Password: "+newpass)
    print(a)
    for i in a:
        print(i, lev_dist(newpass, i))

difflibScore("adit")
