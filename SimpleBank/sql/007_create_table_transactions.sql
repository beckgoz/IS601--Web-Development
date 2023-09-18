CREATE TABLE
    IS601_Bank_Transactions(
        id int UNIQUE AUTO_INCREMENT PRIMARY KEY,
        account_src VARCHAR(12) NOT NULL,
        account_dest VARCHAR(12) NOT NULL,
        balance_change int NOT NULL,
        transaction_type VARCHAR(20) NOT NULL,
        memo text NOT NULL,
        expected_total int NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        CONSTRAINT ZeroTransferNotAllowed CHECK(balance_change != 0)
    )