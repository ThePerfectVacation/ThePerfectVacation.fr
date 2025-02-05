import os
from datetime import datetime

# Paths for your website files
BASE_DIR = "/Users/s.shabreznoorani/Documents/ThePerfectVacation.fr"
BLOG_DIR = os.path.join(BASE_DIR, "blog")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
BLOG_INDEX_FILE = os.path.join(BLOG_DIR, "index.html")

# Function to create a new blog post file
def create_blog_post(title, content):
    # Generate filename from title
    filename = title.lower().replace(" ", "-") + ".html"
    post_path = os.path.join(BLOG_DIR, filename)
    
    # Generate HTML for the blog post
    blog_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title} - The Perfect Vacation</title>
        <link rel="stylesheet" href="../assets/css/style.css">
    </head>
    <body>
        <div class="blog-post">
            <h1>{title}</h1>
            <p><em>Published on {datetime.now().strftime('%d %B %Y')}</em></p>
            <div class="content">{content.replace('\n', '<br>')}</div>
        </div>
        <a href="index.html">Back to Blog</a>
    </body>
    </html>
    """
    
    # Write to file
    with open(post_path, "w", encoding="utf-8") as file:
        file.write(blog_html)
    
    return filename

# Function to update homepage and blog index with summary
def update_summary(title, filename, summary):
    new_entry = f"""
    <div class="blog-entry">
        <h2><a href="blog/{filename}">{title}</a></h2>
        <p>{summary} <a href="blog/{filename}">Read More</a></p>
    </div>
    """
    
    # Update homepage
    with open(INDEX_FILE, "r", encoding="utf-8") as file:
        homepage = file.readlines()
    
    insert_pos = homepage.index("<!-- BLOG_SECTION_START -->\n") + 1
    homepage.insert(insert_pos, new_entry + "\n")
    
    with open(INDEX_FILE, "w", encoding="utf-8") as file:
        file.writelines(homepage)
    
    # Update blog index
    with open(BLOG_INDEX_FILE, "r", encoding="utf-8") as file:
        blog_index = file.readlines()
    
    insert_pos = blog_index.index("<!-- BLOG_SECTION_START -->\n") + 1
    blog_index.insert(insert_pos, new_entry + "\n")
    
    with open(BLOG_INDEX_FILE, "w", encoding="utf-8") as file:
        file.writelines(blog_index)

# Get user input
title = input("Enter blog title: ")
print("Enter blog content (type 'END' on a new line to finish):")
content = ""
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    content += line + "\n"

summary = input("Enter a short summary for homepage and blog index: ")

# Create blog post and update pages
filename = create_blog_post(title, content)
update_summary(title, filename, summary)

print(f"Blog post '{title}' created successfully at {filename}!")

