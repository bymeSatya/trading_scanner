import pyspark.sql.functions as F
from config import *

def detect_hammer(df):
    df_pattern_detection = df.withColumn("is_hammer",F.when((F.col("Body") > 0) & (F.col("Lower_wick") >= F.col("Body") * LOWER_WICK_MULTIPLIER) & (F.col("Upper_wick") < F.col("Body") * MAX_UPPER_WICK_RATIO) & (F.col("Body")/F.col("Total_Range") < MAX_BODY_RATIO),True).otherwise(False))
    return df_pattern_detection