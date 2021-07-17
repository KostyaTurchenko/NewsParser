# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from config import config
import os
import psycopg2



class CrawlerPipeline:
    # Use to connect to postgresql db
    # def open_spider(self, spider):
    #     """ Connect to the PostgreSQL database server """
    #     try:
    #         # read connection parameters from sys variable
    #         params = config(os.environ['DATA_BASE'])
    #
    #         # connect to the PostgreSQL server
    #         print('Connecting to the PostgreSQL database...')
    #         self.connection = psycopg2.connect(**params)
    #
    #         # create a cursor
    #         self.cur = self.connection.cursor()
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)

    def process_item(self, item, spider):
        return item
