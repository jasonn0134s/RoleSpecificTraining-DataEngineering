

# install pyspark
!pip install pyspark

# upload csv file
from google.colab import files

uploaded = files.upload()

# create spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder \
    .appName("SmartHomeETL") \
    .getOrCreate()

# load csv file
df = spark.read.csv(
    "energy_usage.csv",
    header=True,
    inferSchema=True
)

# display original dataset
print("Original Dataset")
df.show()

# room wise energy summary
room_summary = df.groupBy("room_id").agg(
    sum("energy_kwh").alias("total_energy"),
    avg("energy_kwh").alias("average_energy")
)

print("Room Wise Energy Summary")
room_summary.show()

# device wise energy summary
device_summary = df.groupBy("device_id").agg(
    sum("energy_kwh").alias("total_energy"),
    avg("energy_kwh").alias("average_energy")
)

print("Device Wise Energy Summary")
device_summary.show()

# top energy consuming devices
top_devices = device_summary.orderBy(
    "total_energy",
    ascending=False
)

print("Top Energy Consuming Devices")
top_devices.show()

# save output csv
top_devices.toPandas().to_csv(
    "top_devices_output.csv",
    index=False
)

# download output file
files.download("top_devices_output.csv")

# stop spark session
spark.stop()