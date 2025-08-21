import requests
import json
from urllib.parse import urlencode
import time

class EllucianScraper:
    def __init__(self):
        self.base_url = "https://student-ssb-regis.montclair.edu/StudentRegistrationSsb/ssb/searchResults/searchResults"
        
        # Headers from your cURL command
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Referer": "https://student-ssb-regis.montclair.edu/StudentRegistrationSsb/ssb/classSearch/classSearch",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "X-Synchronizer-Token": "2c1c3e78-5d68-4e71-ae60-10713d77e5e0",
            "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }
        
        # Cookies from your cURL command (you'll need to update these when they expire)
        self.cookies = {
            "JSESSIONID": "D8A0276CF05E32B9A3CE5B78566F1D8B",
            "MSUSC01ea9485": "01a5c8b23b70a21c07860eb08d5a2c54860c366e577e074a5602f946f29602545d4a207702127db86f280b428c22ac99b4632817a21288006f27df99bee66ae7b5418550f471a26b2ba4de2f32ab604467a9f13940",
            "_gcl_au": "1.1.128957896.1753174875",
            "__utmzz": "utmcsr=google|utmcmd=organic|utmccn=(not set)|utmcct=(not set)|utmctr=(not provided)|utmgclid=(not set)|utmid=(not set)|msclkid=(not set)",
            "_fbp": "fb.1.1753174875575.8832695159083881",
            "detected-region": "non-eu",
            "remarketing": "on",
            "nmstat": "f1a85a19-702f-af40-80e9-4b3ddd475dec",
            "_cq_duid": "1.1753174875.gYrHKxh7pC4twS0M",
            "_tt_enable_cookie": "1",
            "_ttp": "01K0RNV7NTA6T7XJ9W71Z4BATW*.tt.1",
            "_mkto_trk": "id:893-QIF-790&token:_mch-montclair.edu-2f483188de67abe4df329bd47bf6dcf2",
            "_cq_82322_v": "ODIzMjJfY3EyMV9m",
            "_ga_R50DGR3B2Q": "GS2.1.s1754432229$o1$g1$t1754432333$j60$l0$h0",
            "VisitorType": "MON Internal User",
            "_ga_TTD4ZDP693": "GS2.2.s1755122423$o3$g1$t1755122427$j56$l0$h0",
            "_ga": "GA1.1.730912373.1753174875",
            "_ga_5J9EXYYT8H": "GS2.1.s1755151256$o6$g1$t1755151267$j49$l0$h0",
            "amlbcookie": "02",
            "MSUSC01e805d0": "01a5c8b23ba149db1dd3e4f4beb23956f36b2114004c5867fb411a95d326f83caa4807a21a53eda76eaf9de2532f033470a81a62464a7ef79b6c9b85325c80d7deccdbd8f7",
            "__utmzzses": "1",
            "_cq_suid": "1.1755561604.ulXEpWNRGlvVrJgU",
            "_ga_9LY1813ZZM": "GS2.1.s1755561604$o11$g0$t1755561604$j60$l0$h0",
            "_uetsid": "759c2d307c8f11f09869adcf5aaf7441",
            "_uetvid": "6c853e7066da11f087803b8dca2af5da",
            "ttcsid": "1755561604434::XrHF69w9XwCrpXKbKQBp.9.1755561604434",
            "_clck": "1nzjni0%7C2%7Cfyl%7C0%7C2029",
            "_ga_376R1V222B": "GS2.1.s1755561604$o11$g0$t1755561604$j60$l0$h0",
            "ttcsid_CU3T5KJC77U46J7ET1AG": "1755561604433::ErOTTUN8dWUCPbQR4TqV.9.1755561604804",
            "_clsk": "4wrygh%7C1755561604820%7C1%7C1%7Ck.clarity.ms%2Fcollect",
            "student-ssb-regis.montclair.edu*https": "!M4tYguS/UJYuinUNfp7y1k4lowZedAmaqM7xBAqq/aIdDQQH4QC3VNpQKop2NX0psITS5w17b0Bi+pQ=",
            "MSUSC018b69e0": "01a5c8b23bd0f75a9615de482824740087daeac417eea291193518078de875b81a831c3cc4d35d3f360f8d9dcc908ef72f7809e734a86cf5f8a3cc126f2f31ae4de47e61a7"
        }
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.cookies.update(self.cookies)

    def search_courses(self, term="202540", page_offset=0, page_max_size=10, 
                      start_date="", end_date="", unique_session_id="e7q2x1755561616166",
                      sort_column="subjectDescription", sort_direction="asc"):
        """
        Search for courses with given parameters
        
        Args:
            term: Academic term (default: 202540)
            page_offset: Starting position (0, 50, 100, etc.)
            page_max_size: Number of results per page (default: 10)
            start_date: Start date filter (default: empty)
            end_date: End date filter (default: empty)
            unique_session_id: Session ID (you might need to update this)
            sort_column: Column to sort by (default: subjectDescription)
            sort_direction: Sort direction asc/desc (default: asc)
            
        Returns:
            dict: Response with 'success', 'totalCount', and 'data' fields
        """
        
        # Build query parameters
        params = {
            "txt_term": term,
            "startDatepicker": start_date,
            "endDatepicker": end_date,
            "uniqueSessionId": unique_session_id,
            "pageOffset": page_offset,
            "pageMaxSize": page_max_size,
            "sortColumn": sort_column,
            "sortDirection": sort_direction
        }
        
        try:
            print(f"Making request to: {self.base_url}")
            print(f"Parameters: {params}")
            
            response = self.session.get(self.base_url, params=params, timeout=30)
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"✓ Successfully received JSON response")
                    print(f"✓ Total courses available: {data.get('totalCount', 'unknown')}")
                    print(f"✓ Courses in this page: {len(data.get('data', []))}")
                    return data
                except json.JSONDecodeError as e:
                    print(f"✗ Failed to parse JSON: {e}")
                    print("Raw response:", response.text[:500])
                    return None
            else:
                print(f"✗ Request failed with status {response.status_code}")
                print("Response text:", response.text[:500])
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"✗ Request error: {e}")
            return None

    def get_all_courses(self, term="202540", max_pages=None):
        """
        Get all courses by paginating through results
        
        Args:
            term: Academic term
            max_pages: Maximum number of pages to fetch (None for all)
            
        Returns:
            list: List of all course dictionaries
        """
        all_courses = []
        page_offset = 0  # Start at position 0 (courses 0-49)
        page_size = 50   # Get 50 courses at a time
        total_count = None
        
        while True:
            print(f"\n--- Fetching courses {page_offset}-{page_offset + page_size - 1} ---")
            
            response = self.search_courses(
                term=term,
                page_offset=page_offset,
                page_max_size=page_size
            )
            
            if not response or not response.get('success'):
                print("No data received or request failed, stopping pagination")
                break
                
            # Get total count from first response
            if total_count is None:
                total_count = response.get('totalCount', 0)
                print(f"Total courses available: {total_count}")
                
            courses = response.get('data', [])
            if not courses:
                print("No more courses found, stopping pagination")
                break
                
            all_courses.extend(courses)
            print(f"Got {len(courses)} courses, total: {len(all_courses)}/{total_count}")
            
            # Check if we've reached the end or max pages
            if len(courses) < page_size or len(all_courses) >= total_count:
                print("Reached end of results")
                break
                
            if max_pages and (page_offset // page_size + 1) >= max_pages:
                print(f"Reached maximum pages limit: {max_pages}")
                break
                
            # Move to next batch: 0 -> 50 -> 100 -> 150, etc.
            page_offset += page_size
            time.sleep(1)  # Be respectful to the server
            
        return all_courses

    def parse_course_basic_info(self, course):
        """Extract basic course information"""
        return {
            'id': course.get('id'),
            'crn': course.get('courseReferenceNumber'),
            'subject': course.get('subject'),
            'course_number': course.get('courseNumber'),
            'full_course': course.get('subjectCourse'),
            'title': course.get('courseTitle'),
            'subject_description': course.get('subjectDescription'),
            'credits': course.get('creditHourLow'),
            'term': course.get('termDesc'),
            'part_of_term': course.get('partOfTerm'),
            'sequence': course.get('sequenceNumber'),
            'campus': course.get('campusDescription'),
            'schedule_type': course.get('scheduleTypeDescription'),
            'instructional_method': course.get('instructionalMethodDescription')
        }

    def parse_enrollment_info(self, course):
        """Extract enrollment information"""
        return {
            'max_enrollment': course.get('maximumEnrollment'),
            'current_enrollment': course.get('enrollment'),
            'seats_available': course.get('seatsAvailable'),
            'wait_capacity': course.get('waitCapacity'),
            'wait_count': course.get('waitCount'),
            'wait_available': course.get('waitAvailable'),
            'is_open': course.get('openSection', False)
        }

    def parse_faculty_info(self, course):
        """Extract faculty information"""
        faculty_list = []
        for faculty in course.get('faculty', []):
            faculty_info = {
                'name': faculty.get('displayName'),
                'email': faculty.get('emailAddress'),
                'is_primary': faculty.get('primaryIndicator', False),
                'banner_id': faculty.get('bannerId')
            }
            faculty_list.append(faculty_info)
        return faculty_list

    def parse_meeting_times(self, course):
        """Extract meeting times and locations"""
        meetings = []
        for meeting_faculty in course.get('meetingsFaculty', []):
            meeting_time = meeting_faculty.get('meetingTime', {})
            if meeting_time:
                # Parse days of week
                days = []
                day_mapping = {
                    'monday': 'M', 'tuesday': 'T', 'wednesday': 'W', 
                    'thursday': 'R', 'friday': 'F', 'saturday': 'S', 'sunday': 'U'
                }
                for day, abbrev in day_mapping.items():
                    if meeting_time.get(day, False):
                        days.append(abbrev)
                
                # Format times
                begin_time = meeting_time.get('beginTime', '')
                end_time = meeting_time.get('endTime', '')
                
                def format_time(time_str):
                    if len(time_str) == 4:
                        return f"{time_str[:2]}:{time_str[2:]}"
                    return time_str
                
                meeting_info = {
                    'days': ''.join(days),
                    'start_time': format_time(begin_time),
                    'end_time': format_time(end_time),
                    'building': meeting_time.get('buildingDescription'),
                    'building_code': meeting_time.get('building'),
                    'room': meeting_time.get('room'),
                    'campus': meeting_time.get('campusDescription'),
                    'start_date': meeting_time.get('startDate'),
                    'end_date': meeting_time.get('endDate'),
                    'meeting_type': meeting_time.get('meetingTypeDescription'),
                    'credit_hours': meeting_time.get('creditHourSession'),
                    'hours_per_week': meeting_time.get('hoursWeek')
                }
                meetings.append(meeting_info)
        return meetings

    def get_course_summary(self, course):
        """Get a complete summary of a course"""
        return {
            'basic_info': self.parse_course_basic_info(course),
            'enrollment': self.parse_enrollment_info(course),
            'faculty': self.parse_faculty_info(course),
            'meetings': self.parse_meeting_times(course),
            'raw_data': course  # Include raw data for reference
        }

    def filter_courses(self, courses, **filters):
        """
        Filter courses based on various criteria
        
        Available filters:
        - subject: Course subject (e.g., 'ACCT', 'MATH')
        - course_number: Course number (e.g., '201', '101')
        - open_only: Show only open sections (True/False)
        - credits: Number of credits
        - building: Building name or code
        - days: Days of week (e.g., 'TR', 'MWF')
        - instructor: Instructor name (partial match)
        """
        filtered = courses.copy()
        
        if filters.get('subject'):
            filtered = [c for c in filtered if c.get('subject') == filters['subject']]
            
        if filters.get('course_number'):
            filtered = [c for c in filtered if c.get('courseNumber') == str(filters['course_number'])]
            
        if filters.get('open_only'):
            filtered = [c for c in filtered if c.get('openSection', False)]
            
        if filters.get('credits'):
            filtered = [c for c in filtered if c.get('creditHourLow') == filters['credits']]
            
        if filters.get('building'):
            building_filter = filters['building'].upper()
            filtered = [c for c in filtered 
                       if any(building_filter in meeting.get('meetingTime', {}).get('building', '').upper() or
                             building_filter in meeting.get('meetingTime', {}).get('buildingDescription', '').upper()
                             for meeting in c.get('meetingsFaculty', []))]
        
        if filters.get('days'):
            days_filter = set(filters['days'].upper())
            filtered = [c for c in filtered 
                       if any(self._check_days_match(meeting.get('meetingTime', {}), days_filter)
                             for meeting in c.get('meetingsFaculty', []))]
        
        if filters.get('instructor'):
            instructor_filter = filters['instructor'].lower()
            filtered = [c for c in filtered 
                       if any(instructor_filter in faculty.get('displayName', '').lower()
                             for faculty in c.get('faculty', []))]
        
        return filtered

    def _check_days_match(self, meeting_time, target_days):
        """Helper function to check if meeting days match filter"""
        meeting_days = set()
        day_mapping = {
            'monday': 'M', 'tuesday': 'T', 'wednesday': 'W', 
            'thursday': 'R', 'friday': 'F', 'saturday': 'S', 'sunday': 'U'
        }
        for day, abbrev in day_mapping.items():
            if meeting_time.get(day, False):
                meeting_days.add(abbrev)
        return target_days.issubset(meeting_days)

    def save_courses_to_file(self, courses, filename):
        """Save courses to a JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(courses, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved {len(courses)} courses to {filename}")
        except Exception as e:
            print(f"✗ Error saving to file: {e}")

    def update_auth(self, new_jsessionid, new_sync_token, new_session_id=None):
        """
        Update authentication credentials when they expire
        """
        self.cookies["JSESSIONID"] = new_jsessionid
        self.headers["X-Synchronizer-Token"] = new_sync_token
        
        if new_session_id:
            # Update unique session ID for requests
            pass
            
        # Update session with new credentials
        self.session.headers.update(self.headers)
        self.session.cookies.update(self.cookies)
        print("✓ Authentication credentials updated")


# Example usage - TEST FIRST, then get all courses
if __name__ == "__main__":
    scraper = EllucianScraper()
    
    # Test with a single page first
    print("=== Testing single page request ===")
    result = scraper.search_courses(term="202540", page_max_size=5)
    
    if result and result.get('success'):
        courses = result.get('data', [])
        print(f"\n=== Found {len(courses)} courses ===")
        
        # Show detailed info for first course
        if courses:
            first_course = courses[0]
            print("\n=== Sample Course Details ===")
            summary = scraper.get_course_summary(first_course)
            
            basic = summary['basic_info']
            print(f"Course: {basic['subject']} {basic['course_number']} - {basic['title']}")
            print(f"CRN: {basic['crn']}")
            print(f"Credits: {basic['credits']}")
            print(f"Campus: {basic['campus']}")
            
            enrollment = summary['enrollment']
            print(f"Enrollment: {enrollment['current_enrollment']}/{enrollment['max_enrollment']}")
            print(f"Seats Available: {enrollment['seats_available']}")
            print(f"Open: {enrollment['is_open']}")
            
            faculty = summary['faculty']
            if faculty:
                print("Faculty:")
                for prof in faculty:
                    print(f"  - {prof['name']} ({prof['email']})")
            
            meetings = summary['meetings']
            if meetings:
                print("Meeting Times:")
                for meeting in meetings:
                    print(f"  - {meeting['days']} {meeting['start_time']}-{meeting['end_time']} in {meeting['building']} {meeting['room']}")
        
        # Ask if user wants to proceed with full scrape
        print(f"\n🎯 Ready to scrape all {result.get('totalCount')} courses?")
        choice = input("Type 'yes' to proceed with full scrape: ").lower().strip()
        
        if choice == 'yes':
            print("\n=== Getting ALL courses ===")
            print("⏳ This may take 5-10 minutes...")
            
            # GET ALL COURSES - This is the key line!
            all_courses = scraper.get_all_courses(term="202540", max_pages=None)
            
            print(f"\n✅ Total courses retrieved: {len(all_courses)}")
            
            # Save to file
            if all_courses:
                scraper.save_courses_to_file(all_courses, 'all_courses_202540.json')
                
                # Show some statistics
                print("\n=== Course Statistics ===")
                subjects = {}
                open_count = 0
                for course in all_courses:
                    subject = course.get('subject', 'Unknown')
                    subjects[subject] = subjects.get(subject, 0) + 1
                    if course.get('openSection'):
                        open_count += 1
                
                print(f"📚 Total courses: {len(all_courses)}")
                print(f"🟢 Open sections: {open_count}")
                print(f"🔴 Closed sections: {len(all_courses) - open_count}")
                print(f"🏫 Unique subjects: {len(subjects)}")
                print("\nTop 10 subjects:")
                for subject, count in sorted(subjects.items(), key=lambda x: x[1], reverse=True)[:10]:
                    print(f"  {subject}: {count} courses")
        else:
            print("👍 Okay, just testing for now!")
    
    else:
        print("❌ Initial test failed. Check your authentication credentials.")
        print("\nTroubleshooting tips:")
        print("1. Make sure you're logged into the website in your browser")
        print("2. Get fresh cookies and tokens from a new browser request")
        print("3. Update the JSESSIONID and X-Synchronizer-Token values")
        print("4. Check if the unique session ID needs to be updated")
        
        if result:
            print(f"Response received but success={result.get('success')}")
            print("Response keys:", list(result.keys()))
