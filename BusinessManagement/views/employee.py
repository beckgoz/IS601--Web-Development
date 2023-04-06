from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
import re

@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    #bag27:4/5/2023 Created a query to get all requested employee and company data, with a left join where employee company_id=company id
    query = """SELECT IS601_MP3_Employees.id, first_name, last_name, email, company_id, IS601_MP3_Companies.name
            FROM IS601_MP3_Employees 
            LEFT JOIN IS601_MP3_Companies ON IS601_MP3_Employees.company_id=IS601_MP3_Companies.id 
            WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    #bag27:4/6/2023 Got all data from request args for searching for database entries.
    #Data is pulled from list_employees.html forms
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append like filter for first_name if provided
    #bag27:4/5/2023 If data is submitted in form, it is added to the query to filter the data.
    #If fn is submitted by form, it is added to this query and it will display all entries with matching first name
    if fn:
        query += " AND first_name like %(first_name)s"
        args["first_name"]=fn
    # TODO search-4 append like filter for last_name if provided
    #bag27:4/5/2023 Same as fn
    if ln:
        query += " AND last_name like %(last_name)s"
        args["last_name"]=ln
    # TODO search-5 append like filter for email if provided
    #bag27:4/5/2023 Same as fn
    if email:
        query += " AND email like %(email)s"
        args["email"]=email
    # TODO search-6 append equality filter for company_id if provided
    #bag27:4/5/2023 Same as fn, except using an equality filter since ints are used
    if company:
        query += " AND company_id=%(company_id)s"
        args["company_id"]=company
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    #bag27:4/6/2023 If filter form is submitted by sort_filter.html, query will sort entries by selected column
    #in either ascending or descending order
    if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    #bag27:4/5/2023 Same as fn, limit determines how many entries to show
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %(limit)s"
        args["limit"] = int(limit)
    else:
        flash("Please enter a limit in the range of 1 up to 100", "warning")
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    #bag27:4/5/2023 Flashes an error is limit is out of bounds or not a number
    # TODO change this per the above requirements
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [("first_name", "First Name"), ("last_name", "Last Name"), ("email", "Email"), ("name", "Company")]
    #bag27:4/6/2023 Convert allowed cols to a dict. Needed to change company_name to name to match database column
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        #bag27:4/5/2023 Got all necessary data from request args for adding an employee.
        #Data is pulled from add_employee.html forms
        fn = request.form.get("first_name")
        ln = request.form.get("last_name")
        company = request.form.get("company")
        email = request.form.get("email")
        has_error = False # use this to control whether or not an insert occurs
        # TODO add-2 first_name is required (flash proper error message)
        #bag27:4/5/2023 Ensures a first name was entered
        if not fn:
            has_error = True
            flash("First name is required", "warning")
        # TODO add-3 last_name is required (flash proper error message)
        #bag27:4/5/2023 Ensures a last name was entered
        if not ln:
            has_error = True
            flash("Last name is required", "warning")
        # TODO add-4 company (may be None)
        #bag27:4/6/2023 If no company selected, None is inserted for company_id
        if not company:
            company = None
        # TODO add-5 email is required (flash proper error message)
        #bag27:4/5/2023 Ensures an email with proper formatting was entered
        if not email:
            has_error = True
            flash("Email is required", "warning")
        # TODO add-5a verify email is in the correct format
        #bag27:4/5/2023 Using regex to check email format
        if email:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(regex,email):
                pass
            else:
                has_error = True
                flash("Invalid email", "warning")
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email)
                VALUES (%s, %s, %s, %s)
                """, fn, ln, company, email
                ) # <-- TODO add-6 add query and add arguments
                #bag27:4/5/2023 Created query to add employee to database
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash("Error adding employee", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #bag27:4/5/2023 Gets employee id from args, flashes message if no id
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("ID is required", "warning")
    else:
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            #bag27:4/5/2023 Got all necessary data from request args for editing an employee by id
            fn = request.form.get("first_name")
            ln = request.form.get("last_name")
            company = request.form.get("company")
            email = request.form.get("email")
            has_error = False # use this to control whether or not an insert occurs
            # TODO add-2 first_name is required (flash proper error message)
            #bag27:4/5/2023 Ensures a first name was entered
            if not fn:
                has_error = True
                flash("First name is required", "warning")
            # TODO add-3 last_name is required (flash proper error message)
            #bag27:4/5/2023 Ensures a last name was entered
            if not ln:
                has_error = True
                flash("Last name is required", "warning")
            # TODO add-4 company (may be None)
            #bag27:4/6/2023 If no company selected, None is inserted for company_id
            if not company:
                company = None
            # TODO add-5 email is required (flash proper error message)
            #bag27:4/5/2023 Ensures an email with proper formatting was entered
            if not email:
                has_error = True
                flash("Email is required", "warning")
            # TODO add-5a verify email is in the correct format
            #bag27:4/5/2023 Using regex to check email format
            if email:
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if re.match(regex,email):
                    pass
                else:
                    has_error = True
                    flash("Invalid email", "warning")
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    #bag27:4/5/2023 Created query to edit employee by id
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees 
                    SET first_name = %s, last_name = %s, company_id = %s, email = %s
                    WHERE id = %s
                    """, fn, ln, company, email, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(str(e), "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            #bag27:4/5/2023 Created query to display edited employee
            result = DB.selectOne("""
            SELECT first_name, last_name, email, name
            FROM IS601_MP3_Employees 
            LEFT JOIN IS601_MP3_Companies ON IS601_MP3_Employees.company_id=IS601_MP3_Companies.id 
            WHERE IS601_MP3_Employees.id = %s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    """bag27:4/6/2023   Gets employee id from args, and deletes employee by id from employee
    table. If no ID, sent back to search table and flash warning. If id, employee is deleted
    and a flash lets the user know the entry was deleted. User is still redirected to search
    with all previous arguments passed, showing them that the entry was deleted"""
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
            if result.status:
                # TODO delete-4 ensure a flash message shows for successful delete
                flash("Deleted record", "success")
        except Exception as e:
            flash(e, "danger")
        del args["id"]
    if not id:
        # TODO delete-5 if id is missing, flash necessary message and redirect to search
        flash("ID is required", "warning")
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    return redirect(url_for("employee.search", **args))