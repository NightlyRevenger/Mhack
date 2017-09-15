import os
import csv
from sklearn.datasets import load_files
import codecs

def countLines(file):
    row_count = sum(1 for row in file)
    return  row_count


def prepareFile(path):
    file = codecs.open(path, "r", encoding="utf8")
    reader = csv.DictReader(file)
    rowCount = countLines(reader)
    rowCount = 0.8*rowCount
    reader = csv.DictReader(file)
    rootPath = "otz"
    if not os.path.exists(rootPath):
        os.mkdir(rootPath)
    rootPath = "./" + rootPath + "/"
    i = 0
    for row in reader:
        tmpFloat = float(row['reting'])
        tmpInt = round(tmpFloat)
        pathStr = str(tmpInt)
        if not os.path.exists(rootPath + pathStr):
            os.makedirs(rootPath + pathStr)
        f = open(rootPath + pathStr + "/" + str(i) + ".txt", "w",encoding="utf8")
        f.write(row['comment'] + "\n")
        f.write(row['commentNegative'] + "\n")
        f.write(row['commentPositive'])
        f.close()
        i = i + 1
        if i > rowCount:
            break
    return load_files(rootPath, random_state=42)


def createTest(path):
    file = codecs.open(path, "r", encoding="utf8")
    reader = csv.DictReader(file)
    rowCount = countLines(reader)
    rowCount = 0.8 * rowCount
    reader = csv.DictReader(file)

    i = 0
    tstList = list()
    for row in reader:
        if i > rowCount:
            tmpFloat = float(row['reting'])
            tmpInt = round(tmpFloat)
            tmpstr = row['comment'] + "\n"
            tmpstr = tmpstr + row['commentNegative'] + "\n"
            tmpstr = tmpstr + row['commentPositive']
            tstList.append([tmpInt,tmpstr])
        i=i+1
    return tstList