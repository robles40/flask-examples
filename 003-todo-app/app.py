from flask import Flask, make_response, render_template, redirect, url_for, request
from todo_form import TodoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lorem'

items = []


@app.route('/')
def home():
    return redirect(url_for('todos'))


@app.route('/todos', methods=('GET', 'POST'))
def todos():
    form = TodoForm()
    if form.validate_on_submit():
        new_item = request.form.get('title', '')
        items.insert(0, new_item)
        return redirect(url_for('todos'))
    return render_template('todos.html', form=form, todos=items)


@app.route('/delete', methods=('POST',))
def delete_todo():
    try:
        items.pop(int(request.form.get('todo_index')))
    except IndexError:
        # Handle Index out of range
        pass
    return redirect(url_for('todos'))


@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template('404.html'), 404
