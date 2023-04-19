CREATE TABLE
    IS601_Bank_Accounts(
        id int UNIQUE AUTO_INCREMENT PRIMARY KEY,
        account_number varchar(12) UNIQUE DEFAULT (LPAD(user_id, 12, "0")),
        user_id int NOT NULL,
        balance int DEFAULT 0,
        account_type VARCHAR(20) NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )