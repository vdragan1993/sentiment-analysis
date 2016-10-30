def prepare_stopwords(input_file, output_file):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    stopwords = []
    for line in lines:
        stopword = line.split()[4]
        stopword = stopword.replace("č", 'c')
        stopword = stopword.replace("ć", "c")
        stopword = stopword.replace("đ", "dj")
        stopword = stopword.replace("š", "s")
        stopword = stopword.replace("ž", "z")

        if stopword not in stopwords:
            stopwords.append(stopword)

    f = open(output_file, 'w')
    for word in stopwords:
        f.write("%s\n" % word)
    f.close()

if __name__ == "__main__":
    prepare_stopwords("../data/stopwords_list.txt", "../data/stopwords.txt")