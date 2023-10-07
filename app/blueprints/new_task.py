from flask import Blueprint, render_template, redirect, request


new_task_bp = Blueprint(
    "new_task_bp",
    __name__,
)


@new_task_bp.route("/new-task/")
def add_task():
    return render_template("new-task.html")
