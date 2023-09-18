<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Bank Project</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 2:30:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Create Accounts table and setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot from the db of the system user (Users table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233155613-35c2a7a9-d272-4e8d-adc3-e09615a1bb2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>System user is -1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot from the db of the world account (Accounts table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233155798-5c18986b-3995-40ee-9c8c-2c2cd525caf3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>World account 000000000000<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain the purpose and usage of these two entries and how they relate</td></tr>
<tr><td> <em>Response:</em> <p>The system user is a user that&#39;s sole purpose is for the functionality<br>of the world account so that it has a user_id to associate to.<br>The world account is used to keep track of the transactions that involve<br>the flow of money in and out of the bank. If the system<br>is correct, the world account balance should be equal to the negative of<br>the sum of all of the account balances in the system.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/36">https://github.com/beckgoz/IS601-004/pull/36</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Dashboard </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the requested links/navigation</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233156451-dec1922d-68b4-49e3-b340-6b01629897a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dashboard page screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain which ones are working for this milestone</td></tr>
<tr><td> <em>Response:</em> <p>All of the links on the navbar are working. Create account creates a<br>checking account for the user and associates it to their user_id, and automatically<br>redirects them to a list of all their accounts. The My accounts link<br>takes the user to same page that lists all of their accounts. The<br>actions link gives a dropdown that allows the user to choose if they<br>want to deposit, withdraw, or transfer money from their accounts. The deposit and<br>withdraw links are working, but the transfer link has not yet been implemented.<br>The roles, profile, and logout links are all the same links from the<br>previous milestone.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/36">https://github.com/beckgoz/IS601-004/pull/36</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Create a checking Account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the Create Account Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233157725-03ff20d5-477e-4c4b-847c-aed88e69d688.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully created account<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots showing validation errors and success message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233157725-03ff20d5-477e-4c4b-847c-aed88e69d688.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Account creation success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the transaction generated from the initial deposit (from the DB)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233158186-53f7ea2f-7b82-4615-9055-5b9ea15c4bbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transactions 45 and 46 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain which account number generation you used and the account creation process including the transaction logic</td></tr>
<tr><td> <em>Response:</em> <p>I chose option 1 from the proposal which entails generating a random 12<br>digit number for the account. A user can only create an account if<br>they are logged in. When an account is created, a random 12 digit<br>string is created and that is given as the account number, if the<br>number is already in use, the user is prompted to try again. The<br>system gets the users id and associates the account to the id. An<br>initial deposit of $5 is required, and a transaction occurs between the newly<br>created account and the world account. I chose not have a dedicated page<br>for the create account since there is no input required from the user.<br>They simply click create account and they are redirected to the list account<br>page with their new account shown.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/36">https://github.com/beckgoz/IS601-004/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/">https://is601-bag27-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to list their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's account list view (show 5 accounts)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233159222-80a86e15-1d4b-4624-bc79-7890fa62b271.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>List account page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the page is displayed and the data lookup occurs</td></tr>
<tr><td> <em>Response:</em> <p>The page is a simple table that retrieves headers and data from the<br>sql query that retrieves the accounts and the account data that are associated<br>to the current logged in user based on their user id.&nbsp;<div><br></div><div>Unrelated: i believe<br>the pull request form below this is messed up. I had to input<br>an incorrect link.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/d36">https://github.com/beckgoz/IS601-004/pull/d36</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/list">https://is601-bag27-prod.herokuapp.com/accounts/list</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Account Transaction Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of an account's transaction history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233163397-bedb5210-ff79-4f5e-a66e-c4fd7a251ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction History page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the lookup and display occurs</td></tr>
<tr><td> <em>Response:</em> <p>From the account list page, the user selects which account they want to<br>see the history for. Using that account number, the account details are pulled<br>from the accounts database. Also using the account number, all the transactions where<br>the account is the source are pulled from the transactions table. Only pulling<br>the source account transactions eliminates showing the transactions pairs while still showing the<br>activity of the account.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/37">https://github.com/beckgoz/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/history?account_number=396592875955">https://is601-bag27-prod.herokuapp.com/accounts/history?account_number=396592875955</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Deposit/Withdraw </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a Screenshot of the Deposit Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233163397-bedb5210-ff79-4f5e-a66e-c4fd7a251ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deposit page with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a Screenshot of the Withdraw Page (this potentially can be the same page with different views)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233164725-fbe2cb7d-fadd-427e-b7a4-1a1a56a9518d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Withdraw with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show validation error for negative numbers</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233164583-a1f4f76a-9343-4932-acb4-19f02b0492ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Negative number deposit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Show validation error for withdrawing more than the account contains</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233164960-8785f5fb-329a-42db-9af2-7363affb50e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot withdraw more than account holds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Show a success message for deposit and withdraw (2 screenshots)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233164360-105d69c7-5f1a-41c5-bdea-cd6638b32cb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deposit success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233164803-8954b00c-a172-46c1-ba60-7a11a981f57f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Withdraw success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Show a screenshot of the transaction pairs in the DB for the above tests</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/233165187-7ffb47a5-c4dc-48c8-a1a1-5671c2ce661b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ID 65 and 66 show deposit pair. ID 67 and 68 show withdraw<br>pair<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain how transactions work</td></tr>
<tr><td> <em>Response:</em> <p>The user fills in the form with account number, deposit amount, and memo,<br>which are stored as variables. The balance of the account number and also<br>the world account are pulled from the database and stored as variables. A<br>pair of transactions are then added to the transaction database. The account that<br>is receiving the money has a positive balance change and the expected total<br>is equal to the account&#39;s balance plus the balance change. The account that<br>is giving money has a negative balance change and the expected total is<br>equal to the account&#39;s balance minus the balance change. The accounts are then<br>both updated to set their balance equal to the sum of their balance<br>changes in the transaction table in which the account is the source.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/37">https://github.com/beckgoz/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/withdraw">https://is601-bag27-prod.herokuapp.com/accounts/withdraw</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I did not happen to run into many problems while completing this milestone,<br>which is shocking to me. I used a lot of the previous project<br>files as references which helped me out a ton. One thing that took<br>me a while to wrap my head around was how I was going<br>to make sure that two account numbers don&#39;t collide when they are randomly<br>generated. I then realized I could try a database query where I select<br>account numbers where the account number was the same as the generated one.<br>If any results came back, there was a collision and the user would<br>have to try again. With a 12 digit account number, it is very<br>unlikely that a collision would occur.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/login">https://is601-bag27-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/bag27" target="_blank">Grading</a></td></tr></table>