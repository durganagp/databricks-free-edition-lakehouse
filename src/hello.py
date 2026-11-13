# Databricks notebook source
print("Bundle deploy works")
print(spark.sql("select current_user()").collect())