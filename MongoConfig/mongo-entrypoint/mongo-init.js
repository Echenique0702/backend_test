// # #!/usr/bin/bash

print(
  "Start #################################################################"
);

db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);
db.createUser({
  user: process.env.DB_USER,
  pwd: process.env.DB_PASSWORD,
  roles: [{ role: "readWrite", db: process.env.MONGO_INITDB_DATABASE }],
});
print("END #################################################################");
