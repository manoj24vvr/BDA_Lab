#Python Code Q1

from pyspark.sql.functions import sum
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#Create a SparkSession by calling the builder method:
sc=SparkContext.getOrCreate()
spark=sc.builder.appName("Employee Salaries").getOrCreate()

lines = spark.sc.textFile("spark244/employeeSal.csv") \
                          .filter(lambda line: not line.startswith("department"))
salarySum = lines.flatMap(lambda line: [(line.split(",")[0], float(line.split(",")[1]))]) \
                 .reduceByKey(lambda a, b: a + b) \
                 .toDF(["department", "total_salary"]) \
                 .orderBy(col("total_salary").desc())
# Show results
salarySum.show()
