from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder \
    .appName("ExpenseMonitoringSystem") \
    .getOrCreate()

df = spark.read.csv(
    "expenses.csv",
    header=True,
    inferSchema=True
)

print("Original Expense Dataset")

df.show()

user_summary = df.groupBy("user_id") \
    .agg(
        sum("amount").alias("total_expense"),
        avg("amount").alias("average_expense")
    )

print("User Wise Expense Summary")

user_summary.show()

high_spending_users = user_summary.filter(
    user_summary.total_expense > 1500
)

print("High Spending Users")

high_spending_users.show()

spark.stop()