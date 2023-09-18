from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')
import pycountry

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    #bag27:4/6/2023 Created a query to get all requested employee and company data, with a left join where employee company_id=company id
    #Used Count and Group By to get employee count
    query = """SELECT IS601_MP3_Companies.id, name, address, city, country, state, zip, website, 
    COUNT(IS601_MP3_Employees.id) AS employeeCount 
    FROM IS601_MP3_Companies 
    LEFT JOIN IS601_MP3_Employees ON IS601_MP3_Employees.company_id=IS601_MP3_Companies.id 
    WHERE 1=1
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    #bag27:4/6/2023 Got all data from request args for searching for database entries.
    #Data is pulled from list_companies.html forms
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append a LIKE filter for name if provided
    #bag27:4/6/2023 If data is submitted in form, it is added to the query to filter the data.
    #If name is submitted by form, it is added to this query and it will display all entries with matching company name
    if name:
        query += " AND name like %(name)s"
        args["name"]=name
    # TODO search-4 append an equality filter for country if provided
    #bag27:4/6/2023 Same as name
    if country:
        query += " AND country=%(country)s"
        args["country"]=country
    # TODO search-5 append an equality filter for state if provided
    #bag27:4/6/2023 Same as name
    if state:
        query += " AND state=%(state)s"
        args["state"]=state
    query+=" GROUP BY IS601_MP3_Companies.id"
    if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    #bag27:4/6/2023 Same as name, limit determines how many entries to show
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %(limit)s"
        args["limit"] = int(limit)
    else:
        flash("Please enter a limit in the range of 1 up to 100", "warning")
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    #bag27:4/6/2023 Flashes an error is limit is out of bounds or not a number
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [("name", "Name"), ("city", "City"), ("country", "Country"), ("state", "State")]
    #bag27:4/6/2023 Convert allowed cols to a dict
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        #bag27:4/6/2023 Got all necessary data from request args for adding an employee.
        #Data is pulled from add_company.html forms
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zip")
        website = request.form.get("website")
        has_error = False # use this to control whether or not an insert occurs
        # TODO add-2 name is required (flash proper error message)
        #bag27:4/6/2023 Ensures a company name was entered
        if not name:
            has_error = True
            flash("Name is required", "warning")
        # TODO add-3 address is required (flash proper error message)
        #bag27:4/6/2023 Ensures an address was entered
        if not address:
            has_error = True
            flash("Address is required", "warning")
        # TODO add-4 city is required (flash proper error message)
        #bag27:4/6/2023 Ensures a city was entered
        if not city:
            has_error = True
            flash("City is required", "warning")
        # TODO add-5 state is required (flash proper error message)
        #bag27:4/6/2023 Ensures a state was entered
        if not state:
            has_error = True
            flash("State is required", "warning")
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        #bag27:4/6/2023 Ensures a country name was entered
        if not country:
            has_error = True
            flash("Country is required", "warning")
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        #bag27:4/6/2023 Supposed to ensure country/state are valid
        """if country not in pycountry.countries:
            has_error = True
            flash("Not a valid country", "warning")
        if state not in pycountry.subdivisions.get():
                has_error = True
                flash("Not a valid state", "warning")"""
        # TODO add-7 website is not required
        #bag27:4/6/2023 Sets website to None if none entered
        if not website:
            website = None
        # TODO add-8 zipcode is required (flash proper error message)\
        #bag27:4/6/2023 Ensures a zipcode name was entered
        if not zipcode:
            has_error = True
            flash("Zip is required", "warning")
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, state, country, zipcode, website
                ) # <-- TODO add-8 add query and add arguments
                #bag27:4/6/2023 Created query to add company to database
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Error adding company", "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #bag27:4/6/2023 Gets company id from args, flashes message if no id
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("ID is required", "warning")
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            #bag27:4/6/2023 Got all necessary data from request args for editing an company by id
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip")
            website = request.form.get("website")
            has_error = False # use this to control whether or not an insert occurs
            # TODO add-2 name is required (flash proper error message)
            #bag27:4/6/2023 Ensures a company name was entered
            if not name:
                has_error = True
                flash("Name is required", "warning")
            # TODO add-3 address is required (flash proper error message)
            #bag27:4/6/2023 Ensures an address was entered
            if not address:
                has_error = True
                flash("Address is required", "warning")
            # TODO add-4 city is required (flash proper error message)
            #bag27:4/6/2023 Ensures a city was entered
            if not city:
                has_error = True
                flash("City is required", "warning")
            # TODO add-5 state is required (flash proper error message)
            #bag27:4/6/2023 Ensures a state was entered
            if not state:
                has_error = True
                flash("State is required", "warning")
            # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO add-6 country is required (flash proper error message)
            #bag27:4/6/2023 Ensures a country name was entered
            if not country:
                has_error = True
                flash("Country is required", "warning")
            # TODO add-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            #bag27:4/6/2023 Supposed to ensure country/state are valid
            """if country not in pycountry.countries:
                has_error = True
                flash("Not a valid country", "warning")
            if state not in pycountry.subdivisions.get():
                    has_error = True
                    flash("Not a valid state", "warning")"""
            # TODO add-7 website is not required
            #bag27:4/6/2023 Sets website to None if none entered
            if not website:
                website = None
            # TODO add-8 zipcode is required (flash proper error message)\
            #bag27:4/6/2023 Ensures a zipcode name was entered
            if not zipcode:
                has_error = True
                flash("Zip is required", "warning")
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            
            # populate data dict with mappings
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    #bag27:4/6/2023 Created query to edit company by id
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies 
                    SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s
                    WHERE id = %s
                    """, name, address, city, state, country, zipcode, website, id )
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            #bag27:4/6/2023 Created query to display edited company
            result = DB.selectOne("""
            SELECT name, address, city, state, country, zip, website
            FROM IS601_MP3_Companies
            WHERE id = %s""", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    """bag27:4/6/2023   Gets company id from args, and deletes companuy by id from company
    table. Before this, all employees are deallocated from the company and their company_id
    is set to null. If no ID, sent back to search table and flash warning. If id, company is deleted
    and a flash lets the user know the entry was deleted. User is still redirected to search
    with all previous arguments passed, showing them that the entry was deleted"""
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
                # TODO delete-5 for all employees assigned to this company set their company_id to None/null
                result2 = DB.update("""
                UPDATE IS601_MP3_Employees
                SET company_id = null
                WHERE company_id = %s
                """, id)
                if result2.status:
                    flash("Updated employees", "success")
                # TODO delete-1 delete company by id (unallocate any employees see delete-5)
                result1 = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)
                if result1.status:
                    # TODO delete-4 ensure a flash message shows for successful delete
                    flash("Deleted record", "success")
        except Exception as e:
            flash(str(e), "danger")
        del args["id"]
    if not id:
        # TODO delete-5 if id is missing, flash necessary message and redirect to search
        flash("ID is required", "warning")
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    return redirect(url_for("company.search", **args))
    