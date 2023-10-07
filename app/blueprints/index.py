from flask import Blueprint, render_template, redirect, request
from ..models.task import Task, db


index_bp = Blueprint(
    "index_bp",
    __name__,
)


@index_bp.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        new_task = Task(description=description, completed=False)
        db.session.add(new_task)
        db.session.commit()

    db_info = Task.query.all()

    return render_template("index.html", db_info=db_info)


@index_bp.route("/populate/")
def populate():
    # Sample data to be inserted
    sample_data = [
        (1, "Comprar leche", 0),
        (2, "Lavar la ropa", 0),
        (3, "Pasear al perro", 1),
        (4, "Limpiar la casa", 0),
        (5, "Preparar la cena", 1),
        (6, "Hacer la cama", 1),
        (7, "Estudiar para el examen", 1),
        (8, "Leer un libro", 0),
        (9, "Escribir un correo electrónico", 1),
        (10, "Ir al supermercado", 1),
        (11, "Sacar la basura", 0),
        (12, "Planchar la ropa", 1),
        (13, "Cortar el césped", 1),
        (14, "Lavar los platos", 0),
        (15, "Limpiar el baño", 0),
        (16, "Hornear un pastel", 0),
        (17, "Preparar una presentación", 0),
        (18, "Escribir un artículo", 0),
    ]

    # Function to insert sample data
    for task_data in sample_data:
        new_task = Task(description=task_data[1], completed=task_data[2])
        db.session.add(new_task)
    db.session.commit()

    return redirect("/")
