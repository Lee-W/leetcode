from invoke import task

from tasks.common import PIPENV_PREFIX


@task
def commit(ctx):
    """Commit through commitizen"""
    ctx.run(f"{PIPENV_PREFIX} cz commit", pty=True)
