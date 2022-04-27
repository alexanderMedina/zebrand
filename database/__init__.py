import databases

DATABASE_URL = "postgresql://postgres:postgres@db/zebrand"
db = databases.Database(DATABASE_URL) 