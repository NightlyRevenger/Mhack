
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import prepareCsv
import  csv


path = "./X_train.csv"

train = prepareCsv.prepareFile(path)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train.data)

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, train.target)

tstL = prepareCsv.createTest(path)
docs_new = list()

for item in tstL:
    docs_new.append(item[1])

X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)

field1 = 'Comment'
field2 = 'Calculated'
field3 = 'Real'

with open("ressult.csv", "w") as csvfile:
    fieldnames = [field1, field2, field3]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for doc, category, item in zip(docs_new, predicted,tstL):
        writer.writerow({field1: doc, field2: train.target_names[category],field3:item[0]})