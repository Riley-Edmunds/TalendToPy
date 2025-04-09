from prefect import flow
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret


if __name__ == "__main__":

    github_repo = GitRepository(
        url=r"https://github.com/Riley-Edmunds/TalendToPy.git",
        credentials={
            "access_token": Secret.load("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")
        },
    )

    flow.from_source(
        source=github_repo,
        entrypoint="test_prefect.py:show_stars", # Specific flow to run
    ).deploy(
        name="test-prefect-deployment",
        parameters={
            "github_repos": [
                "PrefectHQ/prefect",
                "pydantic/pydantic",
                "huggingface/transformers"
            ]
        },
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every hour
    )
