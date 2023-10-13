"""
Virtual environments they allow you to separate Python dependencies by project and give you the ability to select
between different versions of the Python interpreter.
On Linux or macOS, we can use the which command-line tool to look up the path to the pip package manager.
"""
# $ which pip3
# /usr/local/bin/pip3

# python3 -m venv ./venv

# $ source ./venv/bin/activate

"""
By running pip list again, you can see that the schedule library was installed successfully into the new environment.
"""

# $ deactivate