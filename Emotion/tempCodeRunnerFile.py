from nltk.corpus import stopwords

txt = "amir sohail sdfsdf sdfsdf dfds fsdfsdfidf is can this the"
s_W = set(stopwords.words("english"))
def remove(txt):
    words = txt.split()
    cleaned = []
    for i in words:
        if not i in s_W:
            cleaned.append(i)
    return list(' '.join(cleaned))

print(remove)