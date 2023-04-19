from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.datastructures import MultiDict
import random

from sql.db import DB
accounts = Blueprint('accounts', __name__, url_prefix='/accounts', template_folder='templates')

@accounts.route("/create", methods=["GET", "POST"])
@login_required
def create():
    user_id = current_user.get_id()
    acc = "%0.12d" % random.randrange(10**12)
    dep = 5
    #unique = DB.selectOne("SELECT account_number = %s FROM IS601_Bank_Accounts WHERE 1=1", str(acc))
    #if unique.status:
    if user_id:
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
        except Exception as e:
            print(e)
            flash(f"{e}", "danger")
    #else:
        #flash("Error creating account, please try again.", "danger")
    flash("Account successfully created!", "success")
    return redirect(url_for("accounts.list"))

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
                    pairs.append((a, "000000000000", wd*-1, "withdrawal", memo, world_bal.row["balance"] + wd))
                    pairs.append(("000000000000", a, wd, "withdrawal", memo , acc_bal.row["balance"] + wd*-1))
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

@accounts.route("/transfer", methods=["GET", "POST"])
@login_required
def transfer():
    pass

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
            result2 = DB.selectAll("""SELECT account_src, account_dest, balance_change, created, expected_total, memo
                                FROM IS601_Bank_Transactions WHERE account_src = %s OR account_dest = %s""", acc_num, acc_num)
            if result2.status:
                rows = result2.rows
        except Exception as e:
            print(e)
            flash("There was an error pulling up history for this account", "danger")
    return render_template("transaction_history.html", acc=acc, rows=rows)
