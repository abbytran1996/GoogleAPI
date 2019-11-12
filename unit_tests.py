import unittest
from data_access import create_company, list_companies, create_job, list_jobs, search_jobs
from runner import HTMLTestRunner

PROJECT_ID = 'recruitrtest-256719'
project_id = 'projects/' + PROJECT_ID
query_software='Software Engineer'
query_designer='Designer'
skills_software=['java','python']
skills_designer=['photoshop']
gpa=3.3
locations = ['Boston, MA', 'New York, NY']
company_size = 'large'
industry = 'SOFTWARE'

class TestStringMethods(unittest.TestCase):
    

    def test_matching_skills_software(self):
        response = search_jobs(project_id, query_software, skills_software, None, None, None, industry)
        jobs = response['matchingJobs']
        
        for item in jobs:
            job = item['job']
            required_skills = job['customAttributes']['required_skills']['stringValues']
            required_skills = list(map(str.lower,required_skills))
            print('Required Skills: ', required_skills)
            flag = False
            for skill in skills_software:
                if (skill in required_skills):
                    flag = True
                    break
            self.assertEqual(flag, True)

    def test_matching_skills_designer(self):
        response = search_jobs(project_id, query_designer, skills_designer, None, None, None, industry)
        jobs = response['matchingJobs']
        
        for item in jobs:
            job = item['job']
            required_skills = job['customAttributes']['required_skills']['stringValues']
            required_skills = list(map(str.lower,required_skills))
            print('Required Skills: ', required_skills)
            flag = False
            for skill in skills_designer:
                if (skill in required_skills):
                    flag = True
                    break
            self.assertEqual(flag, True)

    # def test_matching_gpa(self):
    #     response = search_jobs(project_id, query_software, skills_software, gpa, locations, company_size, industry)
    #     jobs = response['matchingJobs']
        
    #     for item in jobs:
    #         job = item['job']
    #         if ('longValues' not in list(job['customAttributes']['gpa'].keys())):
    #             continue
    #         matched_gpa = float(job['customAttributes']['gpa']['longValues'][0])
    #         print('GPA: ', matched_gpa)
    #         self.assertEqual(gpa >= matched_gpa, True)
    
    # def test_matching_location(self):
    #     response = search_jobs(project_id, query_software, skills_software, None, locations, None, industry)
    #     jobs = response['matchingJobs']
        
    #     for item in jobs:
    #         job = item['job']
    #         matched_locations = job['addresses']
    #         flag = False
    #         for location in locations:
    #              if (location in matched_locations):
    #                  flag = True
    #                  break
    #         self.assertEqual(flag, True)

    # def test_matching_company_size(self):
    #     response = search_jobs(project_id, query_software, skills_software, gpa, locations, company_size, industry)
    #     jobs = response['matchingJobs']
        
    #     for item in jobs:
    #         job = item['job']
    #         matched_company_size = job['customAttributes']['company_size']['stringValues'][0]
    #         print('Company Size: ', matched_company_size)
    #         self.assertEqual(company_size, matched_company_size)
    

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='report'))