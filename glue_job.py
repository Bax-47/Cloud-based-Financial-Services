import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database="my_database", table_name="my_table", transformation_ctx="datasource0")
applymapping1 = ApplyMapping.apply(frame=datasource0, mappings=[("col0", "string", "col0", "string"), ("col1", "int", "col1", "int")], transformation_ctx="applymapping1")
datasink2 = glueContext.write_dynamic_frame.from_options(frame=applymapping1, connection_type="s3", connection_options={"path": "s3://my-bucket/transformed/"}, format="json", transformation_ctx="datasink2")

job.commit()
