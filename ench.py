import enchant
from munging import invert_munge
d=enchant.Dict("en_US")


print(d.check("Hello"))
print(d.check("Adi"))
print(d.check("@n93l"))
print(d.check(invert_munge("@n93l")))
