from sq_cls import *

db = Database()

db.create()

# db.insert("123123", "Hardwell")

print(db.select("123123"))

db.update_location("123123", "1239.0, 12394.5")
