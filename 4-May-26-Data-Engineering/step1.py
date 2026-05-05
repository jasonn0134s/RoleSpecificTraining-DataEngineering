import dlt
from pyspark.sql.functions import *
@dlt.table
def bronze_patient_visit():
    data = [
        (1001,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (1002,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (1003,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (1004,"Priya Nair","Bangalore","Cardiology",5000,2),
        (1005,"Vikram Singh","Chennai","Neurology",7000,1),
        (1006,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (1007,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (1008,"Meera Iyer","Bangalore","Dermatology",1500,2),
        (1009,"Farhan Ali","Hyderabad","Neurology",7000,1),
        (1010,"Divya Menon","Kochi","Cardiology",5000,1)
    ]
    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "consultation_fee",
        "number_of_tests"
    ]
    return spark.createDataFrame(data, columns)