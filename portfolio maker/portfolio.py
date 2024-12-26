# portfolio website maker

name = input("Enter your name: ")
description = input("Enter your description: ")

project1 = input("Enter your project name: ")
project_description1 = input("Enter the description of Project: ")
project_url1 = input("Enter your project url: ")

project2 = input("Enter your project name: ")
project_description2 = input("Enter the description of Project: ")
project_url2 = input("Enter your project url: ")

project3 = input("Enter your project name: ")
project_description3 = input("Enter the description of Project: ")
project_url3 = input("Enter your project url: ")

html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Portfolio Website</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }}
            header {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
            }}
            h1 {{
                margin: 0;
            }}
            main {{
                padding: 20px;
            }}
            h2 {{
                color: #4CAF50;
            }}
            hr {{
                border: none;
                border-top: 1px solid #ddd;
                margin: 20px 0;
            }}
            a {{
                color: #4CAF50;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            footer {{
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }}
        </style>
        <script>
            function greetUser() {{
                alert("Welcome to {name}'s portfolio website!");
            }}
            function highlightProjects() {{
                const projects = document.querySelectorAll("h3");
                projects.forEach(project => {{
                    project.style.color = "#4CAF50";
                    project.style.cursor = "pointer";
                    project.addEventListener("click", () => {{
                        alert("You clicked on: " + project.textContent);
                    }});
                }});
            }}
            window.onload = function() {{
                greetUser();
                highlightProjects();
            }};
        </script>
    </head>
    <body>
        <header>
            <h1>Portfolio Website</h1>
        </header>
        <main>
            <p>Hello! I am {name}, a cool programmer.</p>
            <p>{description}</p>
            <p>You can see my projects below:</p>
            <hr>
            <h2>My Projects</h2>
            <h3>{project1}</h3>
                <p>{project_description1}</p>
                <a href="{project_url1}" target="_blank">View Project</a>
            <hr>
            <h3>{project2}</h3>
                <p>{project_description2}</p>
                <a href="{project_url2}" target="_blank">View Project</a>
            <hr>
            <h3>{project3}</h3>
                <p>{project_description3}</p>
                <a href="{project_url3}" target="_blank">View Project</a>
            <hr>
        </main>
        <footer>
            <p>&copy; 2024 {name}'s Portfolio. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    """
    
with open("index.html", 'w') as f:
    f.write(html)
