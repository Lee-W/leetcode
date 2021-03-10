from invoke import task

@task
def new(ctx):
    """Initialize new problem"""
    problem_id = input("Please enter problem id: ")
    problem_title = input("Please input problem title: ")

    directory_name = f"p_{problem_id}_{problem_title.lower().replace(' ', '_')}"
    default_files = ["__init__.py", "solutions.py", "test_solutions.py"]
    ctx.run(f"mkdir problem/{directory_name}", pty=True)

    for default_file in default_files:
        ctx.run(f"touch problem/{directory_name}/{default_file}", pty=True)

@task
def count(ctx):
    """Count solved problems"""
    result = ctx.run(f"ls -l problem | grep p_ | wc -l", hide="both").stdout.strip()
    print(f"{result} problems solved")
