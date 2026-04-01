from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("Salary ETL").getOrCreate()

df = spark.read.csv("data/employees.csv", header=True, inferSchema=True)

df = df.dropna()

df = df.withColumn(
    "salary_category",
    when(col("salary") > 80000, "HIGH")
    .when(col("salary") > 50000, "MEDIUM")
    .otherwise("LOW")
)

df.show()
