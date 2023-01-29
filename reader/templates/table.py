import webbrowser
import time

variable=3

html_content=f"<html> <head> </head> <body> {variable} </body> </html>"

with open("new_table.html","w") as html_file:
    html_file.write(html_content)