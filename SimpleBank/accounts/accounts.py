from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.datastructures import MultiDict
import random

from sql.db import DB
accounts = Blueprint('accounts', __name__, url_prefix='/accounts', template_folder='templates')

"""bag27:4/17/2023 Created path to create accounts.
Since there is nothing for the user to input, when they select
create account a checking account will be created for them. 
A random 12 digit string is created for their account number
and is associated to them via their user_id. A minimum deposit
of $5 is required, which is taken care of automatically in the code.
When an account is created, the user is automatically redirected to the 
account list page."""
@accounts.route("/create", methods=["GET", "POST"])
@login_required
def create():
    user_id = current_user.get_id()
    acc = "%0.12d" % random.randrange(10**12)
    dep = 5
    has_error = False
    #unique = DB.selectOne("SELECT account_number = %s FROM IS601_Bank_Accounts WHERE 1=1", str(acc))
    #if unique.status:
    if user_id:
        try:
            acc_check = DB.selectOne("""SELECT account_number FROM IS601_Bank_Accounts WHERE account_number = %s""", acc)
            if not acc_check:
                has_error = True
                raise Exception("Please try again")
        except Exception as e:
            flash(f"{e}", "warning")
        if not has_error:
            try:
                DB.insertOne("""
                INSERT INTO IS601_Bank_Accounts (account_number, user_id, account_type)
                VALUES (%s, %s, "checking")
                """, str(acc), user_id)
                acc_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = %s
                            """, acc)
                world_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = "000000000000"
                            """)
                query = """
                    INSERT INTO IS601_Bank_Transactions
                    (account_src, account_dest, balance_change, transaction_type, memo, expected_total) VALUES
                    (%s, %s, %s, %s, %s, %s)
                    """
                pairs = []
                pairs.append(("000000000000", acc, dep*-1, "deposit", "Minimum deposit of $5 required", world_bal.row["balance"] + dep *-1))
                pairs.append((acc, "000000000000", dep, "deposit", "Minimum deposit of $5 required", acc_bal.row["balance"] + dep))
                DB.insertMany(query, pairs)
                DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                        (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = %(acc)s)
                        WHERE account_number = %(acc)s
                        """, {"acc":acc})
                DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                        (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = "000000000000")
                        WHERE account_number = "000000000000"
                        """) 
                flash("Account successfully created!", "success")
            except Exception as e:
                print(e)
                flash(f"{e}", "danger")
    #else:
        #flash("Error creating account, please try again.", "danger")
    
    return redirect(url_for("accounts.list"))

"""bag27:4/18/2023 The account list path is used to list all
the user's accounts in a table. The query gets all the unique accounts
associated with the user_id and displays them in a table, and gives the user
an option to see the accounts history via a button."""
@accounts.route("/list", methods=["GET"])
@login_required
def list():
    rows = []
    user_id = current_user.get_id()
    if user_id:
        try:
            result = DB.selectAll("""SELECT account_number, account_type, modified, balance
                                FROM IS601_Bank_Accounts WHERE user_id = %s""", user_id)
            if result.status:
                rows = result.rows
        except Exception as e:
            print(e)
            flash("Error finding accounts", "danger")
    return render_template("list_accounts.html", rows=rows)

"""bag27:4/29/2023 The deposit route allows users to deposit money into their
account. It first gets the arguments from the form at deposit.html.
The arguments are then used to insert data into the transactions table.
A pair of transactions will be inserted, one for the money going into the 
user's account and one for the money getting taken from the world account.
The accounts balance is then updated based on this transaction, as well
as all previous transactions in the account's history."""
@accounts.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    user_id = current_user.get_id()
    if not user_id:
        flash("No user ID", "warning")
    else:
        if request.method == "POST":
            dep = request.form.get("dep")
            a = request.form.get("account")
            memo = request.form.get("memo")
            has_error = False
            if not dep or int(dep)<=0:
                has_error = True
                flash("Cannot deposit zero or negative amount of funds", "warning")
            if not a:
                has_error = True
                flash("Must choose an account", "warning")
            if not memo:
                has_error = True
                flash("Must include a memo", "warning")
            if not has_error:
                try:
                    dep = int(dep)
                    acc_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = %s
                                """, a)
                    world_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = "000000000000"
                                """)
                    query = """
                        INSERT INTO IS601_Bank_Transactions
                        (account_src, account_dest, balance_change, transaction_type, memo, expected_total) VALUES
                        (%s, %s, %s, %s, %s, %s)
                        """
                    pairs = []
                    pairs.append(("000000000000", a, dep*-1, "deposit", memo, world_bal.row["balance"] + dep *-1))
                    pairs.append((a, "000000000000", dep, "deposit", memo , acc_bal.row["balance"] + dep))
                    DB.insertMany(query, pairs)
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = %(acc)s)
                            WHERE account_number = %(acc)s
                            """, {"acc":a})
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = "000000000000")
                            WHERE account_number = "000000000000"
                            """) 
                    flash(f"Successfully deposited ${dep} into {a}", "success")
                except Exception as e:
                    flash(f"There was an error depositing", "danger")
    return render_template("deposit.html")

