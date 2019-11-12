from google.cloud import talent_v4beta1
from google.cloud.talent_v4beta1.types import CustomAttribute
from uuid import uuid4
from googleapiclient.discovery import build

import six
import numpy
import os


request_metadata = {
    'domain':     'example.com',
    # I created these two ids by "str(uuid4())". They just have to be unique for each user. I think you can use these ids too or create new ones for youself
    'session_id': '8bcf3333-8aa7-4de5-a327-ea93b14421a6',
    'user_id':    '6cf88899-096f-4003-82e7-f3a26c242dd0',
}

# project_id = 'Your Google Cloud Project ID'
# display_name = 'My Company Name'
# external_id = 'Identifier of this company in my system'
def create_company(project_id, display_name, external_id):
    """Create Company"""

    client = talent_v4beta1.CompanyServiceClient()

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(display_name, six.binary_type):
        display_name = display_name.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')

    parent = client.project_path(project_id)
    company = {'display_name': display_name, 'external_id': external_id}

    response = client.create_company(parent, company)

    # Save all the companies in companies.txt
    # Save these fields: external_id, display_name, name
    companies = open("companies.txt", "a")
    numpy.savetxt(companies, [[external_id, display_name, response.name]], fmt='%s', delimiter=' ', header="external_id,display_name,name")
    companies.close()

    print(response)
    print('Created Company')
    print('Name: {}'.format(response.name))
    print('Display Name: {}'.format(response.display_name))
    print('External ID: {}'.format(response.external_id))

# project_id = 'Your Google Cloud Project ID'
def list_companies(project_id):
    """List Companies"""

    client = talent_v4beta1.CompanyServiceClient()

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    parent = client.project_path(project_id)

    companies = open("companies.txt", "a")
    # Iterate over all results
    for response_item in client.list_companies(parent):
        externalIds, displayNames, names = numpy.genfromtxt('companies.txt', unpack=True, dtype='str', delimiter=' ')
        # If the company is not in the file yet, save it
        if (response_item.external_id not in externalIds):
            numpy.savetxt(companies, [[response_item.external_id, response_item.display_name, response_item.name]], fmt='%s', delimiter=' ', header="external_id,display_name,name")
        print('Company Name: {}'.format(response_item.name))
        print('Display Name: {}'.format(response_item.display_name))
        print('External ID: {}'.format(response_item.external_id))
    companies.close()

# project_id = 'Your Google Cloud Project ID'
# company_name = 'Company names returned from the API when created the companies, e.g. projects/your-project/companies/company-id'
# requisition_id = 'Job requisition ID, aka Posting ID. Unique per job.'. I just created these by "str(uuid4())"
# title = 'The job title'
# description = 'This is a description of this job'
# job_application_url = 'https://www.example.org/job-posting/123'
# addresses = List of strings: ['1600 Amphitheatre Parkway, Mountain View, CA 94043','111 8th Avenue, New York, NY 10011']
# language_code = 'en-US'
# required_skills = List of strings: ['Python', 'Java']
# recommended_skills = List of strings: ['Ruby', 'PHP']
# gpa = float number
# company_size = one of these strings: small, medium, large. These are my own conventions because we have company_size as a criteria in our app.
# degree_type = enum: https://cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4beta1#google.cloud.talent.v4beta1.DegreeType
# employment_type = enum: https://cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4beta1#employmenttype
def create_job(project_id, company_name, requisition_id,
                      title, description, job_application_url, addresses,
                      language_code, required_skills, recommended_skills, gpa, company_size, degree_type, employment_type):
    """Create Job"""

    client = talent_v4beta1.JobServiceClient()

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(company_name, six.binary_type):
        company_name = company_name.decode('utf-8')
    if isinstance(requisition_id, six.binary_type):
        requisition_id = requisition_id.decode('utf-8')
    if isinstance(title, six.binary_type):
        title = title.decode('utf-8')
    if isinstance(description, six.binary_type):
        description = description.decode('utf-8')
    if isinstance(job_application_url, six.binary_type):
        job_application_url = job_application_url.decode('utf-8')
    if isinstance(addresses, six.binary_type):
        addresses = addresses.decode('utf-8')
    if isinstance(language_code, six.binary_type):
        language_code = language_code.decode('utf-8')
    if isinstance(required_skills, six.binary_type):
        required_skills = required_skills.decode('utf-8')
    if isinstance(recommended_skills, six.binary_type):
        recommended_skills = recommended_skills.decode('utf-8')
    if isinstance(gpa, six.binary_type):
        gpa = gpa.decode('utf-8')
    if isinstance(company_size, six.binary_type):
        company_size = company_size.decode('utf-8')
    if isinstance(degree_type, six.binary_type):
        skills = degree_type.decode('utf-8')

    parent = client.project_path(project_id)
    uris = [job_application_url]
    application_info = {'uris': uris}

    job = {
        'company': company_name,
        'requisition_id': requisition_id,
        'title': title,
        'description': description,
        'application_info': application_info,
        'addresses': addresses,
        'language_code': language_code,
        'custom_attributes': {
            'required_skills' : CustomAttribute(
                        string_values=required_skills,
                        filterable=True),
            'recommended_skills': CustomAttribute(
                        string_values=recommended_skills,
                        filterable=True),
            'gpa': CustomAttribute(
                        long_values=[gpa],
                        filterable=True),
            'company_size': CustomAttribute(
                        string_values=[company_size],
                        filterable=True),
        },
        'degree_types': [client.enums.DegreeType[degree_type]],
        'employment_types': [client.enums.EmploymentType[employment_type]]
    }

    response = client.create_job(parent, job)

    # Save all jobs in 'jobs.txt'
    # Save these fields: title, name, company, requisition_id
    jobs = open("jobs.txt", "a")
    numpy.savetxt(jobs, [[response.title,response.name, response.company, response.requisition_id]], fmt='%s', delimiter=' ', header="title,name,company,requisition")
    jobs.close() 

    print('Created job: {}'.format(response))

