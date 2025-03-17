# Secure Filesystem Project
These files make up a secure server/client that will allow a user to create an account to send, store, and retrieve encrypted files. The end goal will have the user able to access files from a password protected server accessible from anyone with the secure client.

Use: Run application.py in terminal to run the main application
Terminal: python3 application.py

A menu will appear asking you to register or login, create an account using the numbered options and entering a username and password.

Login to create an account, and use an instance to start up a server (option 4).

Create another instance, and put your file in the directory containing the application. Enter your file name and select send file. The file will be sent through the server and will transfer to the end client application.

Decode the sent file using application.py's decode function.

Next step is to incorporate AWS elements into the project, hopefully such as storing the users in a database instead of a CSV file.
