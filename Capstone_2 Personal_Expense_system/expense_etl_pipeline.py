!pip install pyspark

from google.colab import files
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

uploaded = files.upload()

spark = SparkSession.builder \
    .appName("ExpenseETLPipeline") \
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

category_summary = df.groupBy("category") \
    .agg(
        sum("amount").alias("total_category_expense")
    )

print("Category Wise Expense Summary")

category_summary.show()

high_spending_users = user_summary.filter(
    user_summary.total_expense > 1500
)

print("High Spending Users")

high_spending_users.show()

high_spending_users.toPandas().to_csv(
    "high_spending_users.csv",
    index=False
)

files.download("high_spending_users.csv")

print("ETL Pipeline Executed Successfully")

spark.stop()