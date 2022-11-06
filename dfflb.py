from difflib import get_close_matches
import time
newpass = "alvin1"
file_name="smallsample.txt"
txt_file = open(file_name)
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
    count += 1

txt_file.close()

end = time.time()
print("Execution time in seconds: ", (end - start))
a=get_close_matches(newpass, z, 20)
print("Entered Password: "+newpass)
print(a)