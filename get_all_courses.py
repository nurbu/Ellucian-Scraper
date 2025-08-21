"""
Simple runner for getting ALL courses from Ellucian

This script just runs the scraper to get all courses without any prompts.
Make sure your auth credentials are updated in ellucian_scraper.py first!
"""

from ellucian_scraper import EllucianScraper
import time

def main():
    print("🎓 Ellucian All Courses Scraper")
    print("=" * 50)
    
    scraper = EllucianScraper()
    
    # Quick test first
    print("🔍 Testing connection...")
    test_result = scraper.search_courses(term="202540", page_max_size=1)
    
    if not test_result or not test_result.get('success'):
        print("❌ Connection failed!")
        print("Update your authentication credentials in ellucian_scraper.py:")
        print("  - JSESSIONID cookie")
        print("  - X-Synchronizer-Token header")
        return
    
    total_courses = test_result.get('totalCount', 0)
    print(f"✅ Connected! Found {total_courses} total courses")
    
    # Get ALL courses
    print(f"\n🚀 Starting to scrape all {total_courses} courses...")
    print("⏳ This will take several minutes...")
    
    start_time = time.time()
    all_courses = scraper.get_all_courses(term="202540", max_pages=None)
    end_time = time.time()
    
    if all_courses:
        print(f"\n🎉 Success! Scraped {len(all_courses)} courses")
        print(f"⏱️  Time taken: {(end_time - start_time)/60:.1f} minutes")
        
        # Save to file
        filename = 'all_ellucian_courses.json'
        scraper.save_courses_to_file(all_courses, filename)
        
        # Quick stats
        subjects = {}
        open_count = 0
        total_enrollment = 0
        total_capacity = 0
        
        for course in all_courses:
            subject = course.get('subject', 'Unknown')
            subjects[subject] = subjects.get(subject, 0) + 1
            
            if course.get('openSection'):
                open_count += 1
            
            total_enrollment += course.get('enrollment', 0) or 0
            total_capacity += course.get('maximumEnrollment', 0) or 0
        
        print(f"\n📊 Quick Statistics:")
        print(f"  📚 Total courses: {len(all_courses)}")
        print(f"  🟢 Open sections: {open_count}")
        print(f"  🔴 Closed sections: {len(all_courses) - open_count}")
        print(f"  🎓 Total enrollment: {total_enrollment:,}")
        print(f"  🏫 Unique subjects: {len(subjects)}")
        print(f"  📁 Saved to: {filename}")
        
        print(f"\n🔝 Top 5 subjects:")
        for subject, count in sorted(subjects.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"    {subject}: {count} courses")
            
    else:
        print("❌ Failed to scrape courses")
        print("Check your authentication and try again")

if __name__ == "__main__":
    main()
