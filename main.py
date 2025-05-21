import time

import requests

bewerbung_urls = [
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDEtMTAwMTI0Nzg0My1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDAtMTIwMTU3MTk3MS1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDAtMTE5OTg4ODgxNi1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDAtMTIwMjE1NjU3MS1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTIyMTAtN2I3OGY3YjZkOTcwNGY4LVM/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTEwODEtMTMxMjU3NTctUw/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDEtMTAwMDg3MjQ0My1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDEtMTAwMDA2MDUxOC1T/bewerbung",
    "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDAtMTE5ODQyNjYzMy1T/bewerbung",
]

for url in bewerbung_urls:

    assignment_url = "https://rest.arbeitsagentur.de/idaas/id-aas-service/pc/v1/assignment"
    assignment_payload = {
        "formId": "ARBEITGEBERDATEN",
        "formProtectionLevel": "JB_JOBSUCHE_20",
        "sessionId": "645996DE-E6CE-4505-AD79-6201217F4E0E"
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-api-key": "jobboerse-jobsuche"
    }

    response = requests.post(assignment_url, json=assignment_payload, headers=headers)

    if response.status_code == 200:
        assignment_data = response.json()
        session_id = assignment_data.get('sessionId')
        challenge_id = assignment_data.get('challengeId')
        challenge_type = assignment_data.get('challengeType')
        print(f"Session ID: {session_id}, Challenge ID: {challenge_id}, Challenge Type: {challenge_type}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    # bewerbung_url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobs/MTAwMDAtMTIwMTU3MTk3MS1T/bewerbung"

    bewerbung_headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-api-key": "jobboerse-jobsuche",
        "aas-info": f"sessionId={session_id},challengeId={challenge_id}"
    }

    bewerbung_response = requests.get(url, headers=bewerbung_headers)

    if bewerbung_response.status_code == 200:
        for key, value in bewerbung_response.json().get("angebotskontakt").items():
            print(f"{key}: {value}")
    else:
        print(f"Error: {bewerbung_response.status_code}")
        print(bewerbung_response.text)

    time.sleep(1)
