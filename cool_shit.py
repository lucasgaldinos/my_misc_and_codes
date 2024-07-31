# Databricks notebook source
# MAGIC %md
# MAGIC # down here, copy to another notebook

# COMMAND ----------

from delta.tables import DeltaTable
sc.getConf().getAll()  # returns a list with all spark configuration for this cluster

# COMMAND ----------

# MAGIC %md
# MAGIC # table ownership problem
# MAGIC
# MAGIC Can be:
# MAGIC - Vacuum configuration or something like that for delta tables: https://docs.delta.io/latest/api/python/spark/index.html#delta.tables.DeltaTable.vacuum
# MAGIC - Some warehouse configuration or changed config recently.
# MAGIC
# MAGIC https://stackoverflow.com/questions/41886346/spark-2-1-0-session-config-settings-pyspark#:~:text=As%20soon%20as%20you%20start%20pyspark%20shell%20type%3A,Then%20try%20your%20code%20and%20do%20it%20again.
# MAGIC
# MAGIC https://docs.databricks.com/en/delta/delta-change-data-feed.html#enable-change-data-feed set all tables to changedatafeed for the cluster. must be set at cluster level when initializing it.
# MAGIC
# MAGIC https://docs.databricks.com/en/delta/table-properties.html#how-do-table-properties-and-sparksession-properties-interact reference for delta table properties
# MAGIC
# MAGIC maybe table ownership https://kb.databricks.com/data/object-ownership-is-getting-changed-on-dropping-and-recreating-tables?from_search=152981454
# MAGIC
# MAGIC databricks delta tables properties ref https://docs.databricks.com/en/delta/table-properties.html#how-do-table-properties-and-sparksession-properties-interact
# MAGIC
# MAGIC ## spark configurations
# MAGIC
# MAGIC https://spark.apache.org/docs/latest/configuration.html -> some things can be done by spark configuration, but some are using spark.databricks, it depends on the conf and depends on the cluster
# MAGIC
# MAGIC ## databricks config
# MAGIC
# MAGIC - databricks data-engineering reference https://docs.databricks.com/en/workspace-index.html
# MAGIC - Solution https://kb.databricks.com/en_US/dbsql/cannot-customize-apache-spark-config-in-databricks-sql-warehouse
# MAGIC
# MAGIC - databricks conf documentation (obs: when using sc.getConf().getAll(), databricks properties will be written with JAVA naming conventions, as spark is written in JAVA. Though argument references in the provided documentation will be ) https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/cluster and https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/cluster
# MAGIC
# MAGIC ## DATABRICKS API
# MAGIC
# MAGIC https://docs.databricks.com/api/workspace/clusters

# COMMAND ----------

# MAGIC %md
# MAGIC # Replacing specific data
# MAGIC
# MAGIC https://docs.databricks.com/en/delta/selective-overwrite.html

# COMMAND ----------

# MAGIC %md
# MAGIC # cool things about delta tables configuration
# MAGIC https://docs.delta.io/latest/api/python/spark/index.html#
# MAGIC
# MAGIC https://docs.databricks.com/en/delta-live-tables/tutorial-pipelines.html
# MAGIC
# MAGIC https://docs.databricks.com/en/delta/table-properties.html#how-do-table-properties-and-sparksession-properties-interact
# MAGIC
# MAGIC https://docs.delta.io/3.1.0/table-properties.html
# MAGIC
# MAGIC RESTORE TABLE TO VERSION: https://docs.databricks.com/en/delta/history.html#data-retention

# COMMAND ----------


# COMMAND ----------

finance_metrics = DeltaTable.forName(spark, "financecq.dev_finance_metrics")

# COMMAND ----------

finance_metrics.detail().display()

# COMMAND ----------

finance_metrics.replace(spark).tableName(dev_finance_metrics).location(
    "dbfs:/mnt/edl/raw/financecq/pbyp_opening")


# COMMAND ----------

# MAGIC %sql
# MAGIC drop table financecq.dev_finance_metrics2
