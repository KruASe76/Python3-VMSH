list1 = ["qwe", "qqwerty",            "asdfghjkl;';lkjhgf", "dcs", "wsedfrghjkl", ""]
list2 = ["d",   "dtwgcyuhsijokmpl,;", "dfecsdverf",         "",    "dcewdc",      "489653165165", "string only in one dict"]

res_list = map(lambda str1, str2: str1 if len(str1) >= len(str2) else str2, list1, list2)
print(*res_list, sep="\n")