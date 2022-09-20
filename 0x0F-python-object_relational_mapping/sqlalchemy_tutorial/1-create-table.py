#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import DateTime, Boolean, Table, Column, String, Text, MetaData
from datetime import datetime

metadata = MetaData()

blog = Table(
    'blog', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200), nullable=False),
    Column('content', Text(), nullable=False),
    Column('published', Boolean(), default=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
    )