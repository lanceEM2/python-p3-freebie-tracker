#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create instances of Company, Dev, and Freebie
company = Company(name='Example Company', founding_year=2020)
dev = Dev(name='John Doe')
freebie = Freebie(item_name='Example Item', value=10, dev=dev, company=company)

# Add instances to the session and commit
session.add_all([company, dev, freebie])
session.commit()