from invoke import task


@task
def new(ctx):
    """Initialize new problem"""
    problem_id = input("Please enter problem id: ")
    problem_title = input("Please input problem title: ")

    directory_name = (
        f"p_{int(problem_id):04}_{problem_title.strip().lower().replace(' ', '_')}"
    )
    default_files = ["__init__.py"]
    ctx.run(f"mkdir problem/{directory_name}", pty=True)

    for default_file in default_files:
        ctx.run(f"touch problem/{directory_name}/{default_file}", pty=True)

    ctx.run(f"cp tasks/sample_file/solutions.py problem/{directory_name}")
    ctx.run(f"cp tasks/sample_file/test_solutions.py problem/{directory_name}")


@task
def count(ctx):
    """Count solved problems"""
    result = ctx.run(
        f"git ls-tree master --name-only problem/ | grep p_ | wc", hide="both"
    ).stdout.strip()
    print(f"{result} problems solved")


#
@task(optional=["problem_id"])
def test(ctx, problem_id=None):
    if not problem_id:
        problem_id = input("Please enter problem id: ")

    problem_full_name = ctx.run(
        f"ls problem | grep p_{int(problem_id):04}"
    ).stdout.strip()

    ctx.run(f"pipenv run pytest problem/{problem_full_name}")
