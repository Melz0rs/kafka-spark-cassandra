from pyspark import SparkContext
from operator import add

sc = SparkContext(appName='spark_app')
source_file = 'file:///Users/carmelshupak/Documents//kafka-spark-cassandra/log.txt'

log4jLogger = sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)

input = sc.textFile(source_file)

logger.info("input: ", input.collect())

# print(f"input: {input}")

