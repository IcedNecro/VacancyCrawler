# VacancyCrawler

## 0. Initial setup
 
 1. Create PostgreSQL database and configure connection to it in *settings.py* file
 2. Run local ElasticSearch instance. It should work on localhost:9200

## 1. Run scrapy

 1. Install scrapy ``` pip install Scrapy ``` (without virtualenv)
 2. Install dependencies globally to use scrapy crawler
     ```
     pip install sqlalchemy
     pip install psycopg2
     pip install elasticsearch
     ```
 3. Run crawlers
     ```
     scrapy crawl monster-crawler
     scrapy crawl stepstone-crawler
     ```

## 2. Run webinterface

 1. ``` virtualenv .env ```
 2. ``` source .env/bin/activate ```
 3. ``` pip install -r requirements.txt ```
 4. ``` bower install ```
 5. ``` python server.py ```
