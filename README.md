# 💼 Google Jobs Pay-Per-Result Scraper: Scrape Google Jobs Listings with Python

> **The most efficient, reliable, and developer-friendly Google Jobs scraper - pay only for results returned**

**Actor page:** [apify.com/johnvc/google-jobs-scraper---pay-per-result](https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-jobs-scraper---pay-per-result/input-schema](https://apify.com/johnvc/google-jobs-scraper---pay-per-result/input-schema?fpr=9n7kx3)

Scrape Google Jobs listings with Python using the [Google Jobs Pay-Per-Result scraper on Apify](https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3). Returns structured JSON with job titles, companies, locations, descriptions, and apply links - with pay-per-result pricing so you are only charged for the job listings actually returned.

> Also available: [pay-per-event variant](https://apify.com/johnvc/Google-Jobs-Scraper?fpr=9n7kx3) - better suited for high-volume runs where you expect consistent result counts.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Jobs-Pay-Per-Result.git
   cd Apify-Google-Jobs-Pay-Per-Result
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you don't have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-jobs-pay-per-result-scraper.py
   ```

### Alternative: Set API Key Directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-jobs-pay-per-result-scraper.py
```

## 🌟 Why Use This Google Jobs Pay-Per-Result Scraper?

The [Google Jobs Pay-Per-Result scraper on Apify](https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3) delivers structured job listing data from Google Jobs - the aggregated job index that pulls postings from LinkedIn, Indeed, Glassdoor, company career pages, and thousands of other sources into a single searchable surface.

**Only Pay for What You Get**: With pay-per-result pricing, your cost is tied directly to the number of job listings returned. If a query yields 50 results, you pay for 50 results - no per-page overhead, no charges for empty pages. This makes the scraper especially cost-effective for targeted searches where result counts vary.

**Broad Job Market Coverage**: Google Jobs aggregates listings from across the web - company career sites, major job boards, and niche industry postings all appear together. A single query surfaces opportunities that would otherwise require searching multiple platforms individually.

**Location and Language Precision**: Filter results by `location`, `country`, and `language` to target specific labor markets. Whether you need software engineering roles in Austin, finance jobs in London, or marketing positions in Germany, the input parameters let you scope results precisely without post-filtering.

**Company and Source Filtering**: Use `company_filter` or `company_filter_list` to restrict results to specific employers, with optional regex support for flexible matching. The `via_filter` parameter restricts results by job board source - useful when you only want results from specific platforms.

**Configurable Result Volume**: Set `num_results` to control how many listings to collect per run, and `max_pagination` to limit page depth. This makes it straightforward to run quick spot checks or large-scale market surveys from the same configuration.

**Production-Ready for Talent Intelligence**: Job listing data powers recruiting pipelines, labor market research, compensation benchmarking, and competitive talent analysis. The [Google Jobs scraper](https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3) returns clean, consistently structured JSON ready to load directly into any of these workflows.

## 🎯 Common Use Cases for Google Jobs Data

**Recruiting and Talent Sourcing**: Monitor job openings at target companies or in specific roles to inform recruiting strategy and identify active hiring signals.

**Labor Market Research**: Track job posting volumes, required skills, and compensation ranges across industries, roles, and geographies over time.

**Compensation Benchmarking**: Collect salary data from job descriptions to benchmark roles against market rates across regions and company sizes.

**Competitive Intelligence**: Monitor competitor hiring activity to identify product priorities, team expansions, and strategic shifts before they become public.

**Job Board and Aggregator Development**: Source structured job listing data to populate a niche job board, career resource, or skills gap analysis tool.

**Academic Research**: Build datasets of job postings for labor economics, skills demand analysis, or workforce development research.

## ⚡ Features

### Core Capabilities
- **Google Jobs Index**: Queries Google's aggregated job listing index across all major sources
- **Pay-Per-Result Pricing**: Charged only for job listings actually returned, not pages processed
- **Location Targeting**: Filter by `location`, `country`, and `language` for precise market scoping
- **Company Filtering**: Restrict results to specific employers with string, list, or regex matching
- **Source Filtering**: Limit results to specific job boards or platforms with `via_filter`
- **Configurable Volume**: Control result count with `num_results` and depth with `max_pagination`

### Data Quality
- **Consistent JSON Schema**: Every job listing shares the same field structure regardless of source
- **Full Job Details**: Title, company, location, description, and apply link on every result
- **Source Attribution**: Which platform or site each listing was sourced from
- **Location Radius Support**: Optional `lrad_value` for distance-based location filtering
- **Request Throttling**: Configurable `max_delay` to manage request pacing

## 📖 Usage Examples

### Basic Search: Scrape Google Jobs for Any Role

```json
{
  "query": "Data Scientist",
  "num_results": 50
}
```

### Advanced Search: Location-Targeted with Company Filter

Retrieve Software Engineer roles in Austin, TX filtered to specific companies, with 2 pages of results.

```json
{
  "query": "Software Engineer",
  "location": "Austin, TX",
  "country": "us",
  "language": "en",
  "num_results": 100,
  "max_pagination": 2,
  "company_filter_list": ["Google", "Meta", "Apple"]
}
```

## 🔍 Input Parameters

Full input schema reference: [apify.com/johnvc/google-jobs-scraper---pay-per-result/input-schema](https://apify.com/johnvc/google-jobs-scraper---pay-per-result/input-schema?fpr=9n7kx3)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | YES | - | Job search query |
| `location` | `str` | no | - | Job location (e.g. `"Austin, TX"`) |
| `country` | `str` | no | - | Country code (e.g. `"us"`) |
| `language` | `str` | no | - | Language code (e.g. `"en"`) |
| `google_domain` | `str` | no | `"google.com"` | Google domain to use |
| `num_results` | `int` | no | `100` | Number of results to return |
| `max_pagination` | `int` | no | `0` | Max pages (0 = no limit) |
| `include_lrad` | `bool` | no | `false` | Include location radius filter |
| `lrad_value` | `str` | no | - | Location radius value |
| `max_delay` | `int` | no | `1` | Request delay in seconds |
| `company_filter` | `str` | no | - | Filter by company name |
| `company_filter_list` | `array` | no | - | Filter by list of company names |
| `company_filter_regex` | `bool` | no | `false` | Use regex for company filter |
| `via_filter` | `str` | no | - | Filter by job source platform |
| `via_filter_list` | `array` | no | - | Filter by list of job source platforms |

## 📊 Output Format

Each run returns a dataset of structured JSON objects. Sample output:

```json
{
  "query": "Software Engineer",
  "location": "Austin, TX",
  "country": "us",
  "num_results": 50,
  "results_returned": 50,
  "jobs": [
    {
      "position": 1,
      "title": "Senior Software Engineer, Backend",
      "company": "Cloudflare",
      "location": "Austin, TX",
      "via": "LinkedIn",
      "description": "We are looking for a Senior Software Engineer to join our backend infrastructure team. You will design and build distributed systems that handle millions of requests per second...",
      "apply_link": "https://www.linkedin.com/jobs/view/example",
      "posted_at": "3 days ago",
      "employment_type": "Full-time",
      "salary": "$160,000 - $200,000 a year"
    },
    {
      "position": 2,
      "title": "Software Engineer II",
      "company": "Dell Technologies",
      "location": "Austin, TX (Hybrid)",
      "via": "Indeed",
      "description": "Join our engineering team building next-generation storage solutions. Experience with distributed systems and Go or C++ required...",
      "apply_link": "https://www.indeed.com/viewjob?jk=example",
      "posted_at": "1 week ago",
      "employment_type": "Full-time",
      "salary": null
    }
  ]
}
```

---

[**Made with love**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your data collection with the most reliable and efficient scraper on the market.*

Last Updated: 2026.04.15
