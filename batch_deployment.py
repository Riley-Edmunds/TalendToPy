from prefect import flow
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials

if __name__ == "__main__":

    github_creds = GitHubCredentials.load("talendtopython")

    github_repo = GitRepository(
        url="https://github.com/Riley-Edmunds/TalendToPy.git",
        credentials=github_creds
    )

    flow.from_source(
        source=github_repo,
        entrypoint="batch_prefect.py:master_flow", # Specific flow to run
    ).deploy(
        name="batch-flow-deployment",
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every hour
    )
