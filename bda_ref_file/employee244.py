from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.functions import col
#Create a SparkSession by calling the builder method:
spark=SparkSession.builder.appName("Employee Salaries").getOrCreate()

#Load the CSV file into a PySpark DataFrame:



employee_df =spark.read.format("csv").option("header","true").load("/home/hdoop/spark244/employee.csv")



#group the data by department and calculate the sum of salaries:
sum_df=employee_df.groupBy(col("Department")).agg(sum(col("Salary")))

#Display the results to the console:
sum_df.show()
#Complete the application by adding the following code to stop the SparkSession:
spark.stop()



