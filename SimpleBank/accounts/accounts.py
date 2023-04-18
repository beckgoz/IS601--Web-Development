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

    query = """
        INSERT INTO IS601_Bank_Transactions
        (account_src, account_dest, balance_change, transaction_type, memo, expected_total) VALUES
        (%s, %s, %s, %s, %s, %s)
        """
    pairs = []
    pairs.append((000000000000, acc, dep*-1, reason, details))
    pairs.append((dest, src, change * -1, reason, details))
    #unique = DB.selectOne("SELECT account_number = %s FROM IS601_Bank_Accounts WHERE 1=1", str(acc))
    #if unique.status:
    if user_id:
        try:
            DB.insertOne("""
            INSERT INTO IS601_Bank_Accounts (account_number, user_id, account_type)
            VALUES (%s, %s, "checking")
            """, str(acc), user_id)
            DB.insertOne("""
            INSERT INTO IS601_Bank_Transactions (account_src, account_dest, balance_change, transaction_type, memo, expected_total)
            VALUES ("000000000000", %s, %s, "deposit", "minimum $5 deposit required", %s)
            """, str(acc), (dep*-1), (dep*-1))
            DB.insertOne("""
            INSERT INTO IS601_Bank_Transactions (account_src, account_dest, balance_change, transaction_type, memo, expected_total)
            VALUES (%s, "000000000000", %s, "deposit", "minimum $5 deposit required", %s)
            """, str(acc), dep, dep)
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
    pass

@accounts.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    pass

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
        flash(acc_num, "success")
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
            flash(e, "danger")
    return render_template("transaction_history.html", acc=acc, rows=rows)
