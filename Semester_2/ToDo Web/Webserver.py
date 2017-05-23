import todo
from flask import Flask, request, render_template

app = Flask("ToDoWeb")


# Standard Webseite
@app.route("/")
def index():
    return render_template("list.html", notes=todo.read_data_from_file())


# Route zur Verarbeitung der Form in edit.html
@app.route("/process")
def process():
    id = int(request.args.get('id'))
    if request.args.get('submit') == 'delete':
        todo.delete_task(id - 1)
    else:
        title = request.args.get('title')
        date = request.args.get('date')
        todo.edit_task(id - 1, title, date)
    notes = todo.read_data_from_file()
    return render_template("edit.html", notes=notes)


@app.route("/list")
def list_notes():
    return render_template("list.html", notes=todo.read_data_from_file())


# Neuen Eintrag hinzufügen
@app.route("/add")
def add_note():
    taskname = request.args.get('name')
    taskdate = request.args.get('date')
    todo.new_task(taskname, taskdate)
    return render_template("list.html", notes=todo.read_data_from_file())


@app.route('/button_add_new')
def button_add_new():
    return render_template("add.html")


@app.route('/button_edit')
def button_edit():
    notes = todo.read_data_from_file()
    return render_template("edit.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
