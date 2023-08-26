import time

def IR1A():
    t1 = time.process_time_ns()
    f = open("bible.txt", "r")
    docs = f.readlines()
    f.close()
    t2 = time.process_time_ns()
    print(f"The Time to Read Collection of documents IR1A: {t2 - t1} ")

    t3 = time.process_time_ns()
    word1 = 'punishment'
    word2 = 'transgressions'
    for i in range(len(docs)):
        if word1 in docs[i] and word2 in docs[i]:
            pass
            #print(i, docs[i])
    t4 = time.process_time_ns()
    print(f"The Time for Boolean Retrieval IR1A: {t4 - t3} ")

def IR1B():
    t1 = time.process_time_ns()
    f = open("bible.txt", "r")
    docs = f.readlines()
    f.close()
    t2 = time.process_time_ns()
    print(f"The Time to Read Collection of documents IR1B: {t2 - t1} ")

    t3 = time.process_time_ns()
    invertedIndex = {}
    for i in range(len(docs)):
        for s in docs[i].split():
            if invertedIndex.get(s) == None:
                invertedIndex.update({s : {i}})
            else:
                invertedIndex.get(s).add(i)
    t4 = time.process_time_ns()
    print(f"The Time to make inverted index IR1B: {t4 - t3} ")

    t5 = time.process_time_ns()
    word1 = 'punishment'
    word2 = 'transgressions'
    for j in invertedIndex.get(word1) & invertedIndex.get(word2):
        pass
        #print(j, docs[j])
    t6 = time.process_time_ns()
    print(f"The Time for Boolean Retrieval IR1B: {t6 - t5} ")

if __name__ == "__main__":
    IR1A()
    IR1B()