from pyspark import SparkContext
from pyspark.sql import SparkSession
from operator import add


sc = SparkContext(appName='spark_app')
spark_sesiion = SparkSession(sc)
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


df = rdd.toDF()

#
sc._jsc.hadoopConfiguration().set("fs.s3.awsAccessKeyId", "")
sc._jsc.hadoopConfiguration().set("fs.s3.awsSecretAccessKey", "")

# df = sc.read \
#   .format("com.databricks.spark.redshift") \
#   .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
#   .option("dbtable", "my_table") \
#   .option("tempdir", "s3n://path/for/temp/data") \
#   .load()
#
# # Read data from a query
# df = sc.read \
#   .format("com.databricks.spark.redshift") \
#   .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
#   .option("query", "select x, count(*) my_table group by x") \
#   .option("tempdir", "s3n://path/for/temp/data") \
#   .load()

# Write back to a table
df.write \
  .format("com.databricks.spark.redshift") \
  .option("url", "jdbc:redshift://redshift-cluster-1.cipctqoqgqrk.eu-central-1.redshift.amazonaws.com:5439/dev?user=awsuser&password=Frnkvnkl12") \
  .option("dbtable", "my_table_copy") \
  .option("tempdir", "s3n://testcarmel/spark") \
  .mode("error") \
  .save()
