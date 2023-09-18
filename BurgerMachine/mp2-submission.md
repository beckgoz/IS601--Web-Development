<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 8:32:51 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/225650460-8d83619f-9d2b-41ca-ad08-fa49182e004b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of calculate_cost method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/225650952-96cf4a1e-1d72-4471-9e57-ce8467eb63fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Formatting of input() message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/225651288-88eaa72b-f3d4-4054-9e43-27f49523d2b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Input/Output of burgermachine.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>To calculate the burger cost, I first iterated through the inprogress_burger list using<br>a for loop over a range of the length of the list. For<br>every item in the list, I retrieved the cost of the item and<br>multiplied it by 100 to avoid any float addition errors, and stored in<br>a temp variable. I then added the temp cost for each item to<br>the total cost of the entire burger. In the return statement, I divided<br>the cost by 100 to undo the multiplication by 100 and get the<br>cost back to it&#39;s original value. For the input() statement, I formatted the<br>value to have two decimal places using the :.2f formatter. I also included<br>a $ sign in front to make it more readable for the user.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226432202-aab12e41-006f-4c89-8c84-dbc753013b45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>OutOfStockException Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226432384-af9ac406-41db-45fc-a8df-2b4484d1aef5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226432517-93746e80-bccf-4ed0-a728-770800fc0c3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceException Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226432615-07dea76f-1ca5-42cf-a179-2fc8a98586bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesException Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226432892-1715fb7c-3329-4777-bce2-4297ff0ba531.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226433238-fcbb2092-10df-4daf-a324-ef45793b2042.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample OutOfStockException output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226434026-fbe202f7-c803-4da6-9b3b-120dd42dd858.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample NeedsCleaningException output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226434253-d7045293-5281-4385-8334-bfa7c8667522.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample InvalidChoiceException output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226434437-a0005b33-e0fe-42e7-b02c-85b3d08ecdbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample ExceededRemainingChoicesException output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226434834-79013514-fb05-4e17-bf84-d559a3072a58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample InvalidPaymentException output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>The outofstockexception is thrown when the user asks for an item that is<br>out of stock. The exception handler determines which stage the user is in,<br>and provides an error message informing the user that the item they have<br>chosen for that stage is out of stock. The user is then allowed<br>to select a different option.</div><div><div>The needscleaningexception is thrown when the machine runs out<br>of uses. It temporarily breaks the program and prompts the user to input<br>'clean' in order to clean the machine. The while loop will ask the<br>user for input until it gives the correct input and cleans the machine,<br>at which point the user can resume their order.</div></div><div><div>The invalidchoiceexception is thrown when<br>the user selects an invalid choice for the stage they are at. The<br>handler gives them a message informing them that they have chosen an invalid<br>option, and gives them a chance to select a valid option.</div></div><div><div>The exceededremainingchoicesexception is<br>thrown when the user inputs too many choices for the stage they are<br>on. It informs them that they have chosen too many options and automatically<br>moves onto the next stage.</div></div><div><div>The invalidpaymentexception is thrown when the user inputs a<br>payment that is not exactly the same as the amount displayed, excluding the<br>dollar sign. The program asks for input until the correct amount is input.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226491858-dcb53f01-88e0-421a-a4a9-0f3684cdb300.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 1 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226491937-ff21a244-99ae-4918-a543-fa7ef0aedb6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226491969-910d629a-9a55-44ca-9fc0-df21c3ea6a4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 3 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492019-6821a044-b027-421d-ae0d-e9d586c7c086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492056-09b0d034-ad94-4231-9bda-1dc682621c0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492112-9a3168c9-78d5-4b89-8a60-3944c44f1d27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492173-90c86f02-3402-4b52-9f36-60c664857c42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492224-0ade27a9-7685-4ebd-ba7d-62459bbf78ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226492361-7b6848d3-180e-477c-8e33-412cc7396558.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All tests passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1 is looking for an InvalidStageException when a topping is chosen before<br>a bun. This test tries to add a topping before the bun, and<br>passes when an InvalidStageException is thrown, ensuring that the bun must come first.</div><div><div>Test<br>2 ensures patties can only be added if in stock. When a patty<br>is&nbsp; chosen that is out of stock, and outofstockexception is thrown. This test<br>asserts true when that exception is thrown, ensuring that an error will occur<br>when a user tries to add a patty that is out of stock.<br>I set the beef patty quantity to 1 for this test to reduce<br>the amount of redundant code required to get a patty from quantity 10<br>to 0.</div></div><div><div>Test 3, similar to test 2, ensures a topping can be added<br>only if it is in stock. Using the same logic as test 2,<br>this test asserts&nbsp; true if an outofstockexception is thrown, ensuring users can only<br>select in stock toppings. I also changed the lettuce topping quantity to 1<br>for the same reason as before.</div></div><div><div>Test 4 tests that a burger can be<br>made with 3 unique patties. This case creates a burger with 3 different<br>patties, and ensures that they are all different and a part of the<br>inprogress_burger using an if statement. If the if statement passes, the test asserts<br>true and a burger can be made with three different patties. The second<br>part of test 4 ensures that a burger can only have 3 patties<br>a time. If a user adds more than 3 patties, an exceededremainingchoicesexception is<br>thrown. This test tries to add more than three patties and asserts true<br>when&nbsp; an exceededremainingchoicesexception is thrown, ensuring that the user can only add up<br>to 3 patties.</div></div><div><div>Test 5, similar to test 4, tests that a burger can<br>be made with 3 unique toppings. This case creates a burger with 3<br>different toppings, and ensures that&nbsp; they are all different and a part of<br>the inprogress_burger using an if statement. If the if statement passes, the test<br>asserts true and a burger can be made with 3 different toppings. The<br>second part of test 5 ensures that a burger can only have 3<br>toppings a time. If a user adds more than 3 toppings, an exceededremainingchoicesexception<br>is thrown. This test tries to add more than three toppings and asserts<br>true when an exceededremainingchoicesexception is thrown, ensuring that the user can only add<br>up to 3 toppings.</div></div><div><div>Test 6 ensures that the machine properly calculates the correct<br>cost for each burger based on the given costs. I added up the<br>cost for 3 different burgers, and using the handle_pay method, I made sure<br>the machine calculated the same correct cost. When the input payment (my calculated<br>cost in correect format) is different from&nbsp; the machine calculated cost, an invalidpaymentexception<br>is thrown. This test asserts False if such exception is thrown, ensuring the<br>accuracy of the machine's cost calculation.</div></div><div><div>Test 7 tests the machines ability to keep<br>track of the machine's total sales. To test this, I created 3 different<br>burgers and added up their cost. I then compared it to the machine's<br>total_sales variable. If they are the same, the test asserts true and the&nbsp;<br>machine correctly keeps track of total sales.</div></div><div><div>Test 8 tests the machines ability to<br>keep track of the machine's total burger creations. To test this, I created<br>3 different burgers and compared 3 to the machines total_burger variable. If the<br>variable does not equal 3, the&nbsp; machine is not capable of keeping track<br>of the total number&nbsp; of burgers created and the test asserts false.</div></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/18">https://github.com/beckgoz/IS601-004/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>An issue I encountered during this assignment came when I began to work<br>on the test cases. When using the fixtures, I couldn&#39;t figure out how<br>to reset all of the burgermachine variables in between every test. I had<br>built up orders to test the outofstockexception, and it worked for testing the<br>patties for being out of stock, but then for the next test (topping<br>out of stock) it would get an error in the fixture because the<br>patties would be out of stock and the fixture orders would give me<br>an error. I ended up only using one fixture to use the same<br>burger machine for every test case, and manually editing the quantity of some<br>ingredients to avoid redundant and confusing code.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226493567-f4a929d5-831d-44d5-8ba6-9da39cd1d3a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample working output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/226493677-7ce18265-a781-4fcf-ab7b-d34c70e59511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample working output with some error handling<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/bag27" target="_blank">Grading</a></td></tr></table>