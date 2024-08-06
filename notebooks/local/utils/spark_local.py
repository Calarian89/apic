from pyspark.sql import SparkSession


def get_spark_session(app_name_suffix="") -> SparkSession:
    return (
        SparkSession.builder.appName("local_scom" + app_name_suffix)
        .enableHiveSupport()
        .getOrCreate()
    )
