<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 4/25/2023 11:24:39 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234306182-5ddd9a70-8468-4562-974d-5abfbb335633.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Internal Transfer Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234306956-4c6bd2a2-9729-4e4f-929c-11c3320f7445.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dropdown account values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234307129-36f85ab1-7eb0-4ae5-b10d-6bd465d56551.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cant transfer more than account balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234307315-994b041d-ff9e-4742-90bc-0d70118b9a71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cant transfer to same account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234307799-827ca5ee-49ec-4cdb-8132-5b666a3e28fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing how source acc = dest acc is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234308031-01e7ac6c-a63a-4639-8f48-49171ae2f08c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cant transfer negative balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234308382-021cb816-4ad0-4eda-91a9-5f8dd80fba4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing how negative/zero amount is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234308776-af537384-31ed-41c5-aae7-a7175d552440.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction ids 127 and 128 show internal transfer between two accounts<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234309034-4ef01d0d-0ba0-4fdd-b987-470e2e29f14a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Account ids 32 and 33 show both accounts and affected balances<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p>The initial balances are fetched through SQL queries that return the source and<br>dest account balances by referencing the account number.<div>The expected total is calculate by<br>getting the account balances and adding/subtracting the transfer amount depending on which account<br>is sending/receiving. The transaction pairs are inserted into the transaction table, with one<br>transaction having a negative balance change and the other having a positive balance<br>change. The source account has the negative balance change as they are sending<br>money.</div><div>The balances of the accounts are updated by the summation of all of<br>the balance_change values in the transaction table where the account is the source<br>account. It is important that only the source account is accounted for in<br>this calculation, as including transactions where the account is the dest account would<br>result in a balance of zero.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/40">https://github.com/beckgoz/IS601-004/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/internal_transfer">https://is601-bag27-prod.herokuapp.com/accounts/internal_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234323036-57e66615-df34-42bc-bf4e-ba1e4bf65a11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction IDs 135-152 show transaction pairs for activity involving account 444629199251<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234323445-93beca34-8db5-42f4-a727-0a2365d23855.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction History page of account 444629199251<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234323692-fe21e220-e844-4150-bf71-219b567b9a10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Filtered by deposit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234323830-9a7e332a-fe08-4614-9adb-5191299f392b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page 2 of all transactions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234324045-70123b75-b0d2-412c-ae99-f3eaffd42634.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtered by all transfers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234324235-e5e2f15c-1d3b-45c3-991c-d4f3bd299bee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtered by from date to date where no transactions occured<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>The filters are given by the user in the html form, which are<br>then added to the SQL query, filtering which results are pulled form the<br>database. Using flask-pagination, the results of the query are passed as a list<br>to a pagination object. The pagination object separates the list into lists of<br>10 items. Each list of 10 items is given their own page on<br>the html page. Depending on how many results are given by the SQL<br>query, the pagination object creates page links to navigate through the results. For<br>example, if 36 items are retrieved, there will be 4 pages. The first<br>three will have 10 items each, and the last one will have 6.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/42">https://github.com/beckgoz/IS601-004/pull/42</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/history?account_number=444629199251">https://is601-bag27-prod.herokuapp.com/accounts/history?account_number=444629199251</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234316581-18a828bf-c207-4656-9ba6-fa555353938b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile page with first name and last name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/40">https://github.com/beckgoz/IS601-004/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/profile">https://is601-bag27-prod.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234311758-1d880f3c-054f-445d-b47f-d96b9ec26d16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>External transfer page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234312190-74ef327c-7eba-4304-932b-5ac8f678a087.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cant transfer more than the account balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234312771-f1bceeab-9f74-4603-986e-d87dd8ac6604.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to prevent transfer of more funds than allowed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234313002-26acab44-04ae-49b6-9428-1866a364f7e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to prevent negative/zero transfer<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234313206-5336d1c6-0b68-4664-8269-764446d780e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot transfer zero or negative funds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234313406-8f767159-da83-4fd7-8ac6-137f22549213.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Could not find account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234314015-f4ee438a-8044-4751-b1c5-2cbb37e8eec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing how account is found and what happens if no account found<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234314535-94793cf8-d83d-4fed-bdcf-e1e1b0166e0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction IDs 133 and 134 show external transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/234314712-853d0ce7-c458-4f31-bd31-a14bbce2c524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Account IDs 33 and 34 with different user IDs show the updated balances<br>after transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>The user inputs the destinations last 4 account digits. Using LIKE CONCAT(&#39;%&#39;, %s),<br>the SQL query will look for account numbers whose last 4 digits match<br>the digits input by the user.<div>The last name is found using the LIKE<br>comparator so that the user does not have to worry about case-sensitivity. The<br>query left joins the account and user table on user_id to be able<br>to attribute accounts to specific users.</div><div>Multiple results are not handled.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/41">https://github.com/beckgoz/IS601-004/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bag27-prod.herokuapp.com/accounts/external_transfer">https://is601-bag27-prod.herokuapp.com/accounts/external_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I did not have many issues while completing this milestone 3. The internal<br>and external transfer features re used a lot of the same logic and<br>processing as the deposit and withdrawal features, so with a little bit of<br>form and sql tweaking, I was able to get them working pretty quickly.<br>Adding the first name and last name to the user&#39;s profile was also<br>relatively easy, the hardest being having to change the wtforms for the user.<br>The part I had the most trouble with was the pagination of the<br>transaction history table. After a decent amount of research, I found a youtube<br>video (<a href="https://www.youtube.com/watch?v=vt0OXl2WCGI">https://www.youtube.com/watch?v=vt0OXl2WCGI</a>) and a gist (<a href="https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9">https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9</a>) that showed an example of how to<br>use flask-paginate. I used these two as references and it was simple to<br>implement from there.<div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/bag27" target="_blank">Grading</a></td></tr></table>