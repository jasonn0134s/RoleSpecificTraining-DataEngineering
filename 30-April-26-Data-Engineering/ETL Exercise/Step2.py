import dlt
from pyspark.sql.functions import *
@dlt.table
def silver_patient_visits():
    df = dlt.read("bronze_patient_visits")
    df = df.withColumn("department", upper(col("department")))
    df = df.withColumn("test_cost", col("number_of_tests") * 2000)
    df = df.withColumn("total_bill", col("consultation_fee") + col("test_cost"))
    df = df.filter(col("consultation_fee") > 0)
    return df