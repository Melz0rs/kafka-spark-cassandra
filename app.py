from pyspark import SparkContext
from operator import add
import re


sc = SparkContext(appName='spark_app')
source_file = 'user_actions.txt'

log4jLogger = sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)

input = sc.textFile('log.txt')

# input = input.map(lambda x: x.split('\n'))\
#              .map(lambda x: x[0].split('\t'))
#              .map(lambda x: )

rdd = input.flatMap(lambda x: x.split('\t'))\
              .filter(lambda x: x in ['facebook', 'twitter', 'bing'])\
              .map(lambda x: (x, 1))\
              .reduceByKey(add)


a = rdd.collect()

logger.info(a)



# input = sc.textFile("yourfile.csv").map(lambda line: line.split(","))
# df = sc.read.format("csv").option("header", "true").load(source_file)

# input = input.map(lambda x: x['product'] = (x['product'], 1))  # .filter(lambda x: x.split('\n')).map(lambda x: x[0].split('\t'))

# input = input.collect()

# logger.info(input)




