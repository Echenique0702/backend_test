// mongo-entrypoint/mongo-init.js

print(
  "Start #################################################################"
);

const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
const dbName = process.env.DB_NAME;

print(dbName);
print(dbPassword);
print(dbUser);
db = db.getSiblingDB(dbName);

db.createUser({
  user: dbUser,
  pwd: dbPassword,
  roles: [{ role: "readWrite", db: dbName }],
});

print("END #################################################################");
