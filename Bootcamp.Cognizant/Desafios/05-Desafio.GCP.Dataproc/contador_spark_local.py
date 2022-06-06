#!/usr/bin/env python
# -*- coding: utf-8 -*-

import findspark
from pyspark import SparkContext

if __name__ == "__main__":
    findspark.init()

    sc = SparkContext(appName="PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("livro.txt").flatMap(
        lambda line: line.split(" ")
    )
    wordCounts = (
        words.map(lambda word: (word, 1))
            .reduceByKey(lambda a, b: a + b)
            .sortBy(lambda a: a[1], ascending=False)
    )
    wordCounts.saveAsTextFile("total_palavras_new.txt")
