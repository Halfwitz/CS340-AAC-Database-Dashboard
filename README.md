# CS340-AAC-Database-Dashboard
A web-based dashboard built with Python Dash and uses a PyMongo driver to query from the MongoDB database
Developed by Michael Lorenz
Developed for SNHU CS340 Client/Server Development course

Project Reflection
---

#### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

I write maintainable programs, such as the CRUD Python Module, by focusing on single-responsibility functions like the read() method with the task of returning a queries results, and modular design with reusable components like the verifyNotNone() function to verify the input for each CRUD function. To promote readability, I include clear documentation through inline comments to describe the purpose, inputs, and outputs of each function and a detailed README for installation and usage instructions. By adding a constructor that accepts username, password, database, and other arguments, I ensure the module can adapt to other databases, allowing me to use the CRUD module for any MongoDB database project. 

---

#### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
I break problems into manageable subproblems and structure the solution meaningfully. For this project, I divided the PyMongo module task into distinct operations: create, read, update, and delete. I applied the Model-View-Controller architecture to the dashboard to separate the MongoDB/PyMongo data layer (Model), Dash UI (View), and logic of Dash callbacks (Controller), which differs from the structure of previous assignments. Using this strategy in future database projects provides organization and scalability to the project. 

---

#### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists develop and apply algorithms to solve complex problems, often allowing automation of tasks or improved efficiency and reliability. My work on this project helped Grazioso Salvare with automated data analysis and visualization, saving time and producing solutions that would be difficult or impossible to achieve manually. This type of work matters by allowing organizations to enhance the convenience and reliability of tasks and make data-driven decisions. 

