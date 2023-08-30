<h1>Integration between Trello and Google Sheets</h1>
<p>Integration between Trello and Google Sheets trough APIs to checklist tasks on the card have been completed. The code checks every 60 seconds if the items
have been marked as completed and inserts the information into the selected Google Sheet.</p>

<ol>
<li>We import the libraries</li>
<li>We create and set up the Trello keys and Google credentials through the Google Console for using Sheets</li>
<li>We define the function to authenticate the Google credentials</li>
<li>We define the function to use the credentials. Within the "While True" loop, it clears the entered data to consistently update the information coming from the "for" loop</li>
<li>The code checks every 60 seconds if the tasks have marked as completed</li>
</ol>
<img src="https://github.com/danoliver1792/works/assets/99451711/4a8c2e15-16de-4fb8-beee-9210227fd9c0">
<img src="https://github.com/danoliver1792/works/assets/99451711/052a937f-f9b4-42c9-9817-d596860996b7">
<img src="https://github.com/danoliver1792/works/assets/99451711/b625070d-6608-4d67-ab93-ea4590860053">
