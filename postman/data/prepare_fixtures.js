const path = require("path");
const sqlite3 = require(path.resolve(__dirname, "../../eshop-sut/backend/node_modules/sqlite3")).verbose();

const databasePath = path.resolve(__dirname, "../../eshop-sut/backend/database.sqlite");
const db = new sqlite3.Database(databasePath);

function run(sql, params = []) {
  return new Promise((resolve, reject) => {
    db.run(sql, params, function (error) {
      if (error) reject(error);
      else resolve(this);
    });
  });
}

async function prepare() {
  const users = [
    ["User B", "user-b@example.test", "UserBPass1!", "user", 0, null],
    ["Existing User", "existing@example.test", "ExistingPass1!", "user", 0, null],
    ["Isolated Success", "isolated-success@example.test", "FixturePass1!", "user", 0, null],
    ["Elapsed Lock", "elapsed-lock@example.test", "FixturePass1!", "user", 4, "2000-01-01T00:00:00.000Z"],
    ["Two Failures", "two-failures@example.test", "FixturePass1!", "user", 2, null],
  ];

  for (const user of users) {
    await run("DELETE FROM users WHERE email = ?", [user[1]]);
    await run(
      "INSERT INTO users (name,email,password,role,login_attempts,locked_until) VALUES (?,?,?,?,?,?)",
      user,
    );
  }

  await run("DELETE FROM coupon_usage WHERE user_id IN (1001,1002)");
  await run("INSERT INTO coupon_usage (coupon_id,user_id) VALUES (3,1001),(3,1001)");
  await run("INSERT INTO coupon_usage (coupon_id,user_id) VALUES (3,1002),(3,1002),(3,1002)");

  await run("DELETE FROM coupons WHERE code = 'DUP001'");
  await run(
    "INSERT INTO coupons (code,type,discount_value,min_order_amount,expired_at,is_active,max_uses_per_user) VALUES ('DUP001','fixed',1,0,'2099-12-31',1,1)",
  );
}

prepare()
  .then(() => {
    console.log("HW06 deterministic fixtures prepared.");
    db.close();
  })
  .catch((error) => {
    console.error(error);
    db.close();
    process.exitCode = 1;
  });
