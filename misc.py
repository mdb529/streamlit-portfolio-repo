from classes import Project

print('BEGIN...\n')



# profile_projects = [
#     {
#         'summary':
#         {
#             'name': 'ACO "Holy Grail" Report',
#             'company': 'Michigan Healthcare Professionals',
#             'period_start': '2017',
#             'period_end': '2018',
#             'high_level_overview': 'Analyst at largest provider group in MI; needed analytics to drive decision making'
#         },
#         'details':
#         {
#             'context': 'Recent graduate less than a month on the job with no healthcare experience.',
#             'problem': 'CEO presented me with what he called a "Holy Grail" report: pct of procedures that were referred within vs out of the company.',
#             'action': 'Built first data warehouse using AWS Redshift, provided CEO with medical group referral patterns',
#             'result': 'Network referral leakage rates plummeted, utilization costs decreased.',
#             'skills_and_technologies': 'Modeling'
#         }
#     },
#     {
#         'summary':
#         {
#             'name': 'ACO Program Performance',
#             'company': 'Michigan Healthcare Professionals',
#             'period_start': '2017',
#             'period_end': '2018',
#             'high_level_overview': 'Analyst at largest provider group in MI; needed analytics to drive decision making'
#         },
#         'details':
#         {
#             'context': 'Recent graduate less than a month on the job with no healthcare experience.',
#             'problem': 'CEO presented me with what he called a "Holy Grail" report: pct of procedures that were referred within vs out of the company.',
#             'action': 'Built first data warehouse using AWS Redshift, provided CEO with medical group referral patterns',
#             'result': 'Network referral leakage rates plummeted, utilization costs decreased.',
#             'skills_and_technologies': 'Modeling'
#         }
#     }
# ]


# project_list = [p['summary']['name'] for p in profile_projects]
# for p in profile_projects:
#     summary = p['summary']
#     details = p['details']

#     print(type(details))

#     project = Project(summary,details)

#     summary_df = project.create_summary_df()
#     details_df = project.create_details_df()

#     print(summary_df)


print('\n...END')