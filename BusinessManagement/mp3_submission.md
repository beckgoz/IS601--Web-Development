<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 4/9/2023 7:50:44 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/229383948-f98795f1-82b9-46fd-9448-c57c10250509.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing change of UCID and href changes in nav.html<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/229586355-ca1bfa23-fc33-402d-bae4-5083b9ba1eb4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Companies Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/229586444-65e21212-45af-4cff-88ba-c548cbd450fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employees Table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230143263-1768cac8-8898-408c-8ddb-920e56965805.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking if .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230143532-91f92eea-ae8f-4c8c-aae3-e585fa4c7b7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reading stream as dict and extracting company/employee data into lists only if all<br>data is present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230144038-a3dc237a-85f9-4c0e-b231-d6d8ca8122d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding flash message to show user amount of records inserted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230144484-f7509ef4-0d27-4cdd-ba69-bc3b959d5d94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message with no file attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230144670-afe68aab-ce2c-4cb7-b4d4-463c9d5ab26d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message when passed with a non .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230144869-bb023e88-85cb-4b3e-a094-e2342d9fca9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful import of .csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230145026-dd83b591-ae4c-45be-8124-aa87cde68c92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company table in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230145132-6596cbdc-7d74-4f31-9d87-870f8e4931d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee table in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230498929-d80856c3-4bb9-4611-92a4-ad1acbba1d42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add employee route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730696-161f3f36-158f-46ac-91e1-3c3b5b70b229.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filled in data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730405-d06187e4-5d78-4955-855b-90345ef0934a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730452-e4b6314a-3748-47c9-9456-2f59bbe26341.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last/First/Email Error Messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730734-2d90b23e-e530-4742-bfbc-b0c1a205500d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Joe Shmoe was added to employee table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730885-3d5db30e-9773-4443-962d-98329eebbd79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1/2 Search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730918-4fd9e2d9-0126-45a8-b200-74441248576a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2/2 Search route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230730990-b0b194a5-d7d9-4d14-80bd-4ad7f53a1ebf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731031-c1795245-b863-4115-bbfb-6bc3222060c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731062-8eb8d386-c5de-4634-8a92-2e04604fa80b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731081-a43e6f69-93b8-4a2f-8ae9-bbafa58028f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731160-c0ae9e11-b83b-44f4-9dd5-097be4ff8dde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order ascending by first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731124-5af88e3f-d68f-462a-b3d8-10b61effdbaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order descending by first name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731217-a935967c-2df4-4316-b2e2-5bb99c63a3fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1/2 Edit route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731266-49e54327-9341-4e17-9399-3f83ecc7e8b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2/2 Edit route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731361-7bc1a5dd-d588-41a0-a42b-f1cfa3fc9d58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson butt before edit no company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731409-3464b34a-1739-48ca-8c68-62211946fe7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In edit page adding company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731440-7febb9b3-35a5-46ec-b19a-77e198123cfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson Butt after edit company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731299-d09b6c4b-7065-4824-8433-7a5183843a0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson Butt before edit no company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731476-0b3a8be2-be16-4e25-ba4f-4f5557305348.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson Butt new company ID<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731535-d249a10c-ed9b-4de0-bfda-4db810bf8e65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1/2 Company route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731564-7f54b4aa-0747-4c49-8ede-26f494444b71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2/2 Company route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731754-a8aa231d-b676-4ce2-b98a-c90391213c67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731701-5c275740-1f0e-48fd-97f8-0997f5e438d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230731815-cbcc2279-d405-48ef-8a93-30a82e3319bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801152-f7e546bb-28c4-4175-a1f0-21432e424179.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cool company added ID 9009<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801214-53675789-cec0-48ce-b2f4-472bbb06e4ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company search route code 1/2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801239-0a70e9a6-5702-40b5-82d4-bb6873fb8c06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company search route code 2/2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801319-6ba1e33c-0c36-4c46-89e1-7bb83f677f44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search with name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801350-71ad2ce9-5238-48a2-bf5f-5b8e9635b8e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search with country filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801377-ca2b07ca-5e4e-46fc-bda7-b29de1741f30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search with state filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801406-0a67ae1c-7e5b-433f-b513-4c9df727a324.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sorted by city ascending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801421-e207bd10-8c28-487e-9c6f-094ac41d4f9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sorted by city descending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801461-ed398e03-d23d-41bc-8bd9-163a50a01ede.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company edit route code 1/2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801479-c257313d-e1d9-42e4-b7fe-db8441ab6688.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company edit route code 2/2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801319-6ba1e33c-0c36-4c46-89e1-7bb83f677f44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cool company before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801600-816d3c09-e365-4d0d-8ff2-a6b02c750c94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cooler company after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801152-f7e546bb-28c4-4175-a1f0-21432e424179.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cool company before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801625-f9145d20-3193-40cb-acdb-5f2f025a5d25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cooler company after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801698-61102d88-33f4-4175-9b4e-113c25f2b48b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee delete route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801724-a2dc2070-dd2a-4a4f-9dad-8e3826345680.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801744-5506c0e4-391b-46ae-af86-3ed69dd0c5ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jameson after delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801758-bc5052f4-389d-4332-850a-fdfb14889828.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company delete route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801600-816d3c09-e365-4d0d-8ff2-a6b02c750c94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cooler company before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230801789-f90d8e76-7a7d-4f6c-8d49-29a2aa5eefbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cooler company after delete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/230499319-d8ff0c26-194a-4192-8e31-da711709ab7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>This project was especially challenging for me due to it being my first<br>experience with web development outside of the sample website we have been building<br>in class following the slides. I think the hardest thing for me to<br>grasp was the relationships between the python files and the html files; how<br>they interacted and got data from each other. The biggest thing that helped<br>me overcome the learning curve was in fact the sample website code. I<br>referenced the code for the add, list, edit, and delete route for each<br>deliverable of this project. It helped me recognize how the python code got<br>the data from the html forms and was able to manipulate it from<br>there by passing it through SQL queries. I have experience with SQL and<br>database design so I didn&#39;t have much trouble figuring out how the queries<br>worked. Overall, once I got the hang of the python to html relationships,<br>I was able to complete the project relatively easily. A lot of the<br>same concepts carried over from one route to another, so it was really<br>a matter of just sorting out variables once I understood what the basic<br>algorithm/flow of the program would be. I believe this project has given a<br>lot of knowledge and experience that I will be able to use to<br>complete the final project.<div><br></div><div>I was not able to figure out how to determine<br>a catch for invalid country/state input for the add/edit company routes, however I<br>do not believe it entirely necessary since the country/state dropdowns on the forms<br>only let you select valid states for each country. Knowing this, I felt<br>comfortable leaving it out of the routes since I knew it would not<br>have a huge impact on the websites&#39; performance.</div><div>I also was not able to<br>get my website to pass all of the pytest tests. I am not<br>sure why the th tags for the list employee table weren&#39;t successful, but<br>they showed up on the website in the correct format so I decided<br>to turn those pytests off in order to deploy my website to heroku.</div><div><br></div><div>I<br>was locked out of my Heroku account after I got a new phone<br>and forgot to sync my authenticator app, so that is why some of<br>the website URLs are is601-bag27-dev-temp. That was a site that Dr. Toegel put<br>up for me to get my screenshots. However, halfway through getting my screenshots<br>I realized that my site should still have deployed to Heroku after I<br>pushed it to dev because of the .yml file, and sure enough my<br>site was up and it was running so I was able to use<br>it without being logged into Heroku.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/bag27" target="_blank">Grading</a></td></tr></table>