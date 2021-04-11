
from ..request_api import requests_by_get
from ..models.job import Job


def get_job(job_id, token):
    url = f"https://coding-test.rootstack.net/api/jobs/{job_id}"
    response = requests_by_get(url, token)
    if response and not response.get('message'):
        job = Job(**response)
        return job
    return False


def get_jobs(token):
    url = "https://coding-test.rootstack.net/api/jobs"
    response = requests_by_get(url, token)

    job_ids = []
    if response and response.get('data') and not response.get('message'):
        for job_json in response.get('data'):
            job_id = Job(**job_json)
            job_ids.append(job_id)

    return job_ids
