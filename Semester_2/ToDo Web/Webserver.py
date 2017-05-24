import todo
import uuid
from flask import Flask, request, render_template, redirect

app = Flask("ToDoWeb")


# Standard Webseite
@app.route("/")
def index():
    return render_template("list.html", notes=todo.read_data_from_file())


# Route zur Verarbeitung der Form in edit.html
@app.route("/process", methods=['POST'])
def process():
    id = request.form.get('id')
    if request.form.get('submit') == 'delete':
        todo.delete_task(id)
    else:
        title = request.form.get('title')
        date = request.form.get('date')
        todo.edit_task(id, title, date)
    notes = todo.read_data_from_file()
    return render_template("edit.html", notes=notes)


@app.route("/list")
def list_notes():
    return render_template("list.html", notes=todo.read_data_from_file())


# Neuen Eintrag hinzufügen
@app.route("/add", methods=['POST'])
def add_note():
    taskname = request.form.get('name')
    taskdate = request.form.get('date')
    todo.new_task(taskdate,taskname, uuid.uuid4())
    return redirect("/list", code=302)


@app.route('/button_add_new')
def button_add_new():
    return render_template("add.html")


@app.route('/button_edit')
def button_edit():
    notes = todo.read_data_from_file()
    return render_template("edit.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