"""bag27:4/29/2023 The withdraw route allows users to withdraw money from their
account. It first gets the arguments from the form at withdraw.html.
The arguments are then used to insert data into the transactions table.
A pair of transactions will be inserted, one for the money going into the 
world account and one for the money getting taken from the user's account.
The account's balance is then updated based on this transaction, as well
as all previous transactions in the account's history. A check is put 
in place to ensure no user can withdraw more than what is in the account"""
@accounts.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    user_id = current_user.get_id()
    if not user_id:
        flash("No user ID", "warning")
    else:
        if request.method == "POST":
            wd = request.form.get("wd")
            a = request.form.get("account")
            memo = request.form.get("memo")
            has_error = False
            if not wd or int(wd)<=0:
                has_error = True
                flash("Cannot withdraw zero or negative amount of funds", "warning")
            if not a:
                has_error = True
                flash("Must choose an account", "warning")
            if not memo:
                has_error = True
                flash("Must include a memo", "warning")
            if not has_error:
                try:
                    wd = int(wd)
                    acc_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = %s
                                """, a)
                    if wd > acc_bal.row["balance"]:
                        raise Exception("Cannot withdraw more than the account holds")
                    world_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = "000000000000"
                                """)
                    query = """
                        INSERT INTO IS601_Bank_Transactions
                        (account_src, account_dest, balance_change, transaction_type, memo, expected_total) VALUES
                        (%s, %s, %s, %s, %s, %s)
                        """
                    pairs = []
                    pairs.append((a, "000000000000", wd*-1, "withdrawal", memo, acc_bal.row["balance"] + wd*-1))
                    pairs.append(("000000000000", a, wd, "withdrawal", memo , world_bal.row["balance"] + wd))
                    DB.insertMany(query, pairs)
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = %(acc)s)
                            WHERE account_number = %(acc)s
                            """, {"acc":a})
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = "000000000000")
                            WHERE account_number = "000000000000"
                            """) 
                    flash(f"Successfully withdrew ${wd} from {a}", "success")
                except Exception as e:
                    flash(f"{e}", "danger")
    return render_template("withdraw.html")

@accounts.route("/internal_transfer", methods=["GET", "POST"])
@login_required
def internal_transfer():
    user_id = current_user.get_id()
    if not user_id:
        flash("No user ID", "warning")
    else:
        if request.method == "POST":
            sa = request.form.get("sa")
            da = request.form.get("da")
            dep = request.form.get("dep")
            memo = request.form.get("memo")
            has_error = False
            if not dep or int(dep)<=0:
                has_error = True
                flash("Cannot deposit zero or negative amount of funds", "warning")
            if not sa:
                has_error = True
                flash("Must choose a source account", "warning")
            if not da:
                has_error = True
                flash("Must choose a destination account", "warning")
            if not memo:
                has_error = True
                flash("Must include a memo", "warning")
            if sa == da:
                has_error = True
                flash("Cannot transfer to same account", "warning")
            if not has_error:
                try:
                    dep = int(dep)
                    sa_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = %s
                                """, sa)
                    da_bal = DB.selectOne("""SELECT balance FROM IS601_Bank_Accounts WHERE account_number = %s
                                """, da)
                    
                    if dep > sa_bal.row["balance"]:
                        raise Exception("Cannot transfer more than what is in the account")
                    query = """
                        INSERT INTO IS601_Bank_Transactions
                        (account_src, account_dest, balance_change, transaction_type, memo, expected_total) VALUES
                        (%s, %s, %s, %s, %s, %s)
                        """
                    pairs = []
                    pairs.append((sa, da, dep*-1, "int_transfer", memo, sa_bal.row["balance"] + dep *-1))
                    pairs.append((da, sa, dep, "int_transfer", memo , da_bal.row["balance"] + dep))
                    DB.insertMany(query, pairs)
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = %(acc)s)
                            WHERE account_number = %(acc)s
                            """, {"acc":sa})
                    DB.update("""UPDATE IS601_Bank_Accounts SET balance = 
                            (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_Bank_Transactions WHERE account_src = %(acc)s)
                            WHERE account_number = %(acc)s
                            """, {"acc":da})
                    flash(f"Successfully deposited ${dep} from {sa} into {da}", "success")
                except Exception as e:
                    flash(f"{e}", "danger")
    return render_template("internal_transfer.html")

@accounts.route("/external_transfer", methods=["GET", "POST"])
@login_required
def external_transfer():
    pass

"""bag27:4/18/2023 The history route takes the account number
from the account selected in the list page and lists
all entries where the account was involved in a transaction as
the source."""
@accounts.route("/history", methods=["GET"])
@login_required
def history():
    acc_num = request.args.get("account_number")
    acc = None
    rows = []
    if acc_num is None:
        flash("Account is missing", "danger")
        return redirect(url_for("accounts.list"))
    else:
        try:
            result = DB.selectOne("""SELECT account_number, account_type, balance, created 
                                FROM IS601_Bank_Accounts WHERE account_number = %s""", acc_num)
            if result.status:
                acc = result.row
            result2 = DB.selectAll("""SELECT account_src, account_dest, transaction_type, balance_change, created, expected_total, memo
                                FROM IS601_Bank_Transactions WHERE account_src = %s""", acc_num)
            if result2.status:
                rows = result2.rows
        except Exception as e:
            print(e)
            flash("There was an error pulling up history for this account", "danger")
    return render_template("transaction_history.html", acc=acc, rows=rows)
