import findspark

def setup_spark_session(app_name):
    """Setup the spark session for the application using the SparkSession from pyspark.
    Args:
        app_name: The name of the application
    Returns:
        spark: The SparkSession object
    """
    # Locate the Spark installation and make the necessary initializations
    findspark.init()

    from pyspark.sql import SparkSession

    # Create a SparkSession
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark