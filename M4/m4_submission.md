<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Beck Gozdenovich (bag27)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 2:35:47 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/bag27" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220182987-78197371-1e75-46be-8930-bacc309f8a12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>MyCalc Add function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183068-79c34281-91e8-41fd-8d86-20720049fcad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>MyCalc sub function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183129-229585d4-81e6-4c7e-b45c-8532531ecba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>MyCalc mult function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183186-72fa77b1-8a7f-49e2-ba74-11378c7b67ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>MyCalc div function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183787-6113a5a0-4d38-4040-a17c-4d2b4ac7dc47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot number-add-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220184879-d8f90cf5-f2a2-47ca-8a92-d9f8e4c7a9f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of ans-add-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220184275-3e586ecd-498f-4600-a707-63abef9a5578.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of number-sub-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220184999-02e7c9e4-ef22-474a-aa81-bab083b63492.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-sub-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220184431-f0c3ec42-8a70-4edc-ab3a-0e984d2dcb03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of number-mult-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220185118-190bd2ad-4828-41d6-8afb-d389d99b5c2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-multi-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220184548-0e37b6e9-b953-4659-8849-3e41b8a3dcf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of number-div-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220185233-9f6ca09f-4c09-423e-b548-47b8b57dc085.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-div-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112834/220183979-53d89aa2-20c5-411f-aaf2-e25c9bcd817c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful pytest output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>In this module I learned how classes work and how it is possible<br>to import them between files. Coming from a java/c++ background, I can see<br>similarities in how imports work, but I would say it is definitely easier<br>in Python. I also have never used test cases before, so learning how<br>they work and their uses was very intriguing.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases are used to make sure that a function you are working<br>on works correctly while you are making changes to it. In the test<br>functions, you give set parameters that are always passed through the function along<br>with a set output that you always want the function to give, and<br>the test function will determine if the function gives those outputs. Test cases<br>allow programmers to efficiently test their functions without having to manually input parameters<br>every time they want to test. I had never used test cases before,<br>so getting to work with them hands on has shown me how valuable<br>these functions are for the efficiency as well as accuracy of a programmer&#39;s<br>work.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/beckgoz/IS601-004/pull/11">https://github.com/beckgoz/IS601-004/pull/11</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/bag27" target="_blank">Grading</a></td></tr></table>