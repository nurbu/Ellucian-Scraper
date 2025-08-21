# Ellucian Course Scraper

Simple scraper for Montclair State University's Ellucian course system.

## Files

- **`ellucian_scraper.py`** - Main scraper with all functionality
- **`get_all_courses.py`** - Simple script to get all ~5000 courses
- **`README_ellucian.md`** - This file

## Quick Start (Get All Courses)

1. **Update Authentication** in `ellucian_scraper.py`:
   - Get fresh `JSESSIONID` cookie from browser  
   - Get fresh `X-Synchronizer-Token` header
   - Both expire after ~30 minutes

2. **Run the scraper**:
   ```bash
   python get_all_courses.py
   ```

3. **Wait 5-10 minutes** for all courses to download

4. **Find your data** in `all_ellucian_courses.json`

## How to Get Fresh Authentication

1. Log into the course registration website
2. Open Developer Tools (F12) → Network tab
3. Search for any course
4. Find the `searchResults` request in Network tab
5. Copy these values:
   - **Cookie**: `JSESSIONID=ABC123...`
   - **Header**: `X-Synchronizer-Token: xyz-123...`
6. Update them in `ellucian_scraper.py`

## Pagination Logic

The scraper uses correct pagination:
- `pageOffset=0` & `pageMaxSize=50` → courses 0-49  
- `pageOffset=50` & `pageMaxSize=50` → courses 50-99
- `pageOffset=100` & `pageMaxSize=50` → courses 100-149
- etc.

## Output Data

Each course includes:
- Basic info (subject, number, title, CRN, credits)
- Enrollment (current/max, seats available, waitlist)  
- Faculty (names, emails)
- Schedule (days, times, building, room)
- All raw JSON data

## Filtering Examples

```python
from ellucian_scraper import EllucianScraper

scraper = EllucianScraper()
result = scraper.search_courses(term="202540", page_max_size=100)
courses = result.get('data', [])

# Filter examples
open_courses = scraper.filter_courses(courses, open_only=True)
math_courses = scraper.filter_courses(courses, subject='MATH')
tr_courses = scraper.filter_courses(courses, days='TR')
```

## Troubleshooting

**"Request failed with status 403"** → Update authentication

**"No data received"** → Check if logged into website  

**"JSON decode error"** → Authentication expired

**Takes too long** → Your auth probably expired mid-scrape

## Term Codes

- Fall 2025: `202540`
- Spring 2026: `202610` (estimated)

The scraper defaults to Fall 2025 (`202540`).
