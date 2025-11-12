"""
MAI 5201 - Homework 0: Autograder
Part 1: Regular Expressions Testing

This autograder tests student implementations of regex functions.
Run with: python autograder.py
"""

import sys
import re
import traceback
from typing import List, Tuple, Any

# Import student solutions
try:
    from regex_exercises import *
    from tokenization import *
except ImportError as e:
    print(f"Error importing student code: {e}")
    print("Make sure regex_exercises.py and tokenization.py are in the same directory.")
    sys.exit(1)


class AutoGrader:
    def __init__(self):
        self.total_score = 0
        self.max_score = 0
        self.test_results = []

    def test_function(self, func_name: str, test_cases: List[Tuple], points: int) -> None:
        """Test a function with given test cases."""
        print(f"\n=== Testing {func_name} ({points} points) ===")
        
        try:
            func = globals()[func_name]
        except KeyError:
            print(f"❌ Function {func_name} not found!")
            self.test_results.append((func_name, 0, points, "Function not implemented"))
            self.max_score += points
            return

        passed = 0
        total = len(test_cases)
        errors = []

        for i, (args, expected) in enumerate(test_cases):
            try:
                if isinstance(args, tuple):
                    result = func(*args)
                else:
                    result = func(args)
                
                if self.compare_results(result, expected):
                    print(f"✅ Test case {i+1}: PASSED")
                    passed += 1
                else:
                    print(f"❌ Test case {i+1}: FAILED")
                    print(f"   Input: {args}")
                    print(f"   Expected: {expected}")
                    print(f"   Got: {result}")
                    errors.append(f"Test case {i+1}: Expected {expected}, got {result}")
                    
            except Exception as e:
                print(f"❌ Test case {i+1}: ERROR - {str(e)}")
                errors.append(f"Test case {i+1}: Exception - {str(e)}")

        score = int((passed / total) * points) if total > 0 else 0
        self.total_score += score
        self.max_score += points
        
        print(f"Score: {score}/{points} ({passed}/{total} test cases passed)")
        self.test_results.append((func_name, score, points, errors))

    def compare_results(self, result: Any, expected: Any) -> bool:
        """Compare results, handling different types appropriately."""
        if isinstance(expected, list) and isinstance(result, list):
            # For lists of dictionaries, compare each dict separately
            if len(result) != len(expected):
                return False
            if result and isinstance(result[0], dict):
                # Sort by a consistent key for comparison
                try:
                    result_sorted = sorted(result, key=lambda x: str(x))
                    expected_sorted = sorted(expected, key=lambda x: str(x))
                    return result_sorted == expected_sorted
                except:
                    return result == expected
            else:
                # For lists of non-dict items, sort both to handle order differences
                return sorted(result) == sorted(expected)
        return result == expected

    def run_all_tests(self) -> None:
        """Run all test cases."""
        print("MAI 5201 - Homework 0 Autograder")
        print("=" * 50)

        # Q1: Email and URL Extraction (5 points)
        self.test_q1()
        
        # Q2: Phone Number Processing (5 points)
        self.test_q2()
        
        # Q3: Social Media Processing (5 points)
        self.test_q3()
        
        # Q4: Date and Time Extraction (5 points)
        self.test_q4()
        
        # Q5: Document Structure Extraction (5 points)
        self.test_q5()
        
        # Q6: Address Extraction (5 points)
        self.test_q6()
        
        # Q7: Log File Parsing (5 points)
        self.test_q7()
        
        # Q8: Basic Tokenization (5 points)
        self.test_q8()
        
        # Q9: Advanced Tokenization (5 points)
        self.test_q9()
        
        # Q10: Text Normalization (5 points)
        self.test_q10()
        
        # Q11: BPE Algorithm (10 points)
        self.test_q11()
        
        # Q12: Edit Distance Applications (10 points)
        self.test_q12()

        # Print final results
        self.print_final_results()

    def test_q1(self) -> None:
        """Test Q1: Email and URL extraction - Comprehensive test with 50+ cases each."""
        print(f"\n=== Q1: Email and URL Extraction (5 points) ===")
        
        # Test extract_emails - 50+ challenging cases
        email_test_cases = [
            # Basic valid emails
            ("Contact us at info@university.edu for more information.", ["info@university.edu"]),
            ("Email me at john.doe@gmail.com or admin@school.org", ["john.doe@gmail.com", "admin@school.org"]),
            ("My email is user+newsletter@company.co.uk", ["user+newsletter@company.co.uk"]),
            ("simple@test.com is basic", ["simple@test.com"]),
            ("Send to support@company.net today", ["support@company.net"]),
            
            # Emails with special characters
            ("Contact user.name+tag@company.co.uk", ["user.name+tag@company.co.uk"]),
            ("Email: first.last+newsletter@subdomain.example.org", ["first.last+newsletter@subdomain.example.org"]),
            ("Reach out to user_123@test-domain.com", ["user_123@test-domain.com"]),
            ("My email: name-with-dashes@company-name.co", ["name-with-dashes@company-name.co"]),
            ("Contact: user.with.dots@long-domain-name.example.org", ["user.with.dots@long-domain-name.example.org"]),
            
            # Numbers in emails
            ("Account: user123@domain456.com", ["user123@domain456.com"]),
            ("Contact support2023@company.org", ["support2023@company.org"]),
            ("Email: 123user@test123.net", ["123user@test123.net"]),
            ("Reach: test2024+special@example2025.edu", ["test2024+special@example2025.edu"]),
            ("Admin: admin99@subdomain99.example.com", ["admin99@subdomain99.example.com"]),
            
            # International domains
            ("Email me at user@domain.de for German support", ["user@domain.de"]),
            ("Contact: admin@company.fr for French", ["admin@company.fr"]),
            ("Reach out to support@business.jp", ["support@business.jp"]),
            ("Email: info@university.au for Australia", ["info@university.au"]),
            ("Contact user@website.ca for Canada", ["user@website.ca"]),
            
            # Long domain names
            ("Contact: user@very-long-domain-name.example.com", ["user@very-long-domain-name.example.com"]),
            ("Email: admin@subdomain.very-long-company-name.org", ["admin@subdomain.very-long-company-name.org"]),
            ("Reach: support@a.b.c.d.example.edu", ["support@a.b.c.d.example.edu"]),
            ("Contact: info@department.university.example.ac.uk", ["info@department.university.example.ac.uk"]),
            
            # Multiple emails in text
            ("Contacts: john@company.com, jane@company.com, admin@company.com", 
             ["john@company.com", "jane@company.com", "admin@company.com"]),
            ("Email list: user1@test.com user2@test.org user3@test.net", 
             ["user1@test.com", "user2@test.org", "user3@test.net"]),
            ("Reach: primary@company.com or backup@company.org", 
             ["primary@company.com", "backup@company.org"]),
            ("Contact info@main.com; support@help.com; sales@sales.com", 
             ["info@main.com", "support@help.com", "sales@sales.com"]),
            
            # Emails in different contexts
            ("Please email your resume to hr@company.com by Friday.", ["hr@company.com"]),
            ("The newsletter signup is at newsletter+signup@marketing.org", ["newsletter+signup@marketing.org"]),
            ("Report bugs to bugs.reports@software.company.net", ["bugs.reports@software.company.net"]),
            ("Customer service: help@customer-service.example.com", ["help@customer-service.example.com"]),
            ("Academic inquiry: research.inquiry@university.edu", ["research.inquiry@university.edu"]),
            
            # Mixed valid and invalid
            ("Valid: user@test.com, Invalid: notanemail@, Another valid: admin@company.org", 
             ["user@test.com", "admin@company.org"]),
            ("Contact user@domain.com but not @invalid.com", ["user@domain.com"]),
            ("Email test@example.org not test@.invalid", ["test@example.org"]),
            
            # Edge cases with punctuation
            ("Email (user@company.com) for more info", ["user@company.com"]),
            ("Contact: [admin@test.org] or call", ["admin@test.org"]),
            ("Email 'support@help.com' immediately", ["support@help.com"]),
            ("Reach out to \"info@company.net\" today", ["info@company.net"]),
            ("Email <user@domain.org> for details", ["user@domain.org"]),
            
            # Subdomain emails
            ("Contact: user@mail.company.com", ["user@mail.company.com"]),
            ("Email: admin@internal.corporate.org", ["admin@internal.corporate.org"]),
            ("Support: help@support.service.net", ["help@support.service.net"]),
            ("Reach: info@public.university.edu", ["info@public.university.edu"]),
            
            # Government and academic emails
            ("Official: contact@government.gov", ["contact@government.gov"]),
            ("Academic: professor@research.university.edu", ["professor@research.university.edu"]),
            ("Public: info@city.municipality.gov", ["info@city.municipality.gov"]),
            ("Research: data@science.institute.org", ["data@science.institute.org"]),
            
            # No emails
            ("No emails in this text!", []),
            ("This has no @ symbols or domains", []),
            ("Just some text without any contact information", []),
            ("Numbers 123 and text but no emails", []),
            ("Website www.example.com but no email", []),
            
            # Invalid emails that should be rejected
            ("Invalid email@.com and valid@test.edu", ["valid@test.edu"]),
            ("Bad: @domain.com, Good: user@domain.com", ["user@domain.com"]),
            ("Invalid: user@.com Valid: admin@test.org", ["admin@test.org"]),
            ("Wrong: email@ Right: test@domain.com", ["test@domain.com"]),
        ]
        
        passed_emails = 0
        total_emails = len(email_test_cases)
        positive_tests_passed = 0  # Tests with non-empty expected results
        total_positive_tests = 0
        
        try:
            extract_emails_func = globals()["extract_emails"]
            for i, (text, expected) in enumerate(email_test_cases):
                try:
                    result = extract_emails_func(text)
                    if expected:  # Count positive tests
                        total_positive_tests += 1
                        if self.compare_results(result, expected):
                            positive_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_emails += 1
                    elif i < 5:  # Show first few failures for debugging
                        print(f"❌ Email test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Email test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function extract_emails not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_tests_passed > 0:
            email_score = (passed_emails / total_emails) * 2.5
        else:
            email_score = 0.0
        print(f"Email extraction: {passed_emails}/{total_emails} passed ({email_score:.1f}/2.5 points)")

        # Test extract_urls - 50+ challenging cases
        url_test_cases = [
            # Basic URLs
            ("Visit https://www.uog.edu.gy for more info", ["https://www.uog.edu.gy"]),
            ("Check http://example.com for details", ["http://example.com"]),
            ("Go to https://test.org/path", ["https://test.org/path"]),
            ("Link: http://www.company.com", ["http://www.company.com"]),
            ("See https://university.edu", ["https://university.edu"]),
            
            # URLs with paths
            ("Visit https://example.com/about/contact", ["https://example.com/about/contact"]),
            ("Check http://site.org/blog/2025/article", ["http://site.org/blog/2025/article"]),
            ("Link: https://company.com/products/software", ["https://company.com/products/software"]),
            ("Go to http://university.edu/departments/computer-science", ["http://university.edu/departments/computer-science"]),
            ("See https://news.site.com/2025/07/25/breaking-news", ["https://news.site.com/2025/07/25/breaking-news"]),
            
            # URLs with query parameters
            ("Search: https://example.com/search?q=nlp&type=course", ["https://example.com/search?q=nlp&type=course"]),
            ("Link: http://site.org/page?id=123&action=view", ["http://site.org/page?id=123&action=view"]),
            ("URL: https://api.service.com/v1/data?format=json&limit=100", ["https://api.service.com/v1/data?format=json&limit=100"]),
            ("Check: http://example.com/?utm_source=email&utm_campaign=newsletter", 
             ["http://example.com/?utm_source=email&utm_campaign=newsletter"]),
            ("Visit: https://shop.com/products?category=electronics&sort=price&page=2", 
             ["https://shop.com/products?category=electronics&sort=price&page=2"]),
            
            # URLs with fragments
            ("Go to https://docs.example.com/guide#section-1", ["https://docs.example.com/guide#section-1"]),
            ("See http://tutorial.org/lesson?id=5#step-3", ["http://tutorial.org/lesson?id=5#step-3"]),
            ("Link: https://article.com/story#conclusion", ["https://article.com/story#conclusion"]),
            ("Check: http://reference.org/manual#chapter-2-advanced", ["http://reference.org/manual#chapter-2-advanced"]),
            
            # Different protocols
            ("FTP: ftp://files.example.com/data.txt", ["ftp://files.example.com/data.txt"]),
            ("Secure FTP: ftps://secure.files.org/documents", ["ftps://secure.files.org/documents"]),
            ("File: file://localhost/path/to/file.html", ["file://localhost/path/to/file.html"]),
            ("Download: ftp://download.site.com/software/program.zip", ["ftp://download.site.com/software/program.zip"]),
            
            # URLs with ports
            ("Local: http://localhost:8080/app", ["http://localhost:8080/app"]),
            ("Dev server: https://dev.company.com:3000/dashboard", ["https://dev.company.com:3000/dashboard"]),
            ("API: http://api.service.org:8080/v2/endpoint", ["http://api.service.org:8080/v2/endpoint"]),
            ("Testing: https://test.example.com:4433/secure", ["https://test.example.com:4433/secure"]),
            
            # IP address URLs
            ("Server: http://192.168.1.100/admin", ["http://192.168.1.100/admin"]),
            ("Local: https://127.0.0.1:8080/app", ["https://127.0.0.1:8080/app"]),
            ("Internal: http://10.0.0.1/dashboard", ["http://10.0.0.1/dashboard"]),
            ("Network: https://172.16.0.1:443/portal", ["https://172.16.0.1:443/portal"]),
            
            # Multiple URLs
            ("Links: http://first.com and https://second.org", ["http://first.com", "https://second.org"]),
            ("Check http://example.com, https://test.org, and http://demo.net", 
             ["http://example.com", "https://test.org", "http://demo.net"]),
            ("Sites: https://news.com; http://sports.org; https://weather.net", 
             ["https://news.com", "http://sports.org", "https://weather.net"]),
            ("Visit: http://site1.com, http://site2.org, http://site3.net", 
             ["http://site1.com", "http://site2.org", "http://site3.net"]),
            
            # URLs in different contexts
            ("Click here: https://signup.service.com/register", ["https://signup.service.com/register"]),
            ("Documentation at https://docs.api.org/v2/reference", ["https://docs.api.org/v2/reference"]),
            ("Download from http://releases.software.com/latest/", ["http://releases.software.com/latest/"]),
            ("API endpoint: https://api.data.gov/v1/datasets", ["https://api.data.gov/v1/datasets"]),
            
            # URLs with special characters in paths
            ("Link: https://example.com/path-with-dashes", ["https://example.com/path-with-dashes"]),
            ("URL: http://site.org/path_with_underscores", ["http://site.org/path_with_underscores"]),
            ("Visit: https://company.com/products/item-123", ["https://company.com/products/item-123"]),
            ("Check: http://blog.site.net/2025-07-25/article", ["http://blog.site.net/2025-07-25/article"]),
            
            # International domains
            ("German: https://website.de/information", ["https://website.de/information"]),
            ("French: http://site.fr/accueil", ["http://site.fr/accueil"]),
            ("Japanese: https://company.jp/products", ["https://company.jp/products"]),
            ("UK: http://university.ac.uk/courses", ["http://university.ac.uk/courses"]),
            ("Australian: https://business.com.au/services", ["https://business.com.au/services"]),
            
            # Subdomains
            ("Mail: https://mail.company.com/inbox", ["https://mail.company.com/inbox"]),
            ("Support: http://support.service.org/tickets", ["http://support.service.org/tickets"]),
            ("Wiki: https://wiki.project.net/documentation", ["https://wiki.project.net/documentation"]),
            ("API: http://api.v2.service.com/endpoints", ["http://api.v2.service.com/endpoints"]),
            
            # URLs with encoded characters
            ("Search: https://example.com/search?q=machine%20learning", ["https://example.com/search?q=machine%20learning"]),
            ("Link: http://site.org/path%20with%20spaces", ["http://site.org/path%20with%20spaces"]),
            ("URL: https://api.com/data?filter=%7B%22type%22%3A%22json%22%7D", 
             ["https://api.com/data?filter=%7B%22type%22%3A%22json%22%7D"]),
            
            # URLs in parentheses and brackets
            ("Visit (https://example.com) for details", ["https://example.com"]),
            ("Check [http://reference.org] for info", ["http://reference.org"]),
            ("Link: <https://tutorial.net>", ["https://tutorial.net"]),
            ("See {http://docs.site.com} for documentation", ["http://docs.site.com"]),
            
            # Long URLs
            ("Complex: https://very-long-domain-name.example.com/very/long/path/to/resource?param1=value1&param2=value2&param3=value3", 
             ["https://very-long-domain-name.example.com/very/long/path/to/resource?param1=value1&param2=value2&param3=value3"]),
            
            # No URLs
            ("No URLs in this text!", []),
            ("Just some text without links", []),
            ("Email: user@domain.com but no website", []),
            ("Phone: 123-456-7890 but no URL", []),
            ("www.example.com without protocol should not match", []),
        ]
        
        passed_urls = 0
        total_urls = len(url_test_cases)
        positive_url_tests_passed = 0  # Tests with non-empty expected results
        total_positive_url_tests = 0
        
        try:
            extract_urls_func = globals()["extract_urls"]
            failing_cases = []
            for i, (text, expected) in enumerate(url_test_cases):
                try:
                    result = extract_urls_func(text)
                    if expected:  # Count positive tests
                        total_positive_url_tests += 1
                        if self.compare_results(result, expected):
                            positive_url_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_urls += 1
                    else:
                        failing_cases.append((i+1, text, expected, result))
                        
                except Exception as e:
                    failing_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
            
            # Print all failing cases
            if failing_cases:
                print(f"\n❌ FAILING URL TEST CASES ({len(failing_cases)} total):")
                for test_num, text, expected, result in failing_cases:
                    print(f"  Test {test_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got: {result}")
                    print()
                    
        except KeyError:
            print("❌ Function extract_urls not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_url_tests_passed > 0:
            url_score = (passed_urls / total_urls) * 2.5
        else:
            url_score = 0.0
        print(f"URL extraction: {passed_urls}/{total_urls} passed ({url_score:.1f}/2.5 points)")
        
        total_score = email_score + url_score
        self.total_score += total_score
        self.max_score += 5
        print(f"Q1 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q1", total_score, 5, [f"Emails: {passed_emails}/{total_emails}, URLs: {passed_urls}/{total_urls}"]))

    def test_q2(self) -> None:
        """Test Q2: Phone number processing - Simplified educational test cases."""
        print(f"\n=== Q2: Phone Number Processing (5 points) ===")
        
        # Test extract_phone_numbers - Simplified, teachable cases
        phone_extract_cases = [
            # Standard US formats
            ("Call (800) 123-4567 today", ["(800) 123-4567"]),
            ("Number: (555) 555-0123", ["(555) 555-0123"]),
            ("Contact (456) 789-0123 for support", ["(456) 789-0123"]),
            ("Office: (212) 555-1234", ["(212) 555-1234"]),
            
            # Dot-separated formats
            ("Contact: 456.789.0123", ["456.789.0123"]),
            ("Phone: 212.555.1234", ["212.555.1234"]),
            ("Numbers: 800.555.0123 and 555.123.4567", ["800.555.0123", "555.123.4567"]),
            
            # Dash-separated formats
            ("Phone: 456-789-0123", ["456-789-0123"]),
            ("Call 212-555-1234", ["212-555-1234"]),
            ("Contact: 800-555-0123", ["800-555-0123"]),
            
            # Basic international formats (simplified)
            ("International: +1-800-555-0123", ["+1-800-555-0123"]),
            ("Call +44-20-7946-0958", ["+44-20-7946-0958"]),
            ("Number: +33-1-42-86-83-26", ["+33-1-42-86-83-26"]),
            
            # Space-separated international (simplified)
            ("Call +1 800 555 0123", ["+1 800 555 0123"]),
            ("Number: +44 20 7946 0958", ["+44 20 7946 0958"]),
            
            # Mixed formatting in text
            ("Call (800) 123-4567 or 555.555.0123", ["(800) 123-4567", "555.555.0123"]),
            ("Numbers: 456-789-0123, (212) 555-1234", ["456-789-0123", "(212) 555-1234"]),
            
            # Toll-free numbers with letters
            ("Call 1-800-FLOWERS", ["1-800-FLOWERS"]),
            ("Number: 1-888-GO-FEDEX", ["1-888-GO-FEDEX"]),
            ("Contact 800-CALL-ATT", ["800-CALL-ATT"]),
            
            # No phone numbers
            ("No phone numbers here!", []),
            ("Email: user@domain.com but no phone", []),
            ("Just text without any contact information", []),
            
            # Edge cases (simplified)
            ("Call 800-555-1234 immediately!", ["800-555-1234"]),
            ("Phone number: (800) 555-1234.", ["(800) 555-1234"]),
            ("Contact 'support': 555-123-4567", ["555-123-4567"]),
        ]
        
        passed_extract = 0
        total_extract = len(phone_extract_cases)
        
        try:
            extract_phone_func = globals()["extract_phone_numbers"]
            failing_extract_cases = []
            for i, (text, expected) in enumerate(phone_extract_cases):
                try:
                    result = extract_phone_func(text)
                    if self.compare_results(result, expected):
                        passed_extract += 1
                    else:
                        failing_extract_cases.append((i+1, text, expected, result))
                        
                except Exception as e:
                    failing_extract_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
            
            # Print failing phone extraction cases
            if failing_extract_cases:
                print(f"\n❌ FAILING PHONE EXTRACTION TEST CASES ({len(failing_extract_cases)} total):")
                for test_num, text, expected, result in failing_extract_cases[:10]:
                    print(f"  Test {test_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got: {result}")
                    print()
                if len(failing_extract_cases) > 10:
                    print(f"  ... and {len(failing_extract_cases) - 10} more failing cases")
                    
        except KeyError:
            print("❌ Function extract_phone_numbers not found!")
        
        extract_score = (passed_extract / total_extract) * 2.5
        print(f"Phone extraction: {passed_extract}/{total_extract} passed ({extract_score:.1f}/2.5 points)")

        # Test normalize_phone_number - Simplified, teachable cases
        phone_normalize_cases = [
            # Basic US normalization
            ("(800) 123-4567", "+1-800-123-4567"),
            ("800.123.4567", "+1-800-123-4567"),
            ("800-123-4567", "+1-800-123-4567"),
            ("8001234567", "+1-800-123-4567"),
            
            # Different area codes
            ("(555) 555-1234", "+1-555-555-1234"),
            ("456.789.0123", "+1-456-789-0123"),
            ("212-555-1234", "+1-212-555-1234"),
            
            # International numbers (simplified)
            ("+1 800 555 0123", "+1-800-555-0123"),
            ("+44 20 7946 0958", "+44-20-7946-0958"),
            ("+33 1 42 86 83 26", "+33-1-42-86-83-26"),
            
            # Already formatted international
            ("+1-800-555-0123", "+1-800-555-0123"),
            ("+44-20-7946-0958", "+44-20-7946-0958"),
            ("+33-1-42-86-83-26", "+33-1-42-86-83-26"),
            
            # Numbers with leading 1
            ("1-800-555-1234", "+1-800-555-1234"),
            ("1.800.555.1234", "+1-800-555-1234"),
            ("1 800 555 1234", "+1-800-555-1234"),
            ("18005551234", "+1-800-555-1234"),
            
            # Toll-free number formats
            ("1-800-FLOWERS", "+1-800-FLOWERS"),
            ("800-GO-FEDEX", "+1-800-GO-FEDEX"),
            ("1-888-CALL-ATT", "+1-888-CALL-ATT"),
            
            # With extensions (should ignore extension)
            ("(800) 555-1234 ext 123", "+1-800-555-1234"),
            ("555-123-4567 x456", "+1-555-123-4567"),
            ("800.555.1234 extension 789", "+1-800-555-1234"),
            
            # With extra formatting
            ("  (800) 555-1234  ", "+1-800-555-1234"),
            ("[(555) 789-0123]", "+1-555-789-0123"),
            ("\"800.555.1234\"", "+1-800-555-1234"),
        ]
        
        passed_normalize = 0
        total_normalize = len(phone_normalize_cases)
        
        try:
            normalize_phone_func = globals()["normalize_phone_number"]
            failing_normalize_cases = []
            for i, (input_phone, expected) in enumerate(phone_normalize_cases):
                try:
                    result = normalize_phone_func(input_phone)
                    if result == expected:
                        passed_normalize += 1
                    else:
                        failing_normalize_cases.append((i+1, input_phone, expected, result))
                        
                except Exception as e:
                    failing_normalize_cases.append((i+1, input_phone, expected, f"Exception: {str(e)}"))
            
            # Print failing phone normalization cases
            if failing_normalize_cases:
                print(f"\n❌ FAILING PHONE NORMALIZATION TEST CASES ({len(failing_normalize_cases)} total):")
                for test_num, input_phone, expected, result in failing_normalize_cases[:10]:
                    print(f"  Test {test_num}: '{input_phone}'")
                    print(f"    Expected: '{expected}'")
                    print(f"    Got: '{result}'")
                    print()
                if len(failing_normalize_cases) > 10:
                    print(f"  ... and {len(failing_normalize_cases) - 10} more failing cases")
                    
        except KeyError:
            print("❌ Function normalize_phone_number not found!")
        
        normalize_score = (passed_normalize / total_normalize) * 2.5
        print(f"Phone normalization: {passed_normalize}/{total_normalize} passed ({normalize_score:.1f}/2.5 points)")
        
        total_score = extract_score + normalize_score
        self.total_score += total_score
        self.max_score += 5
        print(f"Q2 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q2", total_score, 5, [f"Extract: {passed_extract}/{total_extract}, Normalize: {passed_normalize}/{total_normalize}"]))

    def test_q3(self) -> None:
        """Test Q3: Social media processing - Comprehensive test with 50+ cases each."""
        print(f"\n=== Q3: Social Media Processing (5 points) ===")
        
        # Test extract_hashtags - 50+ challenging cases
        hashtag_cases = [
            # Basic hashtags
            ("Great day! #university #education", ["university", "education"]),
            ("Learning #MachineLearning today", ["MachineLearning"]),
            ("Check out #AI #ML #NLP", ["AI", "ML", "NLP"]),
            ("Post about #coding and #programming", ["coding", "programming"]),
            ("Excited about #DataScience", ["DataScience"]),
            
            # Hashtags with underscores
            ("Learning #machine_learning and #deep_learning", ["machine_learning", "deep_learning"]),
            ("Topics: #natural_language_processing #computer_vision", ["natural_language_processing", "computer_vision"]),
            ("Studying #data_science and #web_development", ["data_science", "web_development"]),
            ("Working on #software_engineering projects", ["software_engineering"]),
            ("Interested in #cyber_security", ["cyber_security"]),
            
            # Hashtags with numbers
            ("Event #2025conference starting soon", ["2025conference"]),
            ("Learning #Python3 and #JavaScript", ["Python3", "JavaScript"]),
            ("Topics: #AI2025 #ML2024", ["AI2025", "ML2024"]),
            ("Course #CS101 #MATH250", ["CS101", "MATH250"]),
            ("Version #v2024 #update2025", ["v2024", "update2025"]),
            
            # Mixed case hashtags
            ("Studying #MachineLearning #DeepLearning #NeuralNetworks", 
             ["MachineLearning", "DeepLearning", "NeuralNetworks"]),
            ("Topics: #DataScience #BigData #CloudComputing", 
             ["DataScience", "BigData", "CloudComputing"]),
            ("Learning #WebDevelopment #MobileDev #GameDev", 
             ["WebDevelopment", "MobileDev", "GameDev"]),
            ("Working on #SoftwareEngineering #DevOps", 
             ["SoftwareEngineering", "DevOps"]),
            
            # Long hashtags
            ("Conference #NaturalLanguageProcessingConference2025", ["NaturalLanguageProcessingConference2025"]),
            ("Event #InternationalArtificialIntelligenceSymposium", ["InternationalArtificialIntelligenceSymposium"]),
            ("Workshop #MachineLearningAndDataScienceWorkshop", ["MachineLearningAndDataScienceWorkshop"]),
            ("Seminar #AdvancedComputerVisionTechniques", ["AdvancedComputerVisionTechniques"]),
            
            # Hashtags with special contexts
            ("Amazing lecture! #university #education #learning", ["university", "education", "learning"]),
            ("Conference day 1: #AI #research #innovation", ["AI", "research", "innovation"]),
            ("Workshop topics: #coding #algorithms #datastructures", ["coding", "algorithms", "datastructures"]),
            ("Study session: #mathematics #statistics #probability", ["mathematics", "statistics", "probability"]),
            ("Project work: #python #javascript #html #css", ["python", "javascript", "html", "css"]),
            
            # Multiple hashtags in different parts of text
            ("Starting with #morning routine, then #work, ending with #exercise", 
             ["morning", "work", "exercise"]),
            ("Topics covered: #introduction #basics #advanced #expert", 
             ["introduction", "basics", "advanced", "expert"]),
            ("Languages: #english #spanish #french #german", 
             ["english", "spanish", "french", "german"]),
            ("Subjects: #math #science #history #literature", 
             ["math", "science", "history", "literature"]),
            
            # Hashtags with punctuation around them
            ("Great! #amazing, #wonderful, #fantastic!", ["amazing", "wonderful", "fantastic"]),
            ("Topics: #AI; #ML; #DL;", ["AI", "ML", "DL"]),
            ("Learning (#programming) #coding", ["programming", "coding"]),
            ("Study #math, #science.", ["math", "science"]),
            ("Work on #project1 and #project2!", ["project1", "project2"]),
            
            # Hashtags at different positions
            ("#StartOfPost with content in middle #MiddleTag and end #EndTag", 
             ["StartOfPost", "MiddleTag", "EndTag"]),
            ("Content before #tag1 more content #tag2 final content", ["tag1", "tag2"]),
            ("#First #Second content #Third #Fourth", ["First", "Second", "Third", "Fourth"]),
            
            # Technology hashtags
            ("Learning #Python #Java #JavaScript #C++ #Go", ["Python", "Java", "JavaScript", "C", "Go"]),
            ("Frameworks: #React #Angular #Vue #Django #Flask", ["React", "Angular", "Vue", "Django", "Flask"]),
            ("Databases: #MySQL #PostgreSQL #MongoDB #Redis", ["MySQL", "PostgreSQL", "MongoDB", "Redis"]),
            ("Tools: #Git #Docker #Kubernetes #Jenkins", ["Git", "Docker", "Kubernetes", "Jenkins"]),
            ("Cloud: #AWS #Azure #GCP #DigitalOcean", ["AWS", "Azure", "GCP", "DigitalOcean"]),
            
            # Academic hashtags
            ("Courses: #CS101 #MATH201 #PHYS150 #CHEM120", ["CS101", "MATH201", "PHYS150", "CHEM120"]),
            ("Degrees: #ComputerScience #Mathematics #Physics #Engineering", 
             ["ComputerScience", "Mathematics", "Physics", "Engineering"]),
            ("Research: #thesis #dissertation #publication #conference", 
             ["thesis", "dissertation", "publication", "conference"]),
            ("Academic: #student #professor #researcher #scholar", 
             ["student", "professor", "researcher", "scholar"]),
            
            # Event hashtags
            ("Conference #NIPS2025 #ICML2025 #ICLR2025", ["NIPS2025", "ICML2025", "ICLR2025"]),
            ("Events: #workshop #seminar #symposium #summit", ["workshop", "seminar", "symposium", "summit"]),
            ("Competitions: #hackathon #datathon #coding_contest", ["hackathon", "datathon", "coding_contest"]),
            ("Meetings: #standup #retrospective #planning #review", 
             ["standup", "retrospective", "planning", "review"]),
            
            # Hashtags with repeated words (should extract each occurrence)
            ("Daily routine: #work #study #work #exercise #study", 
             ["work", "study", "work", "exercise", "study"]),
            ("Multiple #test #test #different #test", ["test", "test", "different", "test"]),
            
            # No hashtags
            ("No hashtags in this text!", []),
            ("Just regular text without any social media tags", []),
            ("Mentions @user but no hashtags", []),
            ("Email user@domain.com but no #hashtags", []),
            ("Regular text with # but not #hashtag", []),
            
            # Invalid hashtags (should be rejected)
            ("Invalid: # (just hash) Valid: #realtag", ["realtag"]),
            ("Wrong: #123 (only numbers) Right: #tag123", ["tag123"]),
            ("Bad: #spaces not allowed Good: #notag", ["notag"]),
        ]
        
        passed_hashtags = 0
        total_hashtags = len(hashtag_cases)
        positive_hashtags_tests_passed = 0
        total_positive_hashtags_tests = 0
        
        try:
            extract_hashtags_func = globals()["extract_hashtags"]
            failing_hashtag_cases = []
            for i, (text, expected) in enumerate(hashtag_cases):
                try:
                    result = extract_hashtags_func(text)
                    if expected:  # Count positive tests
                        total_positive_hashtags_tests += 1
                        if self.compare_results(result, expected):
                            positive_hashtags_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_hashtags += 1
                    else:
                        failing_hashtag_cases.append((i+1, text, expected, result))
                        
                except Exception as e:
                    failing_hashtag_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
            
            # Print failing hashtag cases
            if failing_hashtag_cases:
                print(f"\n❌ FAILING HASHTAG TEST CASES ({len(failing_hashtag_cases)} total):")
                for test_num, text, expected, result in failing_hashtag_cases[:5]:
                    print(f"  Test {test_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got: {result}")
                    print()
                if len(failing_hashtag_cases) > 5:
                    print(f"  ... and {len(failing_hashtag_cases) - 5} more failing cases")
                    
        except KeyError:
            print("❌ Function extract_hashtags not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_hashtags_tests_passed > 0:
            hashtag_score = (passed_hashtags / total_hashtags) * 1.5
        else:
            hashtag_score = 0.0
        print(f"Hashtag extraction: {passed_hashtags}/{total_hashtags} passed ({hashtag_score:.1f}/1.5 points)")

        # Test extract_mentions - 50+ challenging cases
        mention_cases = [
            # Basic mentions
            ("Thanks @UofG for the lecture!", ["UofG"]),
            ("Shoutout to @user_123", ["user_123"]),
            ("Hello @DrClarke", ["DrClarke"]),
            ("Contact @admin for help", ["admin"]),
            ("Follow @updates for news", ["updates"]),
            
            # Mentions with underscores
            ("Thanks @user_name and @another_user", ["user_name", "another_user"]),
            ("Contact @tech_support for help", ["tech_support"]),
            ("Follow @data_science_news", ["data_science_news"]),
            ("Message @customer_service", ["customer_service"]),
            ("Reach @system_admin", ["system_admin"]),
            
            # Mentions with numbers
            ("Contact @user123 and @admin456", ["user123", "admin456"]),
            ("Follow @update2025 for news", ["update2025"]),
            ("Thanks @team1 @team2 @team3", ["team1", "team2", "team3"]),
            ("Message @support24x7", ["support24x7"]),
            ("Reach @service365", ["service365"]),
            
            # Mentions with dashes
            ("Thanks @user-name and @co-worker", ["user-name", "co-worker"]),
            ("Contact @tech-support", ["tech-support"]),
            ("Follow @data-science", ["data-science"]),
            ("Message @customer-care", ["customer-care"]),
            ("Reach @system-admin", ["system-admin"]),
            
            # Mixed format mentions
            ("Team: @user_123 @admin-456 @service789", ["user_123", "admin-456", "service789"]),
            ("Contacts: @tech_support @user-name @admin123", ["tech_support", "user-name", "admin123"]),
            ("Follow: @news_updates @data-science @ml2025", ["news_updates", "data-science", "ml2025"]),
            ("Thanks: @professor @student_123 @ta-assistant", ["professor", "student_123", "ta-assistant"]),
            
            # Multiple mentions in context
            ("Great presentation by @DrSmith and @ProfJones", ["DrSmith", "ProfJones"]),
            ("Team members: @alice @bob @charlie @diana", ["alice", "bob", "charlie", "diana"]),
            ("Contributors: @dev1 @dev2 @tester1 @designer", ["dev1", "dev2", "tester1", "designer"]),
            ("Speakers: @keynote @workshop1 @workshop2", ["keynote", "workshop1", "workshop2"]),
            
            # Mentions with different contexts
            ("Question for @instructor about homework", ["instructor"]),
            ("Congratulations @graduate on your achievement!", ["graduate"]),
            ("Welcome @new_student to our program", ["new_student"]),
            ("Thanks @librarian for the resources", ["librarian"]),
            ("Shoutout to @researcher for the insights", ["researcher"]),
            
            # Academic mentions
            ("Professor @DrBrown will lecture today", ["DrBrown"]),
            ("TA @assistant will hold office hours", ["assistant"]),
            ("Guest speaker @industry_expert", ["industry_expert"]),
            ("Research group @ai_lab meeting", ["ai_lab"]),
            ("Department @computer_science announcement", ["computer_science"]),
            
            # Organization mentions
            ("Official announcement from @university", ["university"]),
            ("Event by @student_union", ["student_union"]),
            ("Workshop by @tech_club", ["tech_club"]),
            ("Seminar by @research_center", ["research_center"]),
            ("Conference by @ai_society", ["ai_society"]),
            
            # Mentions with punctuation around them
            ("Thanks (@user123) for help", ["user123"]),
            ("Contact @support, they'll help", ["support"]),
            ("Message @admin; urgent issue", ["admin"]),
            ("Follow @updates!", ["updates"]),
            ("Reach @help.", ["help"]),
            
            # Mentions at different positions
            ("@StartMention with content in middle @MiddleMention and end @EndMention", 
             ["StartMention", "MiddleMention", "EndMention"]),
            ("Content before @mention1 more content @mention2 final content", ["mention1", "mention2"]),
            ("@First @Second content @Third @Fourth", ["First", "Second", "Third", "Fourth"]),
            
            # Social media style mentions
            ("Twitter style @username mention", ["username"]),
            ("Instagram @photographer captured this", ["photographer"]),
            ("LinkedIn @professional networking", ["professional"]),
            ("GitHub @developer pushed code", ["developer"]),
            ("Discord @moderator online", ["moderator"]),
            
            # Case variations
            ("Thanks @User and @USER and @user", ["User", "USER", "user"]),
            ("Contact @Admin @ADMIN @admin", ["Admin", "ADMIN", "admin"]),
            ("Follow @NEWS @News @news", ["NEWS", "News", "news"]),
            
            # Long mentions
            ("Contact @very_long_username_here", ["very_long_username_here"]),
            ("Thanks @extremely_long_user_name_with_underscores", ["extremely_long_user_name_with_underscores"]),
            ("Follow @super-long-hyphenated-username", ["super-long-hyphenated-username"]),
            ("Message @combination_of-different_separators123", ["combination_of-different_separators123"]),
            
            # No mentions
            ("No mentions in this text!", []),
            ("Just regular text without any @ symbols", []),
            ("Email user@domain.com but no mentions", []),
            ("Hashtag #tag but no @mentions", []),
            ("Regular @ symbol but not @mention", []),
            
            # Invalid mentions (should be rejected)
            ("Invalid: @ (just at) Valid: @realuser", ["realuser"]),
            ("Wrong: @123 (only numbers) Right: @user123", ["user123"]),
            ("Bad: @spaces not allowed Good: @nospaces", ["nospaces"]),
        ]
        
        passed_mentions = 0
        total_mentions = len(mention_cases)
        positive_mentions_tests_passed = 0
        total_positive_mentions_tests = 0
        
        try:
            extract_mentions_func = globals()["extract_mentions"]
            failing_mention_cases = []
            for i, (text, expected) in enumerate(mention_cases):
                try:
                    result = extract_mentions_func(text)
                    if expected:  # Count positive tests
                        total_positive_mentions_tests += 1
                        if self.compare_results(result, expected):
                            positive_mentions_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_mentions += 1
                    else:
                        failing_mention_cases.append((i+1, text, expected, result))
                        
                except Exception as e:
                    failing_mention_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
            
            # Print failing mention cases
            if failing_mention_cases:
                print(f"\n❌ FAILING MENTION TEST CASES ({len(failing_mention_cases)} total):")
                for test_num, text, expected, result in failing_mention_cases[:5]:
                    print(f"  Test {test_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got: {result}")
                    print()
                if len(failing_mention_cases) > 5:
                    print(f"  ... and {len(failing_mention_cases) - 5} more failing cases")
                    
        except KeyError:
            print("❌ Function extract_mentions not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_mentions_tests_passed > 0:
            mention_score = (passed_mentions / total_mentions) * 1.5
        else:
            mention_score = 0.0
        print(f"Mention extraction: {passed_mentions}/{total_mentions} passed ({mention_score:.1f}/1.5 points)")

        # Test extract_emojis - 50+ challenging cases
        emoji_cases = [
            # Basic emojis
            ("Great day! 🎓 Looking forward to graduation! 🎉", ["🎓", "🎉"]),
            ("Weather is nice ☀️ and I'm happy 😊", ["☀️", "😊"]),
            ("Love coding! 💻", ["💻"]),
            ("Coffee time ☕", ["☕"]),
            ("Book reading 📚", ["📚"]),
            
            # Multiple same emojis
            ("Multiple same emoji: 🎓🎓🎓", ["🎓", "🎓", "🎓"]),
            ("Celebration: 🎉🎉🎉🎉", ["🎉", "🎉", "🎉", "🎉"]),
            ("Happy: 😊😊😊", ["😊", "😊", "😊"]),
            ("Stars: ⭐⭐⭐⭐⭐", ["⭐", "⭐", "⭐", "⭐", "⭐"]),
            ("Hearts: ❤️❤️❤️", ["❤️", "❤️", "❤️"]),
            
            # Face emojis
            ("Emotions: 😀 😃 😄 😁 😆", ["😀", "😃", "😄", "😁", "😆"]),
            ("More emotions: 😊 😂 🤣 😍 🥰", ["😊", "😂", "🤣", "😍", "🥰"]),
            ("Sad faces: 😢 😭 😔 😞 😟", ["😢", "😭", "😔", "😞", "😟"]),
            ("Surprised: 😮 😯 😲 🤯 😱", ["😮", "😯", "😲", "🤯", "😱"]),
            ("Thinking: 🤔 😐 😑 🙄 😏", ["🤔", "😐", "😑", "🙄", "😏"]),
            
            # Object emojis
            ("School items: 🎓 📚 ✏️ 📝 🖊️", ["🎓", "📚", "✏️", "📝", "🖊️"]),
            ("Tech items: 💻 📱 ⌚ 🖥️ ⌨️", ["💻", "📱", "⌚", "🖥️", "⌨️"]),
            ("Food items: 🍎 🍌 🍕 🍔 🍰", ["🍎", "🍌", "🍕", "🍔", "🍰"]),
            ("Transport: 🚗 🚕 🚌 ✈️ 🚀", ["🚗", "🚕", "🚌", "✈️", "🚀"]),
            ("Sports: ⚽ 🏀 🏈 🎾 🏐", ["⚽", "🏀", "🏈", "🎾", "🏐"]),
            
            # Nature emojis
            ("Weather: ☀️ ⛅ ☁️ 🌧️ ⛈️", ["☀️", "⛅", "☁️", "🌧️", "⛈️"]),
            ("Plants: 🌱 🌿 🌳 🌲 🌴", ["🌱", "🌿", "🌳", "🌲", "🌴"]),
            ("Animals: 🐶 🐱 🐭 🐹 🐰", ["🐶", "🐱", "🐭", "🐹", "🐰"]),
            ("Ocean: 🌊 🐠 🐟 🦈 🐙", ["🌊", "🐠", "🐟", "🦈", "🐙"]),
            
            # Activity emojis
            ("Activities: 🏃‍♂️ 🚴‍♀️ 🏊‍♂️ 🧘‍♀️ 🏋️‍♂️", ["🏃‍♂️", "🚴‍♀️", "🏊‍♂️", "🧘‍♀️", "🏋️‍♂️"]),
            ("Hobbies: 🎨 🎸 🎵 📸 ✍️", ["🎨", "🎸", "🎵", "📸", "✍️"]),
            ("Games: 🎮 🎯 🎲 🃏 🧩", ["🎮", "🎯", "🎲", "🃏", "🧩"]),
            
            # Symbol emojis
            ("Symbols: ⭐ 💫 ✨ 💥 💯", ["⭐", "💫", "✨", "💥", "💯"]),
            ("Arrows: ⬆️ ⬇️ ⬅️ ➡️ ↗️", ["⬆️", "⬇️", "⬅️", "➡️", "↗️"]),
            ("Shapes: ❤️ 💙 💚 💛 💜", ["❤️", "💙", "💚", "💛", "💜"]),
            ("Signs: ✅ ❌ ⚠️ 🚫 💯", ["✅", "❌", "⚠️", "🚫", "💯"]),
            
            # Flag emojis
            ("Flags: 🇺🇸 🇬🇧 🇨🇦 🇫🇷 🇩🇪", ["🇺🇸", "🇬🇧", "🇨🇦", "🇫🇷", "🇩🇪"]),
            ("More flags: 🇯🇵 🇨🇳 🇰🇷 🇮🇳 🇧🇷", ["🇯🇵", "🇨🇳", "🇰🇷", "🇮🇳", "🇧🇷"]),
            
            # Emojis with text context
            ("Great presentation! 👏 Well done! 👍", ["👏", "👍"]),
            ("Congratulations on your graduation! 🎓 So proud! 😊", ["🎓", "😊"]),
            ("Working late tonight 🌙 Need coffee ☕", ["🌙", "☕"]),
            ("Beautiful sunset today 🌅 Perfect weather ☀️", ["🌅", "☀️"]),
            ("Finished my project! 🎉 Time to celebrate 🥳", ["🎉", "🥳"]),
            
            # Emojis at different positions
            ("🎯 Starting strong with goals", ["🎯"]),
            ("Working hard 💪 in the middle", ["💪"]),
            ("Ending with success! 🏆", ["🏆"]),
            ("🔥 Beginning 🚀 middle 🎊 end", ["🔥", "🚀", "🎊"]),
            
            # Complex emoji sequences
            ("Story: 🌅 morning ➡️ work 💻 ➡️ gym 🏋️‍♂️ ➡️ home 🏠", 
             ["🌅", "➡️", "💻", "➡️", "🏋️‍♂️", "➡️", "🏠"]),
            ("Recipe: 🥕 + 🧅 + 🍖 = 🍲 Delicious! 😋", 
             ["🥕", "🧅", "🍖", "🍲", "😋"]),
            
            # Skin tone variations
            ("Diversity: 👋🏻 👋🏼 👋🏽 👋🏾 👋🏿", ["👋🏻", "👋🏼", "👋🏽", "👋🏾", "👋🏿"]),
            ("Hands: 👍🏻 👍🏼 👍🏽 👍🏾 👍🏿", ["👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿"]),
            
            # Professional emojis
            ("Work: 💼 📊 📈 💡 �", ["💼", "📊", "📈", "💡", "�"]),
            ("Meeting: 🤝 📝 ✅ 📋 💻", ["🤝", "📝", "✅", "📋", "💻"]),
            ("Success: � 🥇 🎖️ 🏅 👑", ["�", "🥇", "🎖️", "🏅", "👑"]),
            
            # Time-related emojis
            ("Schedule: ⏰ 🕐 🕑 🕒 🕓", ["⏰", "🕐", "🕑", "🕒", "🕓"]),
            ("Calendar: 📅 📆 🗓️ ⏱️ ⏲️", ["📅", "📆", "🗓️", "⏱️", "⏲️"]),
            
            # No emojis
            ("No emojis in this text!", []),
            ("Just regular text without any unicode symbols", []),
            ("Regular ASCII characters only", []),
            ("Text with numbers 123 and letters abc", []),
            ("Punctuation!@#$%^&*() but no emojis", []),
        ]
        
        passed_emojis = 0
        total_emojis = len(emoji_cases)
        positive_emojis_tests_passed = 0
        total_positive_emojis_tests = 0
        
        try:
            extract_emojis_func = globals()["extract_emojis"]
            failing_emoji_cases = []
            for i, (text, expected) in enumerate(emoji_cases):
                try:
                    result = extract_emojis_func(text)
                    if expected:  # Count positive tests
                        total_positive_emojis_tests += 1
                        if self.compare_results(result, expected):
                            positive_emojis_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_emojis += 1
                    else:
                        failing_emoji_cases.append((i+1, text, expected, result))
                        
                except Exception as e:
                    failing_emoji_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
            
            # Print failing emoji cases
            if failing_emoji_cases:
                print(f"\n❌ FAILING EMOJI TEST CASES ({len(failing_emoji_cases)} total):")
                for test_num, text, expected, result in failing_emoji_cases[:5]:
                    print(f"  Test {test_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got: {result}")
                    print()
                if len(failing_emoji_cases) > 5:
                    print(f"  ... and {len(failing_emoji_cases) - 5} more failing cases")
                    
        except KeyError:
            print("❌ Function extract_emojis not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_emojis_tests_passed > 0:
            emoji_score = (passed_emojis / total_emojis) * 2.0
        else:
            emoji_score = 0.0
        print(f"Emoji extraction: {passed_emojis}/{total_emojis} passed ({emoji_score:.1f}/2.0 points)")
        
        total_score = hashtag_score + mention_score + emoji_score
        self.total_score += total_score
        self.max_score += 5
        print(f"Q3 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q3", total_score, 5, 
                                [f"Hashtags: {passed_hashtags}/{total_hashtags}, Mentions: {passed_mentions}/{total_mentions}, Emojis: {passed_emojis}/{total_emojis}"]))

    def test_q4(self) -> None:
        """Test Q4: Date and time extraction - Comprehensive test with 50+ cases each."""
        print(f"\n=== Q4: Date and Time Extraction (5 points) ===")
        
        # Test extract_dates - 50+ challenging cases
        date_cases = [
            # Standard US format (Month Day, Year)
            ("Meeting on July 25, 2025", ["July 25, 2025"]),
            ("Conference on January 1, 2025", ["January 1, 2025"]),
            ("Deadline is December 31, 2024", ["December 31, 2024"]),
            ("Event scheduled for March 15, 2025", ["March 15, 2025"]),
            ("Workshop on September 22, 2025", ["September 22, 2025"]),
            
            # ISO format (YYYY-MM-DD)
            ("Deadline is 2025-07-30", ["2025-07-30"]),
            ("Meeting on 2025-01-15", ["2025-01-15"]),
            ("Conference 2024-12-25", ["2024-12-25"]),
            ("Event on 2025-03-10", ["2025-03-10"]),
            ("Workshop 2025-09-05", ["2025-09-05"]),
            
            # US numeric format (MM/DD/YYYY)
            ("Date: 12/25/2025", ["12/25/2025"]),
            ("Meeting 07/30/2025", ["07/30/2025"]),
            ("Event on 01/15/2025", ["01/15/2025"]),
            ("Deadline 03/20/2025", ["03/20/2025"]),
            ("Conference 09/12/2025", ["09/12/2025"]),
            
            # European format (DD/MM/YYYY and DD-MM-YYYY)
            ("European date: 25/12/2025", ["25/12/2025"]),
            ("Meeting 30-07-2025", ["30-07-2025"]),
            ("Event on 15.01.2025", ["15.01.2025"]),
            ("Deadline 20/03/2025", ["20/03/2025"]),
            ("Workshop 12-09-2025", ["12-09-2025"]),
            
            # Short month names
            ("Event on Jan 15, 2025", ["Jan 15, 2025"]),
            ("Meeting Feb 28, 2025", ["Feb 28, 2025"]),
            ("Conference Mar 10, 2025", ["Mar 10, 2025"]),
            ("Workshop Apr 22, 2025", ["Apr 22, 2025"]),
            ("Deadline May 30, 2025", ["May 30, 2025"]),
            ("Event Jun 15, 2025", ["Jun 15, 2025"]),
            ("Meeting Jul 04, 2025", ["Jul 04, 2025"]),
            ("Conference Aug 20, 2025", ["Aug 20, 2025"]),
            ("Workshop Sep 12, 2025", ["Sep 12, 2025"]),
            ("Event Oct 31, 2025", ["Oct 31, 2025"]),
            ("Meeting Nov 11, 2025", ["Nov 11, 2025"]),
            ("Conference Dec 25, 2025", ["Dec 25, 2025"]),
            
            # Different year formats
            ("Meeting in July 25, 25", ["July 25, 25"]),
            ("Event on Jan 1, 2025", ["Jan 1, 2025"]),
            ("Conference March 15, 2025", ["March 15, 2025"]),
            
            # Multiple dates in one text
            ("Events: January 1, 2025 and 2025-07-30", ["January 1, 2025", "2025-07-30"]),
            ("Dates: 12/25/2025 and 25-12-2025", ["12/25/2025", "25-12-2025"]),
            ("Schedule: July 15, 2025, August 20, 2025, September 10, 2025", 
             ["July 15, 2025", "August 20, 2025", "September 10, 2025"]),
            ("Important dates: 2025-01-01, 2025-06-15, 2025-12-31", 
             ["2025-01-01", "2025-06-15", "2025-12-31"]),
            
            # Dates with ordinal indicators
            ("Meeting on July 25th, 2025", ["July 25th, 2025"]),
            ("Conference on January 1st, 2025", ["January 1st, 2025"]),
            ("Event on March 3rd, 2025", ["March 3rd, 2025"]),
            ("Workshop on April 22nd, 2025", ["April 22nd, 2025"]),
            ("Deadline May 15th, 2025", ["May 15th, 2025"]),
            
            # Dates in different contexts
            ("The project deadline is March 15, 2025.", ["March 15, 2025"]),
            ("Please submit by 2025-07-30 at the latest.", ["2025-07-30"]),
            ("Conference registration opens on 01/15/2025", ["01/15/2025"]),
            ("Academic year starts September 1, 2025", ["September 1, 2025"]),
            ("Final exams begin December 10, 2025", ["December 10, 2025"]),
            
            # Relative date expressions (if implemented)
            ("Meeting tomorrow, July 26, 2025", ["July 26, 2025"]),
            ("Event next week on August 1, 2025", ["August 1, 2025"]),
            ("Conference last month was June 15, 2025", ["June 15, 2025"]),
            
            # Historical dates
            ("Founded on January 1, 1900", ["January 1, 1900"]),
            ("Established in March 15, 1850", ["March 15, 1850"]),
            ("Built on 1776-07-04", ["1776-07-04"]),
            ("Created December 25, 2000", ["December 25, 2000"]),
            
            # Future dates
            ("Planning for January 1, 2030", ["January 1, 2030"]),
            ("Target date: 2050-12-31", ["2050-12-31"]),
            ("Future event on March 15, 2040", ["March 15, 2040"]),
            
            # Dates with day names
            ("Monday, July 25, 2025", ["July 25, 2025"]),
            ("Tuesday, 2025-08-15", ["2025-08-15"]),
            ("Wednesday 03/20/2025", ["03/20/2025"]),
            ("Thursday, January 30, 2025", ["January 30, 2025"]),
            ("Friday 2025-09-12", ["2025-09-12"]),
            ("Saturday, April 5, 2025", ["April 5, 2025"]),
            ("Sunday 06/15/2025", ["06/15/2025"]),
            
            # Dates with punctuation
            ("Date: (July 25, 2025)", ["July 25, 2025"]),
            ("Meeting [2025-08-15] confirmed", ["2025-08-15"]),
            ("Event on 'March 20, 2025'", ["March 20, 2025"]),
            ("Deadline \"January 30, 2025\"", ["January 30, 2025"]),
            ("Conference <September 12, 2025>", ["September 12, 2025"]),
            
            # No dates
            ("No dates in this text!", []),
            ("Just regular text without temporal information", []),
            ("Meeting at the office but no specific date", []),
            ("Numbers 123 and 456 but no dates", []),
            ("July and 2025 mentioned separately", []),
        ]
        
        passed_dates = 0
        total_dates = len(date_cases)
        positive_dates_tests_passed = 0
        total_positive_dates_tests = 0
        failing_date_cases = []
        
        try:
            extract_dates_func = globals()["extract_dates"]
            for i, (text, expected) in enumerate(date_cases):
                try:
                    result = extract_dates_func(text)
                    if expected:  # Count positive tests
                        total_positive_dates_tests += 1
                        if self.compare_results(result, expected):
                            positive_dates_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_dates += 1
                    else:
                        failing_date_cases.append((i+1, text, expected, result))
                except Exception as e:
                    failing_date_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
        except KeyError:
            print("❌ Function extract_dates not found!")
        
        # Show failing cases if any
        if failing_date_cases:
            print(f"\n❌ FAILING DATE TEST CASES ({len(failing_date_cases)} total):")
            for test_num, text, expected, got in failing_date_cases[:10]:  # Show first 10
                print(f"  Test {test_num}: '{text}'")
                print(f"    Expected: {expected}")
                print(f"    Got: {got}")
                print()
        
        # Only award points if student gets at least one positive test case right
        if positive_dates_tests_passed > 0:
            date_score = (passed_dates / total_dates) * 2.5
        else:
            date_score = 0.0
        print(f"Date extraction: {passed_dates}/{total_dates} passed ({date_score:.1f}/2.5 points)")

        # Test extract_times - 50+ challenging cases
        time_cases = [
            # 12-hour format with AM/PM
            ("Meeting at 3:30 PM", ["3:30 PM"]),
            ("Conference at 9:00 AM", ["9:00 AM"]),
            ("Event at 11:45 AM", ["11:45 AM"]),
            ("Workshop at 2:15 PM", ["2:15 PM"]),
            ("Deadline at 11:59 PM", ["11:59 PM"]),
            
            # 12-hour format variations
            ("Meeting at 9:00am", ["9:00am"]),
            ("Event at 5:30 p.m.", ["5:30 p.m."]),
            ("Conference at 2:15PM", ["2:15PM"]),
            ("Workshop at 10:00 A.M.", ["10:00 A.M."]),
            ("Call at 7:30P.M.", ["7:30P.M."]),
            
            # 24-hour format
            ("Conference call at 14:30:00", ["14:30:00"]),
            ("Meeting at 09:15", ["09:15"]),
            ("Event at 16:45", ["16:45"]),
            ("Workshop at 13:00", ["13:00"]),
            ("Deadline at 23:59", ["23:59"]),
            ("Start at 00:00", ["00:00"]),
            ("Noon at 12:00", ["12:00"]),
            ("End at 18:30", ["18:30"]),
            
            # Times with seconds
            ("Precise time: 14:30:45", ["14:30:45"]),
            ("Meeting at 09:15:30", ["09:15:30"]),
            ("Event at 16:45:00", ["16:45:00"]),
            ("Start at 08:00:15", ["08:00:15"]),
            ("End at 17:30:30", ["17:30:30"]),
            
            # Multiple times in text
            ("Event: 9:00am to 5:30 p.m.", ["9:00am", "5:30 p.m."]),
            ("Schedule: 10:00 AM, 2:30 PM, 6:00 PM", ["10:00 AM", "2:30 PM", "6:00 PM"]),
            ("Times: 2:15 AM and 14:45", ["2:15 AM", "14:45"]),
            ("Meeting from 9:00 to 10:30", ["9:00", "10:30"]),
            ("Conference 08:30, break 10:15, lunch 12:00", ["08:30", "10:15", "12:00"]),
            
            # Times in different contexts
            ("Please arrive by 9:00 AM sharp", ["9:00 AM"]),
            ("The presentation starts at 2:30 PM", ["2:30 PM"]),
            ("Deadline submission before 11:59 PM", ["11:59 PM"]),
            ("Office hours: 14:00 to 16:00", ["14:00", "16:00"]),
            ("Call scheduled for 15:30", ["15:30"]),
            
            # Times with time zones
            ("Meeting at 3:30 PM EST", ["3:30 PM"]),
            ("Conference at 14:00 UTC", ["14:00"]),
            ("Event at 9:00 AM PST", ["9:00 AM"]),
            ("Workshop at 16:30 GMT", ["16:30"]),
            ("Call at 11:00 AM EDT", ["11:00 AM"]),
            
            # Specific time expressions
            ("Noon meeting at 12:00 PM", ["12:00 PM"]),
            ("Midnight deadline at 12:00 AM", ["12:00 AM"]),
            ("Early morning at 6:00 AM", ["6:00 AM"]),
            ("Late evening at 11:30 PM", ["11:30 PM"]),
            ("Dawn at 5:30 AM", ["5:30 AM"]),
            ("Dusk at 7:45 PM", ["7:45 PM"]),
            
            # Times with ranges
            ("Office hours 9:00 - 17:00", ["9:00", "17:00"]),
            ("Event from 14:30 to 16:45", ["14:30", "16:45"]),
            ("Meeting 10:00am - 11:30am", ["10:00am", "11:30am"]),
            ("Workshop 2:00 PM to 4:30 PM", ["2:00 PM", "4:30 PM"]),
            ("Conference 08:00 until 18:00", ["08:00", "18:00"]),
            
            # Times with different separators
            ("Meeting at 14.30", ["14.30"]),
            ("Event at 9h30", ["9h30"]),
            ("Conference at 16:45h", ["16:45h"]),
            ("Workshop at 13h00", ["13h00"]),
            
            # Times with punctuation around them
            ("Time: (3:30 PM)", ["3:30 PM"]),
            ("Meeting [14:30] confirmed", ["14:30"]),
            ("Event at '9:00 AM'", ["9:00 AM"]),
            ("Deadline \"11:59 PM\"", ["11:59 PM"]),
            ("Conference <2:15 PM>", ["2:15 PM"]),
            
            # Times in schedules
            ("Monday 9:00 AM, Tuesday 10:30 AM, Wednesday 2:00 PM", 
             ["9:00 AM", "10:30 AM", "2:00 PM"]),
            ("Schedule: 08:00 breakfast, 12:00 lunch, 18:00 dinner", 
             ["08:00", "12:00", "18:00"]),
            ("Timetable: 9:15, 10:45, 14:30, 16:00", 
             ["9:15", "10:45", "14:30", "16:00"]),
            
            # Edge cases
            ("Time 12:00 could be noon or midnight", ["12:00"]),
            ("Meeting at exactly 15:30:00", ["15:30:00"]),
            ("Event starts 9:00 AM sharp", ["9:00 AM"]),
            ("Deadline approaches at 23:59:59", ["23:59:59"]),
            
            # No times
            ("No times in this text!", []),
            ("Just regular text without temporal information", []),
            ("Meeting at the office but no specific time", []),
            ("Numbers 123 and 456 but no times", []),
            ("AM and PM mentioned but no actual times", []),
            
            # Invalid times (should be rejected)
            ("Invalid: 25:00 (hour too high) Valid: 14:30", ["14:30"]),
            ("Wrong: 12:60 (minute too high) Right: 12:30", ["12:30"]),
            ("Bad: 13:30 AM (contradiction) Good: 1:30 PM", ["1:30 PM"]),
        ]
        
        passed_times = 0
        total_times = len(time_cases)
        positive_times_tests_passed = 0
        total_positive_times_tests = 0
        failing_time_cases = []
        
        try:
            extract_times_func = globals()["extract_times"]
            for i, (text, expected) in enumerate(time_cases):
                try:
                    result = extract_times_func(text)
                    if expected:  # Count positive tests
                        total_positive_times_tests += 1
                        if self.compare_results(result, expected):
                            positive_times_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_times += 1
                    else:
                        failing_time_cases.append((i+1, text, expected, result))
                except Exception as e:
                    failing_time_cases.append((i+1, text, expected, f"Exception: {str(e)}"))
        except KeyError:
            print("❌ Function extract_times not found!")
        
        # Show failing cases if any
        if failing_time_cases:
            print(f"\n❌ FAILING TIME TEST CASES ({len(failing_time_cases)} total):")
            for test_num, text, expected, got in failing_time_cases[:10]:  # Show first 10
                print(f"  Test {test_num}: '{text}'")
                print(f"    Expected: {expected}")
                print(f"    Got: {got}")
                print()
        
        # Only award points if student gets at least one positive test case right
        if positive_times_tests_passed > 0:
            time_score = (passed_times / total_times) * 2.5
        else:
            time_score = 0.0
        print(f"Time extraction: {passed_times}/{total_times} passed ({time_score:.1f}/2.5 points)")
        
        total_score = date_score + time_score
        self.total_score += total_score
        self.max_score += 5
        print(f"Q4 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q4", total_score, 5, [f"Dates: {passed_dates}/{total_dates}, Times: {passed_times}/{total_times}"]))

    def test_q5(self) -> None:
        """Test Q5: Document structure extraction - Comprehensive test with 50+ cases each."""
        print(f"\n=== Q5: Document Structure Extraction (5 points) ===")
        
        # Test extract_sections - 50+ challenging cases
        section_test_cases = [
            # Basic markdown headers
            ("# Introduction\nContent here", ["Introduction"]),
            ("## Background\nMore content", ["Background"]),
            ("### Details\nDetailed content", ["Details"]),
            ("#### Subsection\nSubsection content", ["Subsection"]),
            ("##### Minor Section\nMinor content", ["Minor Section"]),
            ("###### Smallest\nSmallest content", ["Smallest"]),
            
            # Multiple headers
            ("# Main Title\n## Subsection\n### Details", ["Main Title", "Subsection", "Details"]),
            ("## Chapter 1\n### Section 1.1\n### Section 1.2", ["Chapter 1", "Section 1.1", "Section 1.2"]),
            ("# Introduction\n## Methods\n## Results\n## Conclusion", 
             ["Introduction", "Methods", "Results", "Conclusion"]),
            
            # Headers with numbers
            ("## 1. Introduction", ["1. Introduction"]),
            ("### 2.1 Background", ["2.1 Background"]),
            ("#### 3.2.1 Methodology", ["3.2.1 Methodology"]),
            ("## Chapter 1: Getting Started", ["Chapter 1: Getting Started"]),
            ("### Section 2.3: Advanced Topics", ["Section 2.3: Advanced Topics"]),
            
            # Headers with special characters
            ("# Introduction & Overview", ["Introduction & Overview"]),
            ("## Methods - Part I", ["Methods - Part I"]),
            ("### Results (Preliminary)", ["Results (Preliminary)"]),
            ("#### Discussion [Draft]", ["Discussion [Draft]"]),
            ("##### Conclusion: Final Thoughts", ["Conclusion: Final Thoughts"]),
            
            # Academic paper structure
            ("# Abstract\n## Introduction\n## Literature Review\n## Methodology\n## Results\n## Discussion\n## Conclusion", 
             ["Abstract", "Introduction", "Literature Review", "Methodology", "Results", "Discussion", "Conclusion"]),
            
            # Technical documentation
            ("# API Documentation\n## Authentication\n## Endpoints\n### GET /users\n### POST /users\n## Error Handling", 
             ["API Documentation", "Authentication", "Endpoints", "GET /users", "POST /users", "Error Handling"]),
            
            # Mixed levels
            ("# Part I\n## Chapter 1\n### 1.1 Overview\n### 1.2 Details\n## Chapter 2\n# Part II", 
             ["Part I", "Chapter 1", "1.1 Overview", "1.2 Details", "Chapter 2", "Part II"]),
            
            # Headers with content between
            ("# Introduction\nThis is intro content\n## Background\nBackground info\n### History\nHistorical context", 
             ["Introduction", "Background", "History"]),
            
            # No headers
            ("Just regular text without any headers", []),
            ("Plain content with no markdown formatting", []),
            ("Text with # but not at start of line", []),
            
            # Edge cases
            ("#NoSpace", ["NoSpace"]),
            ("# ", []),  # Empty header
            ("####### Too many hashes", []),  # Invalid markdown
            ("Not a header # in middle", []),
            ("# Valid Header\n### Another Valid Header", ["Valid Header", "Another Valid Header"]),
        ]
        
        passed_sections = 0
        total_sections = len(section_test_cases)
        positive_sections_tests_passed = 0
        total_positive_sections_tests = 0
        
        try:
            extract_sections_func = globals()["extract_sections"]
            for i, (text, expected) in enumerate(section_test_cases):
                try:
                    result = extract_sections_func(text)
                    if expected:  # Count positive tests
                        total_positive_sections_tests += 1
                        if self.compare_results(result, expected):
                            positive_sections_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_sections += 1
                    elif i < 5:  # Show first few failures for debugging
                        print(f"❌ Section test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Section test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function extract_sections not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_sections_tests_passed > 0:
            section_score = (passed_sections / total_sections) * 1.5
        else:
            section_score = 0.0
        print(f"Section extraction: {passed_sections}/{total_sections} passed ({section_score:.1f}/1.5 points)")

        # Test extract_citations - Simplified educational cases
        citation_test_cases = [
            # Standard academic citations - consistent "Author (Year)" format
            ("According to Smith et al. (2023), this is important.", ["Smith et al. (2023)"]),
            ("Research by Jones (2022) shows that...", ["Jones (2022)"]),
            ("Previous work by Brown (2021) demonstrates...", ["Brown (2021)"]),
            ("As noted by Wilson et al. (2024)...", ["Wilson et al. (2024)"]),
            ("The study by Taylor (2023) found...", ["Taylor (2023)"]),
            
            # Multiple authors - simplified patterns
            ("Research by Smith and Jones (2023)...", ["Smith and Jones (2023)"]),
            ("Study by Brown and Wilson (2022)...", ["Brown and Wilson (2022)"]),
            ("Research by Lee and Park (2023)...", ["Lee and Park (2023)"]),
            
            # Et al. variations
            ("Smith et al. (2023) demonstrated...", ["Smith et al. (2023)"]),
            ("Jones et al. (2022) found...", ["Jones et al. (2022)"]),
            ("Brown et al. (2024) reported...", ["Brown et al. (2024)"]),
            ("According to Wilson et al. (2021)...", ["Wilson et al. (2021)"]),
            
            # Multiple citations in one sentence
            ("See Jones (2022) and Brown (2021).", ["Jones (2022)", "Brown (2021)"]),
            ("Multiple studies: Smith (2023), Jones et al. (2022)", ["Smith (2023)", "Jones et al. (2022)"]),
            ("Research shows (Brown, 2021; Wilson, 2022; Taylor, 2023)...", 
             ["Brown, 2021", "Wilson, 2022", "Taylor, 2023"]),
            ("Previous work (Smith et al., 2020; Jones, 2021; Brown et al., 2022)...", 
             ["Smith et al., 2020", "Jones, 2021", "Brown et al., 2022"]),
            
            # Simple name variations - educational focus
            ("Smith (2023) conducted research...", ["Smith (2023)"]),
            ("Research by Johnson (2023)...", ["Johnson (2023)"]),
            ("Study by Williams (2023)...", ["Williams (2023)"]),
            ("According to Brown (2023)...", ["Brown (2023)"]),
            ("Davis (2022) noted...", ["Davis (2022)"]),
            
            # Organization citations
            ("WHO (2023) guidelines state...", ["WHO (2023)"]),
            ("According to NASA (2022)...", ["NASA (2022)"]),
            ("The CDC (2024) recommends...", ["CDC (2024)"]),
            ("UNESCO (2023) reports...", ["UNESCO (2023)"]),
            ("UNICEF (2022) data shows...", ["UNICEF (2022)"]),
            
            # Government and institutional citations
            ("Department of Education (2023)...", ["Department of Education (2023)"]),
            ("Ministry of Health (2022)...", ["Ministry of Health (2022)"]),
            ("National Institute (2024)...", ["National Institute (2024)"]),
            ("World Bank (2023)...", ["World Bank (2023)"]),
            
            # Citations with page numbers
            ("Smith (2023, p. 45) argues...", ["Smith (2023, p. 45)"]),
            ("Jones et al. (2022, pp. 12-15)...", ["Jones et al. (2022, pp. 12-15)"]),
            ("Brown (2021, p. 234)...", ["Brown (2021, p. 234)"]),
            ("Wilson (2024, pp. 45-67)...", ["Wilson (2024, pp. 45-67)"]),
            
            # Book and journal citations - consistent format
            ("In his book, Smith (2023)...", ["Smith (2023)"]),
            ("The textbook by Jones (2022)...", ["Jones (2022)"]),
            ("According to the handbook by Wilson (2024)...", ["Wilson (2024)"]),
            
            # Parenthetical citations - standalone format
            ("(Smith, 2023)", ["Smith, 2023"]),
            ("(Jones et al., 2022)", ["Jones et al., 2022"]),
            ("(Brown and Davis, 2021)", ["Brown and Davis, 2021"]),
            
            # Simple international names
            ("Research by Garcia (2022)...", ["Garcia (2022)"]),
            ("Study by Lopez (2024)...", ["Lopez (2024)"]),
            
            # No citations
            ("No citations in this text!", []),
            ("Just regular text without any references", []),
            ("Text with years 2023 and names Smith but no citations", []),
            ("Numbers (123) and names but no proper citations", []),
        ]
        
        passed_citations = 0
        total_citations = len(citation_test_cases)
        positive_citations_tests_passed = 0
        total_positive_citations_tests = 0
        
        try:
            extract_citations_func = globals()["extract_citations"]
            failed_cases = []
            for i, (text, expected) in enumerate(citation_test_cases):
                try:
                    result = extract_citations_func(text)
                    if expected:  # Count positive tests
                        total_positive_citations_tests += 1
                        if self.compare_results(result, expected):
                            positive_citations_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_citations += 1
                    else:
                        failed_cases.append((i+1, text[:50] + "..." if len(text) > 50 else text, expected, result))
                except Exception as e:
                    failed_cases.append((i+1, text[:50] + "..." if len(text) > 50 else text, expected, f"Exception: {str(e)}"))
            
            # Show detailed failure analysis
            if failed_cases:
                print(f"\n📋 Citation Extraction Failure Analysis ({len(failed_cases)} failures):")
                for case_num, text, expected, actual in failed_cases[:15]:  # Show first 15 failures
                    print(f"  Case {case_num}: '{text}'")
                    print(f"    Expected: {expected}")
                    print(f"    Got:      {actual}")
                    print()
                    
        except KeyError:
            print("❌ Function extract_citations not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_citations_tests_passed > 0:
            citation_score = (passed_citations / total_citations) * 1.5
        else:
            citation_score = 0.0
        print(f"Citation extraction: {passed_citations}/{total_citations} passed ({citation_score:.1f}/1.5 points)")

        # Test extract_code_blocks - 50+ challenging cases
        code_block_cases = [
            # Basic code blocks
            ("```python\nprint('Hello')\n```", ["print('Hello')"]),
            ("```javascript\nconsole.log('Hi');\n```", ["console.log('Hi');"]),
            ("```java\nSystem.out.println('Hello');\n```", ["System.out.println('Hello');"]),
            ("```cpp\nstd::cout << \"Hello\";\n```", ["std::cout << \"Hello\";"]),
            ("```bash\necho 'Hello World'\n```", ["echo 'Hello World'"]),
            
            # Code blocks without language specification
            ("```\nsimple code\n```", ["simple code"]),
            ("```\nx = 5\ny = 10\n```", ["x = 5\ny = 10"]),
            ("```\nfunction hello() {\n  return 'world';\n}\n```", ["function hello() {\n  return 'world';\n}"]),
            
            # Multi-line code blocks
            ("```python\ndef hello():\n    print('Hello, World!')\n    return True\n```", 
             ["def hello():\n    print('Hello, World!')\n    return True"]),
            ("```javascript\nfunction calculate(a, b) {\n  let sum = a + b;\n  return sum;\n}\n```", 
             ["function calculate(a, b) {\n  let sum = a + b;\n  return sum;\n}"]),
            ("```sql\nSELECT name, age\nFROM users\nWHERE age > 18\nORDER BY name;\n```", 
             ["SELECT name, age\nFROM users\nWHERE age > 18\nORDER BY name;"]),
            
            # Multiple code blocks in one text
            ("Code: ```python\nprint('hi')\n``` and ```js\nconsole.log('bye');\n```", 
             ["print('hi')", "console.log('bye');"]),
            ("Examples:\n```python\nx = 1\n```\nAnd:\n```python\ny = 2\n```", 
             ["x = 1", "y = 2"]),
            
            # Code blocks with different languages
            ("```python\nimport numpy as np\n```", ["import numpy as np"]),
            ("```r\nlibrary(ggplot2)\n```", ["library(ggplot2)"]),
            ("```matlab\nA = [1 2; 3 4];\n```", ["A = [1 2; 3 4];"]),
            ("```ruby\nputs 'Hello Ruby'\n```", ["puts 'Hello Ruby'"]),
            ("```go\nfmt.Println('Hello Go')\n```", ["fmt.Println('Hello Go')"]),
            ("```rust\nprintln!(\"Hello Rust\");\n```", ["println!(\"Hello Rust\");"]),
            
            # Code blocks with comments
            ("```python\n# This is a comment\nprint('Hello')  # Inline comment\n```", 
             ["# This is a comment\nprint('Hello')  # Inline comment"]),
            ("```javascript\n// Function definition\nfunction test() {\n  // Return value\n  return 42;\n}\n```", 
             ["// Function definition\nfunction test() {\n  // Return value\n  return 42;\n}"]),
            
            # Code blocks with special characters
            ("```python\ntext = \"Special chars: @#$%^&*()\"\n```", ["text = \"Special chars: @#$%^&*()\""]),
            ("```bash\ngrep -E \"[0-9]+\" file.txt\n```", ["grep -E \"[0-9]+\" file.txt"]),
            ("```regex\n^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\n```", 
             ["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"]),
            
            # Code blocks with indentation
            ("```python\nclass MyClass:\n    def __init__(self):\n        self.value = 42\n    \n    def get_value(self):\n        return self.value\n```", 
             ["class MyClass:\n    def __init__(self):\n        self.value = 42\n    \n    def get_value(self):\n        return self.value"]),
            
            # HTML/XML code blocks
            ("```html\n<div class=\"container\">\n  <h1>Title</h1>\n  <p>Content</p>\n</div>\n```", 
             ["<div class=\"container\">\n  <h1>Title</h1>\n  <p>Content</p>\n</div>"]),
            ("```xml\n<?xml version=\"1.0\"?>\n<root>\n  <item>Value</item>\n</root>\n```", 
             ["<?xml version=\"1.0\"?>\n<root>\n  <item>Value</item>\n</root>"]),
            
            # JSON code blocks
            ("```json\n{\n  \"name\": \"John\",\n  \"age\": 30,\n  \"city\": \"New York\"\n}\n```", 
             ["{\n  \"name\": \"John\",\n  \"age\": 30,\n  \"city\": \"New York\"\n}"]),
            
            # Configuration files
            ("```yaml\nname: my-app\nversion: 1.0.0\ndependencies:\n  - numpy\n  - pandas\n```", 
             ["name: my-app\nversion: 1.0.0\ndependencies:\n  - numpy\n  - pandas"]),
            ("```ini\n[database]\nhost = localhost\nport = 5432\nname = mydb\n```", 
             ["[database]\nhost = localhost\nport = 5432\nname = mydb"]),
            
            # Empty code blocks
            ("```python\n\n```", [""]),
            ("```\n```", [""]),
            
            # Code blocks in documentation
            ("To run the script:\n```bash\npython script.py --input data.txt\n```\nThis will process the file.", 
             ["python script.py --input data.txt"]),
            ("Example usage:\n```python\nfrom mymodule import MyClass\nobj = MyClass()\nresult = obj.process()\n```", 
             ["from mymodule import MyClass\nobj = MyClass()\nresult = obj.process()"]),
            
            # No code blocks
            ("No code blocks here!", []),
            ("Just regular text without any code formatting", []),
            ("Text with backticks `inline code` but no blocks", []),
            ("Mentions ```python but not a complete block", []),
            
            # Invalid code blocks (should be rejected)
            ("Incomplete: ```python\nprint('hello')", []),  # Missing closing ```
            ("Wrong: ``python\ncode\n``", []),  # Wrong number of backticks
        ]
        
        passed_code = 0
        total_code = len(code_block_cases)
        positive_code_tests_passed = 0
        total_positive_code_tests = 0
        
        try:
            extract_code_blocks_func = globals()["extract_code_blocks"]
            for i, (text, expected) in enumerate(code_block_cases):
                try:
                    result = extract_code_blocks_func(text)
                    if expected:  # Count positive tests
                        total_positive_code_tests += 1
                        if self.compare_results(result, expected):
                            positive_code_tests_passed += 1
                    
                    if self.compare_results(result, expected):
                        passed_code += 1
                    elif i < 5:  # Show first few failures for debugging
                        print(f"❌ Code block test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Code block test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function extract_code_blocks not found!")
        
        # Only award points if student gets at least one positive test case right
        if positive_code_tests_passed > 0:
            code_score = (passed_code / total_code) * 2.0
        else:
            code_score = 0.0
        print(f"Code block extraction: {passed_code}/{total_code} passed ({code_score:.1f}/2.0 points)")
        
        total_score = section_score + citation_score + code_score
        self.total_score += total_score
        self.max_score += 5
        print(f"Q5 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q5", total_score, 5, 
                                [f"Sections: {passed_sections}/{total_sections}, Citations: {passed_citations}/{total_citations}, Code: {passed_code}/{total_code}"]))

    def test_q6(self) -> None:
        """Test Q6: Address extraction - Comprehensive test with 50+ cases."""
        print(f"\n=== Q6: Address Extraction (5 points) ===")
        
        # Test extract_addresses - Simplified educational cases focused on core patterns
        address_cases = [
            # Basic street addresses with numbers
            ("Send mail to 123 Main Street, Georgetown", 
             [{"full_address": "123 Main Street, Georgetown", "type": "street"}]),
            ("Visit us at 456 Oak Avenue, New Amsterdam", 
             [{"full_address": "456 Oak Avenue, New Amsterdam", "type": "street"}]),
            ("Office at 789 Pine Road, Linden", 
             [{"full_address": "789 Pine Road, Linden", "type": "street"}]),
            ("Located at 321 Water Street, Georgetown", 
             [{"full_address": "321 Water Street, Georgetown", "type": "street"}]),
            
            # PO Box addresses
            ("Contact P.O. Box 456", 
             [{"full_address": "P.O. Box 456", "type": "po_box"}]),
            ("Mail to PO Box 789", 
             [{"full_address": "PO Box 789", "type": "po_box"}]),
            ("Send to P.O. Box 123, Georgetown", 
             [{"full_address": "P.O. Box 123, Georgetown", "type": "po_box"}]),
            
            # Addresses with suites and units
            ("Office at 456 Oak Avenue, Suite 100, Georgetown", 
             [{"full_address": "456 Oak Avenue, Suite 100, Georgetown", "type": "street"}]),
            ("Located at 123 Main Street, Unit 5A, New Amsterdam", 
             [{"full_address": "123 Main Street, Unit 5A, New Amsterdam", "type": "street"}]),
            ("Visit 789 Water Street, Apt 15, Georgetown", 
             [{"full_address": "789 Water Street, Apt 15, Georgetown", "type": "street"}]),
            
            # Different street types
            ("Visit 123 Main Boulevard, Georgetown", 
             [{"full_address": "123 Main Boulevard, Georgetown", "type": "street"}]),
            ("Located at 456 Oak Drive, New Amsterdam", 
             [{"full_address": "456 Oak Drive, New Amsterdam", "type": "street"}]),
            ("Office at 789 Water Lane, Georgetown", 
             [{"full_address": "789 Water Lane, Georgetown", "type": "street"}]),
            ("Address is 111 Pine Circle, Linden", 
             [{"full_address": "111 Pine Circle, Linden", "type": "street"}]),
            
            # Multiple addresses (clear separation)
            ("Office: 123 Main Street, Georgetown. Branch: 456 Oak Avenue, New Amsterdam", 
             [{"full_address": "123 Main Street, Georgetown", "type": "street"}, 
              {"full_address": "456 Oak Avenue, New Amsterdam", "type": "street"}]),
            ("Mail: P.O. Box 123. Visit: 789 Water Street, Georgetown", 
             [{"full_address": "P.O. Box 123", "type": "po_box"}, 
              {"full_address": "789 Water Street, Georgetown", "type": "street"}]),
            
            # No addresses
            ("No addresses in this text!", []),
            ("Just regular text without any location information", []),
            ("Meeting at the office but no specific address", []),
            
            # Edge cases
            ("Street number only: 123", []),
            ("City only: Georgetown", []),
            ("Not an address: Street Fighter game", []),
        ]
        
        passed_addresses = 0
        positive_address_tests_passed = 0
        total_addresses = len(address_cases)
        
        try:
            extract_addresses_func = globals()["extract_addresses"]
            for i, (text, expected) in enumerate(address_cases):
                try:
                    result = extract_addresses_func(text)
                    if self.compare_results(result, expected):
                        passed_addresses += 1
                        # Only count positive tests (non-empty expected results)
                        if expected:  # Non-empty list means positive test
                            positive_address_tests_passed += 1
                    elif i < 5:  # Show first few failures for debugging
                        print(f"❌ Address test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Address test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function extract_addresses not found!")
        
        # Only award points if student got at least one positive test case correct
        if positive_address_tests_passed > 0:
            address_score = (passed_addresses / total_addresses) * 5.0
        else:
            address_score = 0.0
        self.total_score += address_score
        self.max_score += 5
        print(f"Address extraction: {passed_addresses}/{total_addresses} passed ({address_score:.1f}/5.0 points)")
        self.test_results.append(("Q6", address_score, 5, [f"Addresses: {passed_addresses}/{total_addresses}"]))

    def test_q7(self) -> None:
        """Test Q7: Log file parsing with complex real-world data."""
        # Load the challenging log file
        import os
        log_file_path = os.path.join(os.path.dirname(__file__), 'data', 'server_logs.txt')
        
        try:
            with open(log_file_path, 'r', encoding='utf-8') as f:
                log_content = f.read()
        except FileNotFoundError:
            print(f"Warning: Log file not found at {log_file_path}")
            log_content = """192.168.1.100 - admin [25/Jul/2025:10:30:45 +0000] "GET /api/users HTTP/1.1" 200 1234 "https://example.com/" "Mozilla/5.0"
10.0.0.1 - - [25/Jul/2025:10:31:00 +0000] "POST /login HTTP/1.1" 403 567 "-" "curl/7.68.0"
2001:db8::1 - tech_support [25/Jul/2025:10:33:30 +0000] "PUT /api/settings HTTP/1.1" 200 892 "https://settings.example.com" "Mozilla/5.0 (X11; Linux x86_64)"
172.16.0.50 - "john.doe@company.com" [25/Jul/2025:10:32:15 +0000] "DELETE /api/user/123 HTTP/1.1" 204 0 "https://admin.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
INVALID LOG LINE WITHOUT PROPER FORMAT
192.168.1.200 - api_user [25/Jul/2025:10:34:45 +0000] "GET /search?q=natural%20language%20processing&category=AI HTTP/1.1" 200 5678 "https://search.example.com/" "Python-urllib/3.9" """

        # Test parsing the complex log file
        print(f"\n=== Q7: Complex Log File Parsing (5 points) ===")
        print("Testing with challenging real-world log data...")
        
        try:
            result = parse_log_files(log_content)
            
            # Basic validation tests
            if not isinstance(result, list):
                print("❌ Function should return a list")
                self.test_results.append(("Q7", 0, 5, ["Function should return a list"]))
                self.max_score += 5
                return
            
            valid_entries = [entry for entry in result if isinstance(entry, dict) and 'ip' in entry]
            
            # Scoring based on how many valid entries were parsed
            total_valid_lines = 18  # Known valid log lines in the file (excluding comments and malformed)
            parsed_count = len(valid_entries)
            
            print(f"📊 Parsed {parsed_count} valid log entries out of ~{total_valid_lines} expected")
            
            if parsed_count == 0:
                score = 0
                feedback = "No valid log entries parsed. Check your regex pattern."
            elif parsed_count < 5:
                score = 1
                feedback = f"Basic parsing working but missing many entries ({parsed_count}/{total_valid_lines})"
            elif parsed_count < 10:
                score = 2
                feedback = f"Good progress! Handling some edge cases ({parsed_count}/{total_valid_lines})"
            elif parsed_count < 15:
                score = 3
                feedback = f"Very good! Handling most cases ({parsed_count}/{total_valid_lines})"
            elif parsed_count < total_valid_lines:
                score = 4
                feedback = f"Excellent! Almost complete ({parsed_count}/{total_valid_lines})"
            else:
                score = 5
                feedback = f"Perfect! All valid entries parsed ({parsed_count}/{total_valid_lines})"
            
            # Additional validation for structure
            if valid_entries:
                sample_entry = valid_entries[0]
                required_fields = ['ip', 'user', 'timestamp', 'method', 'path', 'status', 'size']
                missing_fields = [field for field in required_fields if field not in sample_entry]
                
                if missing_fields:
                    score = max(0, score - 1)
                    feedback += f" Missing required fields: {missing_fields}"
                
                # Check for IPv6 support
                ipv6_entries = [e for e in valid_entries if ':' in e.get('ip', '')]
                if ipv6_entries:
                    print("✅ IPv6 addresses detected - good job!")
                else:
                    print("⚠️  No IPv6 addresses found - check if you're handling 2001:db8::1 format")
                
                # Check for quoted usernames
                quoted_users = [e for e in valid_entries if e.get('user', '').startswith('"') and e.get('user', '').endswith('"')]
                if quoted_users:
                    print("✅ Quoted usernames detected - excellent!")
                else:
                    print("⚠️  No quoted usernames found - check handling of quoted user fields")
                
                print(f"📝 Sample parsed entry: {sample_entry}")
            
            print(f"Score: {score}/5 - {feedback}")
            self.total_score += score
            self.max_score += 5
            self.test_results.append(("Q7", score, 5, [feedback]))
            
        except Exception as e:
            print(f"❌ Error during testing: {str(e)}")
            self.test_results.append(("Q7", 0, 5, [f"Exception during testing: {str(e)}"]))
            self.max_score += 5

    def test_q8(self) -> None:
        """Test Q8: Basic tokenization (5 points)."""
        print(f"\n=== Q8: Basic Tokenization (5 points) ===")
        
        total_score = 0
        
        # Test whitespace_tokenize (1.5 points)
        whitespace_cases = [
            ("Hello world", ["Hello", "world"]),
            ("Hello,  world!", ["Hello,", "world!"]),
            ("  Hello   world  ", ["Hello", "world"]),
            ("", []),
            ("Single", ["Single"]),
        ]
        
        passed_ws = 0
        positive_ws_tests_passed = 0
        total_ws = len(whitespace_cases)
        
        try:
            whitespace_tokenize_func = globals()["whitespace_tokenize"]
            for i, (text, expected) in enumerate(whitespace_cases):
                try:
                    result = whitespace_tokenize_func(text)
                    if self.compare_results(result, expected):
                        passed_ws += 1
                        # Only count positive tests (non-empty expected results)
                        if expected:  # Non-empty list means positive test
                            positive_ws_tests_passed += 1
                    elif i < 5:  # Show first few failures
                        print(f"❌ Whitespace test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Whitespace test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function whitespace_tokenize not found!")
        
        # Only award points if student got at least one positive test case correct
        if positive_ws_tests_passed > 0:
            ws_score = (passed_ws / total_ws) * 1.5
        else:
            ws_score = 0.0
        print(f"Whitespace tokenization: {passed_ws}/{total_ws} passed ({ws_score:.1f}/1.5 points)")
        total_score += ws_score

        # Test punctuation_tokenize (1.5 points)
        punctuation_cases = [
            ("Hello, world!", ["Hello", ",", "world", "!"]),
            ("It's working.", ["It", "'", "s", "working", "."]),
            ("No punctuation", ["No", "punctuation"]),
            ("Multiple!!! marks???", ["Multiple", "!", "!", "!", "marks", "?", "?", "?"]),
        ]
        
        passed_punct = 0
        positive_punct_tests_passed = 0
        total_punct = len(punctuation_cases)
        
        try:
            punctuation_tokenize_func = globals()["punctuation_tokenize"]
            for i, (text, expected) in enumerate(punctuation_cases):
                try:
                    result = punctuation_tokenize_func(text)
                    if self.compare_results(result, expected):
                        passed_punct += 1
                        # Only count positive tests (non-empty expected results)
                        if expected:  # Non-empty list means positive test
                            positive_punct_tests_passed += 1
                    elif i < 5:  # Show first few failures
                        print(f"❌ Punctuation test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Punctuation test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function punctuation_tokenize not found!")
        
        # Only award points if student got at least one positive test case correct
        if positive_punct_tests_passed > 0:
            punct_score = (passed_punct / total_punct) * 1.5
        else:
            punct_score = 0.0
        print(f"Punctuation tokenization: {passed_punct}/{total_punct} passed ({punct_score:.1f}/1.5 points)")
        total_score += punct_score

        # Test sentence_tokenize (2 points)
        sentence_cases = [
            ("Hello world. How are you?", ["Hello world.", "How are you?"]),
            ("Single sentence", ["Single sentence"]),
            ("Dr. Smith went to U.S.A. yesterday.", ["Dr. Smith went to U.S.A. yesterday."]),
            ("First! Second? Third.", ["First!", "Second?", "Third."]),
        ]
        
        passed_sent = 0
        positive_sent_tests_passed = 0
        total_sent = len(sentence_cases)
        
        try:
            sentence_tokenize_func = globals()["sentence_tokenize"]
            for i, (text, expected) in enumerate(sentence_cases):
                try:
                    result = sentence_tokenize_func(text)
                    if self.compare_results(result, expected):
                        passed_sent += 1
                        # Only count positive tests (non-empty expected results)
                        if expected:  # Non-empty list means positive test
                            positive_sent_tests_passed += 1
                    elif i < 5:  # Show first few failures
                        print(f"❌ Sentence test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Sentence test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function sentence_tokenize not found!")
        
        # Only award points if student got at least one positive test case correct
        if positive_sent_tests_passed > 0:
            sent_score = (passed_sent / total_sent) * 2
        else:
            sent_score = 0.0
        print(f"Sentence tokenization: {passed_sent}/{total_sent} passed ({sent_score:.1f}/2.0 points)")
        total_score += sent_score
        
        self.total_score += total_score
        self.max_score += 5
        print(f"Q8 Total Score: {total_score:.1f}/5.0 points")
        self.test_results.append(("Q8", total_score, 5, [f"Whitespace: {passed_ws}/{total_ws}, Punctuation: {passed_punct}/{total_punct}, Sentence: {passed_sent}/{total_sent}"]))

    def test_q9(self) -> None:
        """Test Q9: Advanced tokenization (5 points)."""
        print(f"\n=== Q9: Advanced Tokenization (5 points) ===")
        
        # Test advanced_tokenize
        advanced_cases = [
            ("I can't believe it!", ["I", "ca", "n't", "believe", "it", "!"]),
            ("twenty-first century", ["twenty-first", "century"]),
            ("Visit www.example.com now", ["Visit", "www.example.com", "now"]),
            ("It's a don't-care situation.", ["It", "'s", "a", "don", "'t", "-", "care", "situation", "."]),
        ]
        
        passed_adv = 0
        total_adv = len(advanced_cases)
        
        try:
            advanced_tokenize_func = globals()["advanced_tokenize"]
            for i, (text, expected) in enumerate(advanced_cases):
                try:
                    result = advanced_tokenize_func(text)
                    if self.compare_results(result, expected):
                        passed_adv += 1
                    elif i < 5:  # Show first few failures
                        print(f"❌ Advanced test {i+1}: Expected {expected}, got {result}")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Advanced test {i+1}: Exception - {str(e)}")
        except KeyError:
            print("❌ Function advanced_tokenize not found!")
        
        adv_score = (passed_adv / total_adv) * 5.0
        print(f"Advanced tokenization: {passed_adv}/{total_adv} passed ({adv_score:.1f}/5.0 points)")
        
        self.total_score += adv_score
        self.max_score += 5
        print(f"Q9 Total Score: {adv_score:.1f}/5.0 points")
        self.test_results.append(("Q9", adv_score, 5, [f"Advanced: {passed_adv}/{total_adv}"]))

    def test_q10(self) -> None:
        """Test Q10: Basic text normalization (5 points)."""
        print(f"\n=== Q10: Basic Text Normalization (5 points) ===")
        
        # Test normalize_text - Simplified educational cases
        normalization_cases = [
            # Basic case conversion
            ("HELLO WORLD", "hello world"),
            ("MiXeD cAsE tExT", "mixed case text"),
            ("Simple text", "simple text"),
            
            # Basic accent removal (common cases only)
            ("café restaurant", "cafe restaurant"),
            ("naïve approach", "naive approach"),
            ("résumé review", "resume review"),
            ("São Paulo", "sao paulo"),
            
            # Basic punctuation removal (excessive only)
            ("Hello!!! How are you???", "hello how are you"),
            ("Text with... many dots", "text with many dots"),
            ("Multiple!!! Exclamation!!!", "multiple exclamation"),
            
            # Whitespace normalization
            ("  Extra   spaces   everywhere  ", "extra spaces everywhere"),
            ("Multiple\n\nNewlines", "multiple newlines"),
            ("Tabs\t\tand\t\tspaces", "tabs and spaces"),
            ("    Leading and trailing    ", "leading and trailing"),
            
            # Combined simple cases
            ("THE CAFÉ SERVES COFFEE!!!", "the cafe serves coffee"),
            ("RÉSUMÉ WITH QUALIFICATIONS!!!", "resume with qualifications"),
            
            # Simple edge cases
            ("", ""),
            ("   ", ""),
            ("A", "a"),
            ("123", "123"),
        ]
        
        passed_normalization = 0
        positive_normalization_tests_passed = 0
        total_normalization = len(normalization_cases)
        
        try:
            from tokenization import normalize_text
            for i, (text, expected) in enumerate(normalization_cases):
                try:
                    result = normalize_text(text)
                    if result == expected:
                        passed_normalization += 1
                        # Only count positive tests (non-empty expected results)
                        if expected:  # Non-empty string means positive test
                            positive_normalization_tests_passed += 1
                    elif i < 5:  # Show first few failures for debugging
                        print(f"❌ Normalization test {i+1}: Expected '{expected}', got '{result}'")
                except Exception as e:
                    if i < 5:
                        print(f"❌ Normalization test {i+1}: Exception - {str(e)}")
        except ImportError:
            print("❌ Function normalize_text not found!")
        
        # Only award points if student got at least one positive test case correct
        if positive_normalization_tests_passed > 0:
            normalization_score = (passed_normalization / total_normalization) * 5.0
        else:
            normalization_score = 0.0
        print(f"Text normalization: {passed_normalization}/{total_normalization} passed ({normalization_score:.1f}/5.0 points)")
        
        self.total_score += normalization_score
        self.max_score += 5
        print(f"Q10 Total Score: {normalization_score:.1f}/5.0 points")
        self.test_results.append(("Q10", normalization_score, 5, [f"Normalization: {passed_normalization}/{total_normalization}"]))

    def test_q11(self) -> None:
        """Test Q11: BPE (Byte Pair Encoding) Algorithm Implementation (15 points)"""
        print(f"\n=== Q11: BPE Algorithm Implementation (15 points) ===")
        
        try:
            from tokenization import BPETokenizer
        except ImportError:
            print("❌ Could not import BPETokenizer class from tokenization.py")
            self.test_results.append(("Q11", 0, 15, ["Could not import BPETokenizer class"]))
            self.max_score += 15
            return
        
        total_points = 0
        errors = []
        
        # Test case 1: Basic BPE training and tokenization (4.5 points)
        test1_points = 0
        try:
            corpus = ["hello world", "hello there", "world peace"]
            bpe = BPETokenizer(num_merges=20)
            bpe.train(corpus)
            
            # Check that merges were learned (1.5 points)
            merges = bpe.get_merges()
            if isinstance(merges, list) and len(merges) > 0:
                test1_points += 1.5
                print("  ✓ BPE training produces merges")
            else:
                errors.append("BPE training should produce a list of merges")
            
            # Check vocabulary structure (1.5 points)
            vocab = bpe.get_vocabulary()
            if isinstance(vocab, (set, list, dict)) and len(vocab) > 0:
                test1_points += 1.5
                print("  ✓ BPE training produces vocabulary")
            else:
                errors.append("BPE training should produce a vocabulary")
            
            # Test tokenization (1.5 points)
            tokens = bpe.tokenize("hello")
            if isinstance(tokens, list) and len(tokens) > 0:
                test1_points += 1.5
                print(f"  ✓ BPE tokenization works: 'hello' -> {tokens}")
            else:
                errors.append("BPE tokenization should return a list of tokens")
                
        except Exception as e:
            errors.append(f"Basic BPE test error: {e}")
        
        total_points += test1_points
        print(f"  Test 1 Score: {test1_points}/4.5 points")
        
        # Test case 2: Subword patterns (3.5 points)
        test2_points = 0
        try:
            corpus = ["playing played player", "running runner runs", "jumping jumper jumped"]
            bpe = BPETokenizer(num_merges=30)
            bpe.train(corpus)
            tokens = bpe.tokenize("player")
            
            if isinstance(tokens, list) and len(tokens) >= 1:
                test2_points += 2.0
                print(f"  ✓ Subword tokenization: 'player' -> {tokens}")
                
                # Check if common patterns were learned (1.5 points)
                token_str = " ".join(tokens)
                if any(pattern in token_str for pattern in ["play", "er", "ed", "ing"]):
                    test2_points += 1.5
                    print("  ✓ Common subword patterns detected")
                else:
                    errors.append("Expected common subword patterns (play, er, ed, ing)")
            else:
                errors.append("Subword tokenization failed")
                
        except Exception as e:
            errors.append(f"Subword test error: {e}")
        
        total_points += test2_points
        print(f"  Test 2 Score: {test2_points}/3.5 points")
        
        # Test case 3: Vocabulary size constraint (3.0 points)
        test3_points = 0
        try:
            corpus = ["the cat sat on the mat", "the dog ran in the park"]
            bpe = BPETokenizer(num_merges=15)
            bpe.train(corpus)
            
            vocab = bpe.get_vocabulary()
            merges = bpe.get_merges()
            
            vocab_count = len(vocab) if isinstance(vocab, (set, list)) else len(list(vocab.keys())) if isinstance(vocab, dict) else 0
            
            # Check that merges don't exceed the limit (1.5 points)
            if len(merges) <= 15:
                test3_points += 1.5
                print(f"  ✓ Merge limit respected: {len(merges)} <= 15")
            else:
                errors.append(f"Too many merges: {len(merges)} > 15")
            
            # Test that algorithm stops appropriately (1.5 points)
            if len(merges) < 100:  # Reasonable number of merges
                test3_points += 1.5
                print(f"  ✓ Reasonable number of merges: {len(merges)}")
            else:
                errors.append("Too many merges generated")
                
        except Exception as e:
            errors.append(f"Vocabulary constraint test error: {e}")
        
        total_points += test3_points
        print(f"  Test 3 Score: {test3_points}/3.0 points")
        
        # Test case 4: Edge cases (4.0 points)
        test4_points = 0
        try:
            # Empty corpus (1.0 point)
            try:
                bpe = BPETokenizer(num_merges=10)
                bpe.train([])
                merges = bpe.get_merges()
                if len(merges) == 0:
                    test4_points += 1.0
                    print("  ✓ Empty corpus handled")
                else:
                    errors.append("Empty corpus should produce no merges")
            except:
                errors.append("Empty corpus not handled gracefully")
            
            # Single character words (1.0 point)
            try:
                corpus = ["a b c", "a a b", "c c c"]
                bpe = BPETokenizer(num_merges=10)
                bpe.train(corpus)
                tokens = bpe.tokenize("a")
                if isinstance(tokens, list):
                    test4_points += 1.0
                    print("  ✓ Single character handling")
                else:
                    errors.append("Single character tokenization failed")
            except:
                errors.append("Single character case not handled")
            
            # Unknown word tokenization (2.0 points)
            try:
                corpus = ["hello world"]
                bpe = BPETokenizer(num_merges=10)
                bpe.train(corpus)
                tokens = bpe.tokenize("goodbye")  # New word
                if isinstance(tokens, list) and len(tokens) > 0:
                    test4_points += 2.0
                    print(f"  ✓ Unknown word tokenization: 'goodbye' -> {tokens}")
                else:
                    errors.append("Unknown word tokenization failed")
            except:
                errors.append("Unknown word case not handled")
                
        except Exception as e:
            errors.append(f"Edge cases test error: {e}")
        
        total_points += test4_points
        print(f"  Test 4 Score: {test4_points}/4.0 points")
        
        # Record results
        self.test_results.append(("Q11", total_points, 15, errors))
        self.total_score += total_points
        self.max_score += 15
        
        print(f"Q11 Score: {total_points}/15 points")
        if errors:
            print("Issues found:")
            for error in errors[:3]:  # Show first 3 errors
                print(f"  - {error}")
    
    def test_q12(self) -> None:
        """Test Q12: Edit Distance Applications (10 points)"""
        print(f"\n=== Q12: Edit Distance Applications (10 points) ===")
        
        try:
            from tokenization import levenshtein_distance, spell_check, name_matching
        except ImportError:
            print("❌ Could not import edit distance functions from tokenization.py")
            self.test_results.append(("Q12", 0, 8, ["Could not import edit distance functions"]))
            self.max_score += 8
            return
        
        total_points = 0
        errors = []
        
        # Test 1: Basic Levenshtein distance (3 points)
        print("  Testing basic Levenshtein distance...")
        basic_tests = [
            ("kitten", "sitting", 3),
            ("saturday", "sunday", 3),
            ("", "abc", 3),
            ("abc", "", 3),
            ("same", "same", 0),
            ("a", "b", 1),
            ("intention", "execution", 5)
        ]
        
        basic_score = 0
        for word1, word2, expected in basic_tests:
            try:
                result = levenshtein_distance(word1, word2)
                if result == expected:
                    basic_score += 1
                else:
                    errors.append(f"levenshtein_distance('{word1}', '{word2}') = {result}, expected {expected}")
            except Exception as e:
                errors.append(f"Error in levenshtein_distance('{word1}', '{word2}'): {e}")
        
        if basic_score >= 6:  # 6 out of 7 correct
            total_points += 2.4
            print(f"  ✓ Basic Levenshtein distance: {basic_score}/7 tests passed")
        elif basic_score >= 4:
            total_points += 1.6
            print(f"  ◐ Basic Levenshtein distance: {basic_score}/7 tests passed")
        elif basic_score >= 2:
            total_points += 0.8
            print(f"  ◑ Basic Levenshtein distance: {basic_score}/7 tests passed")
        else:
            print(f"  ✗ Basic Levenshtein distance: {basic_score}/7 tests passed")
        
        # Test 2: Spell checking (4 points)
        print("  Testing spell checking application...")
        
        # Load dictionary
        import os
        dict_path = os.path.join(os.path.dirname(__file__), 'data', 'english_words.txt')
        dictionary = []
        
        try:
            with open(dict_path, 'r', encoding='utf-8') as f:
                dictionary = [line.strip().lower() for line in f if line.strip()]
        except FileNotFoundError:
            # Fallback dictionary
            dictionary = ["the", "cat", "sat", "mat", "dog", "ran", "park", "receive", "believe", 
                         "separate", "definitely", "necessary", "occurred", "beginning"]
        
        spell_tests = [
            ("teh", ["the", "tea", "ten"], "the"),
            ("recieve", ["receive", "deceive", "believe"], "receive"),
            ("seperate", ["separate", "desperate", "generate"], "separate"),
            ("definately", ["definitely", "fortunately", "unfortunately"], "definitely"),
            ("occured", ["occurred", "obscured", "procured"], "occurred"),
            ("begining", ["beginning", "begging", "belonging"], "beginning"),
            ("neccessary", ["necessary", "unnecessary", "accessory"], "necessary")
        ]
        
        spell_score = 0
        for misspelled, candidates, expected in spell_tests:
            try:
                result = spell_check(misspelled, candidates)
                if result == expected:
                    spell_score += 1
                    print(f"    ✓ '{misspelled}' -> '{result}'")
                else:
                    errors.append(f"spell_check('{misspelled}') = '{result}', expected '{expected}'")
                    print(f"    ✗ '{misspelled}' -> '{result}' (expected '{expected}')")
            except Exception as e:
                errors.append(f"Error in spell_check('{misspelled}'): {e}")
        
        if spell_score >= 6:
            total_points += 3.2
        elif spell_score >= 4:
            total_points += 2.4
        elif spell_score >= 2:
            total_points += 1.6
        elif spell_score >= 1:
            total_points += 0.8
        
        print(f"    Spell checking: {spell_score}/7 tests passed")
        
        # Test 3: Name matching (3 points)
        print("  Testing name matching application...")
        
        name_tests = [
            ("John Smith", ["Jon Smith", "John Smyth", "Jane Smith"], "Jon Smith"),
            ("McDonald", ["MacDonald", "McDonnell", "MacLeod"], "MacDonald"),
            ("Catherine", ["Katherine", "Katharine", "Cathryn"], "Katherine"),
            ("Steven", ["Stephen", "Stefan", "Stewart"], "Stephen"),
            ("Mohammad", ["Mohammed", "Muhammad", "Mohamed"], "Mohammed"),
            ("Elisabeth", ["Elizabeth", "Elisabet", "Elspeth"], "Elizabeth")
        ]
        
        name_score = 0
        for query, candidates, expected in name_tests:
            try:
                result = name_matching(query, candidates)
                if result == expected:
                    name_score += 1
                    print(f"    ✓ '{query}' -> '{result}'")
                else:
                    # Check if result is reasonable (close distance)
                    try:
                        query_dist = levenshtein_distance(query, result) if result else float('inf')
                        expected_dist = levenshtein_distance(query, expected)
                        if query_dist <= expected_dist + 1:  # Allow some flexibility
                            name_score += 0.5
                            print(f"    ◐ '{query}' -> '{result}' (acceptable alternative)")
                        else:
                            print(f"    ✗ '{query}' -> '{result}' (expected '{expected}')")
                    except:
                        print(f"    ✗ '{query}' -> '{result}' (expected '{expected}')")
                        
            except Exception as e:
                errors.append(f"Error in name_matching('{query}'): {e}")
        
        if name_score >= 5:
            total_points += 2.4
        elif name_score >= 3:
            total_points += 1.6
        elif name_score >= 1:
            total_points += 0.8
        
        print(f"    Name matching: {name_score}/6 tests passed")
        
        # Record results
        self.test_results.append(("Q12", total_points, 8, errors))
        self.total_score += total_points
        self.max_score += 8
        
        print(f"Q12 Score: {total_points}/8 points")
        if errors:
            print("Issues found:")
            for error in errors[:3]:  # Show first 3 errors
                print(f"  - {error}")

    def print_final_results(self) -> None:
        """Print final test results and score."""
        print("\n" + "=" * 50)
        print("FINAL RESULTS")
        print("=" * 50)
        
        for func_name, score, max_points, errors in self.test_results:
            status = "✅ PASS" if score == max_points else "❌ FAIL"
            print(f"{func_name}: {score}/{max_points} {status}")
            
        print(f"\nOverall Score: {self.total_score}/{self.max_score}")
        percentage = (self.total_score / self.max_score * 100) if self.max_score > 0 else 0
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            print("🎉 Excellent work!")
        elif percentage >= 80:
            print("👍 Good job!")
        elif percentage >= 70:
            print("👌 Not bad, but room for improvement.")
        else:
            print("📚 Keep working - you can do this!")


def main():
    """Main function to run the autograder."""
    import argparse
    
    parser = argparse.ArgumentParser(description='MAI 5201 HW0 Autograder')
    parser.add_argument('-q', '--question', help='Test specific question (e.g., q1, q2)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    grader = AutoGrader()
    
    if args.question:
        # Test specific question
        question_map = {
            'q1': grader.test_q1,
            'q2': grader.test_q2,
            'q3': grader.test_q3,
            'q4': grader.test_q4,
            'q5': grader.test_q5,
            'q6': grader.test_q6,
            'q7': grader.test_q7,
            'q8': grader.test_q8,
            'q9': grader.test_q9,
            'q10': grader.test_q10,
            'q11': grader.test_q11,
            'q12': grader.test_q12,
        }
        
        if args.question in question_map:
            print(f"Testing {args.question.upper()}...")
            question_map[args.question]()
            grader.print_final_results()
        else:
            print(f"Unknown question: {args.question}")
            print("Available questions: q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12")
    else:
        # Run all tests
        grader.run_all_tests()


if __name__ == "__main__":
    main()
