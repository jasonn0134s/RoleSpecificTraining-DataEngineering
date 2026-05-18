from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

# create spark session
spark = SparkSession.builder \
    .appName("SmartHomeEnergyTracker") \
    .getOrCreate()

# load csv file
df = spark.read.csv(
    "energy_usage.csv",
    header=True,
    inferSchema=True
)

# show dataset
print("Original Dataset")
df.show()

# device wise total energy
device_summary = df.groupBy("device_id") \
    .agg(
        sum("energy_kwh").alias("total_energy"),
        avg("energy_kwh").alias("average_energy")
    )

print("Device Wise Summary")
device_summary.show()

# top energy consuming devices
top_devices = device_summary.orderBy(
    "total_energy",
    ascending=False
)

print("Top Energy Consuming Devices")
top_devices.show()

# stop spark session
spark.stop()