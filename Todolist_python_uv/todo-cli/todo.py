import click
import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """A simple CLI for managing TODO tasks."""
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a new task to the TODO list."""
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    click.echo(f'Task added successfully: {task}')

@cli.command()
def list():
    """List all tasks in the TODO list."""
    tasks = load_tasks()
    if not tasks:
        click.echo('No tasks found.')
    else:
        for index, task in enumerate(tasks, 1):
            status = '✓' if task['done'] else '✗'
            click.echo(f"{index}. [{status}] {task['task']}")
            
@cli.command()
@click.argument('task_number', type=int)
def complete():
    """Mark the first task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f'Task {task_number} marked as completed.')
    else:
        click.echo(f"Invalid task number: {task_number}")
        
        
@cli.command()
@click.argument('task_number', type=int)
def remove(task_number):
    """Remove a task from the TODO list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f'Task removed: {removed_task["task"]}')
    else:
        click.echo(f"Invalid task number: {task_number}")        

if __name__ == '__main__':
    cli()
