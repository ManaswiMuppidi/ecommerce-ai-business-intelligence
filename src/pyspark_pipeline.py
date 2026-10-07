from pyspark.sql import SparkSession, functions as F

spark=SparkSession.builder.appName("EcommerceBigData").getOrCreate()
df=spark.read.option("header",True).option("inferSchema",True).csv("data/ecommerce_orders_large.csv")

clean=df.dropDuplicates(["order_id"]).filter(F.col("revenue")>=0)
summary=clean.groupBy("category").agg(
    F.sum("revenue").alias("revenue"),
    F.sum("profit").alias("profit"),
    F.count("*").alias("orders")
).orderBy(F.desc("revenue"))
summary.show()
spark.stop()
