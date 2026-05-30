"""
Example: call the Google Jobs API (Pay Per Result) Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

Billing note: this Actor is billed per result returned. The example asks for
num_results=10 (the minimum the Actor accepts) so the first run stays cheap.
Raise num_results only when you are ready to pay for more results.

Also available: a pay-per-page edition at
https://apify.com/johnvc/Google-Jobs-Scraper?fpr=9n7kx3
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive. This Actor bills per
# result, and num_results=10 is the minimum it accepts.
run_input = {
    "query": "Software Engineer",
    "location": "Austin, TX",
    "country": "us",
    "language": "en",
    "num_results": 10,
    # Optional filters (uncomment to exclude specific companies or job sources):
    # "company_filter_list": ["Staffing Agency A", "Staffing Agency B"],
    # "via_filter_list": ["ZipRecruiter"],
    # "company_filter_regex": True,  # treat the filters above as regex patterns
}

print(f"Searching jobs for: {run_input['query']} in {run_input['location']}")
run = client.actor("johnvc/google-jobs-scraper---pay-per-result").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"\nReturned {len(items)} job listings.\n")

for i, job in enumerate(items, start=1):
    title = job.get("title", "")
    company = job.get("company_name") or job.get("company") or ""
    location = job.get("location", "")
    via = job.get("via", "")

    print(f"{i}. {title}")
    print(f"   Company:  {company}")
    print(f"   Location: {location}")
    print(f"   Source:   {via}")

    apply_options = job.get("apply_options") or []
    if apply_options:
        first = apply_options[0]
        print(f"   Apply:    {first.get('title', '')} -> {first.get('link', '')}")

    description = job.get("description") or ""
    if description:
        snippet = description[:160].replace("\n", " ").strip()
        print(f"   About:    {snippet}...")
    print()
