set1 = set(input("Input a word: "))
set2 = set(input("Input another word: "))
list1 = list(set1)
list2 = list(set2)
print(list1, list2)


def one(alist1, alist2):
    overall = []
    overall.extend(alist1)
    overall.extend(alist2)
    overall = set(overall)
    print(f"Letters that appear in at least one of the two words. {overall}")


def common(alist1, alist2):
    commonlist = []
    for n in alist1:
        if n in alist2:
            commonlist.append(n)
    for n in alist2:
        if n in alist1:
            commonlist.append(n)
    commonlist = list(set(commonlist))
    print(f"letters that appear in both words {commonlist}")


def none(alist1, alist2):
    nonelist = []
    for n in alist1:
        if n not in alist2:
            nonelist.append(n)
    for n in alist2:
        if n not in alist1:
            nonelist.append(n)
    nonelist = list(set(nonelist))
    print(f"Letters that appear in either word, but not in both. {nonelist}")


one(list1, list2)
common(list1, list2)
none(list1, list2)
