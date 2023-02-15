<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 2/15/2023 6:42:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219156162-57313ee1-188c-46d4-8521-3f302de43e9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the add_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219157547-f155c755-8f4c-4bd4-9375-2c92a5f323f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the success/failure of adding tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>Using datetime.now(), the lastActivity value is updated to the current time. The function<br>takes all of the user-input arguments and updates the associated key-value pairs in<br>the task with the input (name, description, due date). The due date is<br>string is passed through the str_to_datetime function so that it is correctly represented<br>as a datetime object in the dict. The task is then appended to<br>the tasks list. Finally, a message is printed letting the user know whether<br>the task has been successfully added or not, depending on missing arguments<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219158878-42255b46-bc32-444a-992a-fab5ad2e6cf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of process_update function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>Function first checks if index is out of bounds. One of two error<br>messages are shown, depending on whether the index is beyond or before acceptable<br>index range. A temporary task variable is used to represent the task at<br>the given index. Next it extracts the name, description, and due date of<br>selected task using key value pairs. The values are displayed next to prompts.<br>Function then call update_task function to update the task</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219160433-97716c90-a7f6-4e6c-be68-80360925157d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of update_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219161068-daba7821-1f32-41ab-bd76-3c9d001df710.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success/failure of update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>The index is handled by the process_update function. The function updates the task<br>values only if the user has input data. If no data supplied, the<br>original data is kept. Regardless of any changes, the lastActivity value is always<br>updated. Finally, a print statement tells the user which values have been updated.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219207736-b2e80fdc-ac92-4663-979a-4d661a7c6535.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of mark_done function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219208386-2d98c6d6-f150-40e8-84f9-4b60f13abce7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success/failure of mark_done function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>First check if index is in bounds. Next, the done value of the<br>task is evaluated. If it is not completed, it is marked as done,<br>and the done value is filled in with the current datetime. If it<br>is already completed, a message saying so is shown.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219208588-28355bb7-14ee-4444-a0cf-7ae5c15f5cce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of view_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219208789-0711c49a-cfc8-413b-a910-9c4062bb8768.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure/success of view_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219209194-8cb88aaa-e212-45be-86e7-24649b3f620e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of list_tasks function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219209825-819627bc-8c1f-4e0a-ac08-2b14b2097b63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of delete_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219210165-d905306f-f6e9-422a-8af0-ab5cd79c9483.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success/failure of delete_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>First made sure index was in bounds. Then the function deleted&nbsp; the task<br>from the tasks list at given index using the del command. A message<br>is shown confirming whether the task was deleted or not.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219210887-aa3d7d22-1f66-4b43-bf61-213d8a1e2390.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of get_incomplete_tasks function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219212562-f139990a-c516-4cd6-9c0c-030a606b78a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure of incomplete (no incomplete tasks)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219213601-5fac4f98-0e5f-4452-ab28-506bf10b4a60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success of get_incomplete_tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>Traverses the tasks list using a for loop. For every task, determines if<br>done = false. if done = false, task is added to _tasks list<br>which represents the incomplete tasks. Finally, the _tasks list is passed to the<br>list_tasks function which displays all of the incomplete tasks. If no incomplete tasks,<br>a message is shown saying no tasks to show.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219213944-edd2bc8c-d66f-4bb9-b55a-c6ca4705e5e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of get_overdue_tasks function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219214368-0923b1b5-b72d-444c-a1f3-4b091f7809e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure of get_overdue_tasks (no overdue tasks)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219214833-7f3de600-9251-4321-8eaf-b14859b21cda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success of get_overdue_tasks <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>Similar to get_incomplete_tasks, this function traverses the list to find all the tasks<br>that are not done and have a due date that is less than<br>the current date. str_to_datetime converts the 'due' value for each task to a<br>datetime, so that it can be easily compared to the current date using<br>comparison operators. If a task has not been marked completed and a due<br>date that is less than the current time, it is added to the<br>_tasks list which is passed to the list_tasks function which displays the tasks.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219215401-237349c2-c379-4e7a-be2a-6dd321ddcbb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of get_time_remaining function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219215533-dc08351c-2365-4eae-b5eb-0ee84381221c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure/success of get_time_remaining function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div>First makes sure index is in bounds. Next the function compares current time<br>to the due date. If the due date &gt; current time, the function<br>gets the days and seconds to the due date simply using the subtraction<br>operator. The data is then formatted using an algorithm to get the hours,<br>minutes, and seconds in a readable format. If the due date &lt; current<br>time, the task is overdue. The time past since the due date gathered<br>by subtracting the due date from the current time, and is formatted the<br>same. I found the data formatting algorithm on stack overflow (https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes).</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219217006-a18a53a1-9816-4acb-a1ca-6c42f9adb455.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing add, done, and list functions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219217537-4744c2c8-da03-4dd8-9cbc-2e3e0876c97d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing remaining, list, and update functions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219217932-3af6ffab-fd00-4aa6-916e-10b0f7e38794.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing overdue function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/219218371-5c380d24-eba2-4fad-8afd-2630309ccef0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SavedJSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I didn&#39;t really run into any issues while completing this project. I was<br>able to implement every function after I took the time to understand what<br>it was trying to do and how it was trying to do it.<br>One of the biggest takeaways from this project for was learning how to<br>access values from a dict, which I would previously have to google the<br>steps to every time. After this project, I don&#39;t think I will have<br>to google that ever again.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/9">https://github.com/beckgoz/IS601-004/pull/9</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/bag27" target="_blank">Grading</a></td></tr></table>