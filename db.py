#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import sys
pymysql.install_as_MySQLdb()

#Open connection
con = pymysql.connect('localhost', 'testuser', 'test623', 'testdb')

cursor = con.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS per36qf")
# cursor.execute("DROP TABLE IF EXISTS PLAYERS_PER_GAME")

# Create per game

# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
###########################################
# sql = """CREATE TABLE per36 (
#          NAME  CHAR(50) NOT NULL,
#          POS CHAR(5),  
#          AGE CHAR(2),
#          TM CHAR(3),
#          G CHAR(2),
#          GS CHAR(2),
#          MP CHAR(4),
#          FGM CHAR(5),
#          FGA CHAR(5),
#          FGPERCENTAGE CHAR(5),
#          3PM CHAR(5),
#          3PA CHAR(5),
#          3PPERCENTAGE CHAR(5),
#          2PM CHAR(5),
#          2PA CHAR(5),
#          2PPERCENTAGE CHAR(5),
#          FTM CHAR(5),
#          FTA CHAR(5),
#          FTPERCENTAGE CHAR(5),
#          ORB CHAR(5),
#          DRB CHAR(5),
#          TRB CHAR(5),
#          AST CHAR(5),
#          STL CHAR(5),
#          BLK CHAR(5),
#          TOV CHAR(5),
#          PF CHAR(5),
#          PTS CHAR(5))"""
##########################################
sql = """CREATE TABLE per36qf (
         NAME  CHAR(50) NOT NULL,
         POS CHAR(5),  
         AGE CHAR(2),
         TM CHAR(3),
         G CHAR(2),
         GS CHAR(2),
         MP CHAR(4),
         FGM CHAR(5),
         FGA CHAR(5),
         FGPERCENTAGE CHAR(5),
         3PM CHAR(5),
         3PA CHAR(5),
         3PPERCENTAGE CHAR(5),
         2PM CHAR(5),
         2PA CHAR(5),
         2PPERCENTAGE CHAR(5),
         FTM CHAR(5),
         FTA CHAR(5),
         FTPERCENTAGE CHAR(5),
         ORB CHAR(5),
         DRB CHAR(5),
         TRB CHAR(5),
         AST CHAR(5),
         STL CHAR(5),
         BLK CHAR(5),
         TOV CHAR(5),
         PF CHAR(5),
         PTS CHAR(5))"""
##########################################
# sql = """CREATE TABLE EXPERIMENT (
#          d1 DOUBLE(3,1),
#          d2 DOUBLE(4,3))"""
# sql = """ALTER TABLE EXPERIMENT ADD COLUMN str CHAR(5)"""
##########################################
# sql = """CREATE TABLE TEST (
#          NAME  CHAR(40) NOT NULL,
#          POS CHAR(4),  
#          AGE INT,
#          TM CHAR(3),
#          G INT,
#          GS INT,
#          MP DOUBLE(3,1),
#          FGM DOUBLE(3,1),
#          FGA DOUBLE(3,1),
#          FGPERCENTAGE DOUBLE(4,3),
#          3PM DOUBLE(3,1),
#          3PA DOUBLE(3,1),
#          3PPERCENTAGE DOUBLE(4,3),
#          2PM DOUBLE(3,1),
#          2PA DOUBLE(3,1),
#          2PPERCENTAGE DOUBLE(4,3),
#          eFGPERCENTAGE DOUBLE(4,3),
#          FTM DOUBLE(3,1),
#          FTA DOUBLE(3,1),
#          FTPERCENTAGE DOUBLE(4,3),
#          ORB DOUBLE(3,1),
#          DRB DOUBLE(3,1),
#          TRB DOUBLE(3,1),
#          AST DOUBLE(3,1),
#          STL DOUBLE(3,1),
#          BLK DOUBLE(3,1),
#          TOV DOUBLE(3,1),
#          PF DOUBLE(3,1),
#          PTS DOUBLE(3,1))"""

cursor.execute(sql)

con.close()