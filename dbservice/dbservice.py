from sqlalchemy import create_engine
import configparser
config = configparser.RawConfigParser()
config.read('/Users/ashu/Documents/workspaces/python/rms-service/config.properties')
db_conf = dict(config.items('DB_SECTION'))

engine = create_engine(db_conf['db_url'], echo = True)
