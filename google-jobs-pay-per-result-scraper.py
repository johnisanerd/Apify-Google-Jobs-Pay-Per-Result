"""
Google Jobs Pay-Per-Result Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-jobs-scraper---pay-per-result/input-schema?fpr=9n7kx3

This script demonstrates how to scrape Google Jobs listings using the
pay-per-result pricing model - you are only charged for results returned.
Supports location-based searches, company filtering, and pagination.

Also available: pay-per-event variant at https://apify.com/johnvc/Google-Jobs-Scraper?fpr=9n7kx3

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "query": "Software Engineer",
    "location": "Austin, TX",
    "country": "us",
    "language": "en",
    "num_results": 50,
    "max_pagination": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-jobs-scraper---pay-per-result").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
