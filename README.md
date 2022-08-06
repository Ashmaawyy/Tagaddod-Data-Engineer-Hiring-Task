# Tagaddod-Data-Engineer-Hiring-Task

- In this task I will try to build an ETL pipeline that extracts longitude, latitude and some meta data from json files, then transforms it to a csv format that data analysts can use to build a history map.
- There are several aproaches to such a task, one of wich we can use apache airflow to handle the schedule of running the python sccripts that will transform and extract the data, and use apache kafka to handle the consumtion of the extracted and the transformed data where the extracted data is loaded into a data-lake/data-warehouse and the transformed data is fed to the analyst's map.
