import dlt
from pyspark.sql.functions import *
@dlt.table
def gold_patient_summary():    
    df = dlt.read("silver_patient_visit")    
    result = df.groupBy("city", "department") \
        .agg(
            count("visit_id").alias("total_patients"),
            sum("number_of_tests").alias("total_tests"),
            sum("total_bill").alias("total_revenue")
        )
    
    return result