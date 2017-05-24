import todo
import uuid
import time
from flask import Flask, request, render_template, redirect

app = Flask("ToDoWeb")


# Standard Webseite
@app.route("/")
def index():
    return render_template("list.html", notes=sort_notes(todo.read_data_from_file()))


@app.route("/button_search")
def button_search():
    return render_template("list.html", notes=sort_notes(todo.read_data_from_file()))


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


def sort_notes(notes):
    sorted_notes = notes
    for i in range(2, len(notes)):
        sortin = notes[i]
        j = i
        while j > 1 and time.strptime(notes[j - 1].getDate(), "%m/%d/%Y") > time.strptime(sortin.getDate(), "%m/%d/%Y"):
            notes[j] = notes[j - 1]
            j = j - 1
        sorted_notes[j] = sortin
    return sorted_notes


@app.route("/search")
def list_filtered_notes():
    search = request.args.get('search')
    return render_template("list.html", notes=sort_notes(todo.read_data_from_file(search)))


@app.route("/list")
def list_notes():
    return render_template("list.html", notes=sort_notes(todo.read_data_from_file()))


# Neuen Eintrag hinzufügen
@app.route("/add", methods=['POST'])
def add_note():
    taskname = request.form.get('name')
    taskdate = request.form.get('date')
    todo.new_task(taskdate, taskname, uuid.uuid4())
    return redirect("/list", code=302)


@app.route('/button_add_new')
def button_add_new():
    return render_template("add.html")


@app.route('/button_edit')
def button_edit():
    return render_template("edit.html", notes=sort_notes(todo.read_data_from_file()))


if __name__ == '__main__':
    app.run(debug=True)
