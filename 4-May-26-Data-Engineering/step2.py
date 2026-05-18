import dlt
from pyspark.sql.functions import *

@dlt.table
def silver_patient_visit():   
    df = dlt.read("bronze_patient_visit")    
    df = df.withColumn("department", upper(col("department")))    
    df = df.withColumn("test_cost", col("number_of_tests") * 2000)    
    df = df.withColumn("total_bill", col("consultation_fee") + col("test_cost"))
    
    return df