# This does not work yet... Somehow I got an error about my project ID
# project_id = 'Your Google Cloud Project ID'
# filter_ = 'companyName=projects/my-project/companies/company-id'
def list_jobs(project_id, filter_):
    """List Job"""

    client = talent_v4beta1.JobServiceClient()

    

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(filter_, six.binary_type):
        filter_ = filter_.decode('utf-8')
    parent = client.project_path(project_id)

    # Iterate over all results
    for response_item in client.list_jobs(parent, filter_):
        print('Job name: {}'.format(response_item.name))
        print('Job requisition ID: {}'.format(response_item.requisition_id))
        print('Job title: {}'.format(response_item.title))
        print('Job description: {}'.format(response_item.description))

# This does not work yet... Somehow I got an error about my project ID
# project_id = 'Your Google Cloud Project ID'
# job_id = Your job id that you want to get info of
def sample_get_job(project_id, job_id):
    """Get Job"""

    client = talent_v4beta1.JobServiceClient()

    if isinstance(job_id, six.binary_type):
        job_id = job_id.decode('utf-8')
    name = client.job_path(project_id,'tentants', job_id)

    response = client.get_job(name)
    print('Job name: {}'.format(response.name))
    print('Requisition ID: {}'.format(response.requisition_id))
    print('Title: {}'.format(response.title))
    print('Description: {}'.format(response.description))
    print('Posting language: {}'.format(response.language_code))
    for address in response.addresses:
        print('Address: {}'.format(address))
    for email in response.application_info.emails:
        print('Email: {}'.format(email))
    for website_uri in response.application_info.uris:
        print('Website: {}'.format(website_uri))

# Search for jobs based on the job query
# project_id = Your Google Project Id
# query = The query string that matches against the job title, description, and location fields.
# skills = A list of skills that the user put in
# gpa = User's GPA
# locations = A list of locations
# company_size = 'small', 'medium' or 'large'. Match against a customAttribute named 'company_size'
# industry = Match against the field in Job, I still need to figure out how
def search_jobs(project_id, query, skills, gpa, locations, company_size, industry):
    client = talent_v4beta1.JobServiceClient()
    client_service = build('jobs', 'v4beta1')

    # TODO: For now I just OR everthing, but we later on need to find a way to enforce required_skills
    # Example of a query: 
    # 'LOWER(required_skills)="java" OR LOWER(required_skills)="python" OR LOWER(required_skills)="php"'
    # Construct query string for required_skills
    custom_query = '((LOWER(required_skills)='
    for skill in skills[0:-1]:
        custom_query += '"' + skill.lower() + '" OR LOWER(required_skills)='
    custom_query += '"' + (skills[-1]).lower() + '") OR '

    # Construct query string for recommended_skills
    custom_query += '(LOWER(recommended_skills)='
    for skill in skills[0:-1]:
        custom_query += '"' + skill.lower() + '" OR LOWER(recommended_skills)='
    custom_query += '"' + (skills[-1]).lower() + '"))'

    # Construct query string for GPA
    if (gpa != None):
        custom_query += ' AND ( gpa <= 3 )'

    # Construct query string for company_size
    if (company_size != None):
        custom_query += ' AND ( company_size = "' + company_size +'" )'

    print('Skills query string: ', custom_query)

    # Add location to query string
    if (locations != None):
        for location in locations:
            query += ' ' + location
    print('Query string: ', query)

    # TODO: Add gpa, locations, company_size, industry to job_query 
    job_query = {
        'query': query,
        'queryLanguageCode': 'en-US',
        'customAttributeFilter': custom_query
    }
    order_by = 'relevance desc'

    # This is not used yet. Should test to see if it actually makes CustomRankingInfo more weighted
    importance_level = client.enums.SearchJobsRequest.CustomRankingInfo.ImportanceLevel.EXTREME
    ranking_expression = '(skills + 25) * 0.75'
    custom_ranking_info = {
        'importance_level': importance_level,
        'ranking_expression': ranking_expression
    }
    
    # Request for the job search
    request = {
        'request_metadata': request_metadata,
        'job_query': job_query,
        'order_by': order_by
    }
    response = client_service.projects().jobs().search(
        parent=project_id, body=request).execute()

    # Inspect the results
    if response.get('matchingJobs') is not None:
        print('Job matched: {}'.format(response))
        print('Search Results:')
        for job in response.get('matchingJobs'):
            print('%s: %s' % (job.get('job').get('title'),
                                job.get('searchTextSnippet')))
    else:
        print('No Job Results')
    
    return response