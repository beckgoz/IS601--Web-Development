<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 3:56:16 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231000509-a65450ec-19d2-4cd5-8a8f-df975eae51aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231000726-6e390698-11db-4979-a365-ab5852dce133.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231000844-9df540c7-383b-4103-8af0-0bdc0cbb72d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231001007-5069c860-c506-46aa-8598-72cafa7b4684.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231001147-4811b9ec-f1f2-4a23-815d-8cf44fef4cdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231001254-13b77ca4-7498-416a-8661-2da4470fa435.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords not matching<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231001385-b85da350-c174-4cd8-9815-6c32b0dbe918.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User bgoz ID 6<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/25">https://github.com/beckgoz/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The register html page calls the render_field macro from the _formhelpers.html code to<br>set up form input fields for a user to register to our site.<br>On the frontend, the html page gets the data input from the user<br>into the form fields. On the backend, the register route from auth.py gets<br>the arguments from the form and determines if they are valid or not.<br>The RegisterForm and AuthForm are responsible for determining if the input is valid.<br>Username requires an input between 2 and 30 characters and compares it to<br>the user table to see if the username is already taken. Email requires<br>an input in proper email format (requires an @ symbol). Password requires an<br>input above 8 characters, and requires it to be typed twice and be<br>an exact match in order for it to be valid. If everything is<br>valid, the data is loaded into the database via an SQL query that<br>inserts the data into the Users table. The password is hashed before it<br>is stored in the database for security.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231003126-52df0f3d-3891-411a-b543-36b6b1047b87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231003228-41e655f5-5927-4f70-b64e-47a47d589d6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231003303-febd6e06-3bdd-4ebf-ba11-e2d12725a1d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/25">https://github.com/beckgoz/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Similar to the register page, the login page creates two form inputs for<br>a user to input their username and password. The login route from auth.py<br>gets the username and password from the form, validates it using the LoginForm<br>function, and finally compares the username and password against the database using SQL<br>select queries to see if they exist, and if the password is correct.<br>The password is again hashed before the comparison so that it will match<br>the hash of the stored password. On a successful login, the user is<br>redirected to a landing page and greeted with a welcome text that displays<br>their username.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231004448-9acc7e4b-b204-4b2c-ae06-416f183deba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231004744-f8e32a4d-1fbd-4ded-acf7-bf70aadeb90b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized to access landing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/25">https://github.com/beckgoz/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>When a user is logged in, their username is put into a session<br>list, letting the website know that the user is logged in. When the<br>user clicks the logout button, the username is removed from the session list<br>and their session is ended. They must log back in if they want<br>access to their profile and the rest of the site.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231004744-f8e32a4d-1fbd-4ded-acf7-bf70aadeb90b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized to access landing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231019337-1a99d619-c633-49ea-89e6-5cfc7d85a7d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied: role protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231020552-ab543c8d-06cd-4c2c-8f35-0298153d075d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231020620-6eab36c4-62e4-4504-9173-10f369c9cacf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles table <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231020796-eb430cb5-b6fd-4e24-88c4-24074ec3b284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users table, bgoz id 6 is admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/27">https://github.com/beckgoz/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For login protected pages, the pages check if the user trying to reach<br>the page has an active session on the website already i.e. is logged<br>in. If they are logged in and have a valid session active, they<br>are allowed to reach the page. If not, they are met with an<br>error screen.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For the role protected pages such as roles/add or roles/assign, an admin role<br>is required. The inital admin role is required to be added to the<br>mysql database directly since it is impossible to add a role without admin.<br>The pages associated with role are all kept behind this admin barrier in<br>the code that requires an admin role. If a user has been added<br>to the userroles table and has the admin role, they will be allowed<br>to reach these pages, otherwise they will be met with a permissions denied<br>page.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231265888-a1735401-351d-41ef-a320-63ff9366cdde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Styling/theme shown in sample list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/22">https://github.com/beckgoz/IS601-004/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>The CSS for the site will capitalize any text in the header section,<br>including nav.html and flash.html. It also creates a header and footer for every<br>page to make the site uniform.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231000726-6e390698-11db-4979-a365-ab5852dce133.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User friendly username warning<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231000844-9df540c7-383b-4103-8af0-0bdc0cbb72d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User friendly email warning<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231001007-5069c860-c506-46aa-8598-72cafa7b4684.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User friendly email warning<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/28">https://github.com/beckgoz/IS601-004/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>When an exception is thrown in the code, flash is used to alert<br>the user that something has gone wrong. Exception handling is used in the<br>code to ensure a good user experience. When something goes wrong, they are<br>redirected to their page, a nice flash message tells them that something went<br>wrong, and they can try again. In the terminal it is smart to<br>print the technical error for the developer to see what went wrong.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231269777-e58709fa-d5ff-4770-ba71-d2c36c8399f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/28">https://github.com/beckgoz/IS601-004/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>When the user visits the profile page, the page will retrieve the current<br>user&#39;s username and email from the database via a select query by matching<br>their ID number. The user ID number is all handled back-end and the<br>user never interacts with it.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231271651-aa37ba8d-08a7-4a8f-9b7e-82154de7d12c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password/email/username validation messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231271903-3195fe18-c53e-4621-9c1a-e33a62adcd6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231272112-8f38dad8-5f53-4a28-bdff-23e40bf594bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>bgoz1 before edit (email=<a href="mailto:&#98;&#x65;&#x63;&#x6b;&#50;&#64;&#x6e;&#106;&#105;&#x74;&#x2e;&#x63;&#111;&#109;">&#98;&#x65;&#x63;&#x6b;&#50;&#64;&#x6e;&#106;&#105;&#x74;&#x2e;&#x63;&#111;&#109;</a>)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/231272309-2e65b575-8c8c-42de-bc46-e37d893464f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>bgoz1 after edit (email=<a href="mailto:&#98;&#101;&#x63;&#x6b;&#64;&#x6e;&#106;&#105;&#x74;&#46;&#99;&#111;&#x6d;">&#98;&#101;&#x63;&#x6b;&#64;&#x6e;&#106;&#105;&#x74;&#46;&#99;&#111;&#x6d;</a>)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/28">https://github.com/beckgoz/IS601-004/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The profile route gets the users username, email, current pswd, new password, and<br>confirmation password all through the profile.html form. The user can edit all of<br>these values to edit their profile. Similar to adding a user, the code<br>checks if the username/email is already in use. Also, the current password has<br>to match the users password, and the new password has be typed exactly<br>the same in both the new password and confirm fields. The code will<br>send an update query to update their profile in the database.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>There were no issues throughout this milestone, as most of it was copying/pasting<br>from the slides.&nbsp; This whole milestone was a huge help for miniproject3 as<br>it gave me a reference to look at for my business management site.<br>Learning how python code gets data from html forms was especially helpful for<br>me, as that was something I was struggling to understand in miniproject3. I<br>am sure I will be coming back to this milestone for help in<br>completing my final project.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/login">https://is601-bag27-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/bag27" target="_blank">Grading</a></td></tr></table>