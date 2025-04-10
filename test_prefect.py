import httpx

from prefect import flow, task # Prefect flow and task decorators

@flow
def show_stars(github_repos: list[str]):
    """Show the number of stars that GitHub repos have"""
    for repo in github_repos:
        repo_stats = fetch_stats(repo)
        stars = get_stars(repo_stats)
        print(f"{repo}: {stars} stars")

@task
def fetch_stats(github_repo: str):
    """Fetch the statistics for a GitHub repo"""
    response = httpx.get(f"https://api.github.com/repos/{github_repo}")
    try:
        response.raise_for_status()  # Raise exception for HTTP errors (e.g., 404, 403)
        return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": str(e), "status_code": response.status_code}

@task
def get_stars(repo_stats: dict):
    """Get the number of stars from GitHub repo statistics"""
    if "stargazers_count" in repo_stats:
        return repo_stats["stargazers_count"]
    elif "error" in repo_stats:
        return f"Error fetching repo: {repo_stats['error']}"
    else:
        return "Unknown error"

if __name__ == "__main__":
    show_stars([
        "PrefectHQ/prefect",
        "pydantic/pydantic",
        "huggingface/transformers"
    ])
