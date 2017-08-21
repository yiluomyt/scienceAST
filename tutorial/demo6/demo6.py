from gensim import corpora, models, similarities
import logging
import csv

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
# 打开一个带有id并且已经分词的.txt文档
with open('segementWithID.txt', encoding='utf-8') as f:
    documents = [line.strip() for line in f.readlines()]
# 将文章中#后部分即内容赋值到texts列表
texts = [document.split('#')[1].split(',') for document in documents]
# 将#前部分即id赋值到id列表
id = [document.split('#')[0] for document in documents]
# 利用.txt文档中所有文章创建字典
dictionary = corpora.Dictionary(texts)
# 将文章标号
corpus = [dictionary.doc2bow(text) for text in texts]
# 创建tfidf模型
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
# 创建lsi分析文本模型
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
# 保存lsi模型
lsi.save('./lsi.model')
# 创建索引
index = similarities.MatrixSimilarity(lsi[corpus])
# 打开.csv文件将结果写入其中
result = open('result.csv', 'w', newline='', encoding='utf-8')
# 总共有72527条数据(可以先由读取.txt文档行数得到)
for i in range(0, 72527):
    list = []
    query = texts[i]
    query_bow = dictionary.doc2bow(query)
    query_lsi = lsi[query_bow]
    sims = index[query_lsi]
    # 将相似度从高到低排序取不包括自身的前十个
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])[1:11:]
    # 将结果tuple赋值进list列表
    list.append(id[i])
    for tuple in sort_sims:
        # 取tuple中的id部分
        list.append(id[tuple[0]])
    # 将结果写入.csv文件
    writer = csv.writer(result)
    writer.writerow(list)
result.close()
