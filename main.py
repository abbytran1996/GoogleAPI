
import settings
import numpy
from data_access import create_company, list_companies, create_job, list_jobs, search_jobs
from uuid import uuid4


PROJECT_ID = 'recruitrtest-256719'
project_id = 'projects/' + PROJECT_ID
jobDescription = 'Code high-volume software using primarily C++ and Java. Create web applications using primarily PHP. Implement web interfaces using XHTML, CSS, and JavaScript. Build report interfaces and data feeds'
UXJobDescription1='Design and user experience (UX) are at the forefront of everything we do. The job of a Designer is to envision how people experience our products and bring that vision to life in a way that feels inspired, refined and even magical. In a Designer role, you’ll address complex tasks and transform them into intuitive, accessible and easy-to-use solutions for billions of people around the world—from the first-time user to the sophisticated expert. Achieving this goal requires collaboration with teams of other Designers, Researchers, Engineers and Product Managers throughout the design process—from creating user flows and wireframes to building user interface mockups and prototypes. At each stage, you will anticipate what our users need, advocate for them and ensure that the final product surprises and delights them'
UXJobDescription2='Perform responsibilities which vary by project area. Interaction: Produce and test interaction flows and mocks, using research to accurately communicate product functionality to the team. Understand web and/or mobile environments such as HTML, CSS, JavaScript, Android UI, and iOS UI, to further enhance the overall experience. Visual: Produce designs that reflect a visual design language or brand guidelines. Understand typography, color, grid, and composition. Demonstrate best practices for production considerations and methods. Execute a range of styles with a consistent, but unrestricting, aesthetic personality/voice. Motion: Create motion studies for enhancing usability, interaction, storytelling, and delight. Work with partners and product managers to ideate and define, with engineering to integrate explorations into product experiences, and with research to inform user experiences'
degreeType = 'BACHELORS_OR_EQUIVALENT'
skills = ['perl', 'java', 'php', 'python', 'c++']
skills1 = ['perl', 'java', 'php', 'python', 'c++', 'High levels of creativity', 'quick problem-solving capabilities', 'software engineering experience from previous internship']
employmentType = 'INTERN'
qualifications = 'perl, java, php, python, c++'
qualifications1 = 'perl, java, php, python, c++, High levels of creativity, quick problem-solving capabilities, software engineering experience from previous internship'
qualifications2 = '1 or more years of experience with perl, java, php, python, or c++. Must be currently enrolled in a full-time, degree-seeking program and in the process of obtaining a Bachelors or Masters degree in Computer Science or a related field. Must obtain work authorization in country of employment at the time of hire, and maintain ongoing work authorization during employment. Demonstrated software engineering experience from previous internship, work experience, coding competitions, or publications. Intent to return to degree-program after the completion of the internship/co-op. High levels of creativity and quick problem-solving capabilities'

def main():      
    '''
    def create_company(project_id, display_name, external_id):
    '''
    # Example: create_company(PROJECT_ID, 'Amazon', str(uuid4()))
    # Example: list_companies(PROJECT_ID)

    '''
    create_job(project_id, company_name, requisition_id, title, description, job_application_url, addresses, language_code, skills, degree_type)
    
    Below are the jobs that I have created
    '''
    # JOB1: Facebook
    # create_job(PROJECT_ID, 'projects/recruitrtest-256719/tenants/075e3c6b-df00-0000-0000-00fbd63c7ae0/companies/fa8e59c6-dd47-4b8a-822b-6e77aab6b217', str(uuid4()), 'Software Engineer', 'Software Engineer', 'https://www.facebook.com/careers/jobs/2350871135127906/', ['Boston, MA', 'New York, NY'], 'en-US', required_skills=['Java','Python'], recommended_skills=['Ruby','PHP'], gpa=int(3.2), company_size='small', degree_type=degreeType, employment_type=employmentType)

    # JOB2: Apple
    # create_job(PROJECT_ID, 'projects/recruitrtest-256719/tenants/075e3c6b-df00-0000-0000-00fbd63c7ae0/companies/c221fb6d-9b33-47da-93d2-f455aed66df7', str(uuid4()), 'Software Engineer', 'Software Engineer', 'https://www.apple.com/jobs/us/', ['Seattle, WA', 'New York, NY'], 'en-US', required_skills=['Java','Python', 'PHP'], recommended_skills=['Ruby','JavaScript'], gpa=int(3.4), company_size='large', degree_type=degreeType, employment_type=employmentType)
   
    # JOB3: Amazon
    # create_job(PROJECT_ID, 'projects/recruitrtest-256719/tenants/075e3c6b-df00-0000-0000-00fbd63c7ae0/companies/2cd2df30-fdbe-43ff-ab62-78245c6c5fe2', str(uuid4()), 'Software Engineer Intern', 'Software Engineer', 'https://www.amazon.jobs/en', ['San Francisco, CA'], 'en-US', required_skills=['Java'], recommended_skills=['Ruby'], gpa=int(3.0), company_size='medium', degree_type=degreeType, employment_type=employmentType)
   
    # JOB4: Google
    # create_job(PROJECT_ID, 'projects/recruitrtest-256719/tenants/075e3c6b-df00-0000-0000-00fbd63c7ae0/companies/486e5d0a-1619-4248-a7ed-23ea222f707e', str(uuid4()), 'User Experience Designer', UXJobDescription1, 'https://careers.google.com/jobs/', ['San Francisco, CA'], 'en-US', required_skills=['Photoshop', 'Illustrator'], recommended_skills=['After Effects'], gpa=int(3.2), company_size='large', degree_type=degreeType, employment_type=employmentType)
   

    '''
    def search_jobs(project_id, query, skills, gpa, locations, company_size, industry):

    Below is a query that I have tested
    '''
    # Query 1: Matching more than 2 skills
    query='Software Engineer'
    skills=['java','python']
    gpa=3.2
    locations = ['Boston, MA', 'New York, NY']
    company_size = 'large'
    industry = 'SOFTWARE'

    response = search_jobs(project_id, query, skills, gpa, locations, company_size, industry)
    f = open("search_results.txt", "a")
    f.write(str(response))
    f.close()

if __name__ == '__main__':
    main()
