import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from classes import Project
from PIL import Image
import base64
from pathlib import Path

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
# count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")


st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)



profile_projects = [
    {
    # ACO Network Referral Leakage Report
        'summary':
        {
            'name': 'ACO Network Referral Leakage Report',
            'company': 'Michigan Healthcare Professionals',
            'period_start': '2017',
            'period_end': '2018',
            'high_level_overview': '''
    • One man data team at largest provider group in MI; needed analytics to drive decision making
    • CEO approached with "Holy Grail" ACO network referral leakage report request
    • Built data warehouse, generated actionable "report card" reports for 500+ doctors, promoting change in referral patterns
            '''
        },
        'details':
        {
            'context': '''
                    • Recent graduate less than a month on the job with no healthcare experience.

                    • Sole analyst at Michigan Healthcare Professionals
            ''',
            'problem': '''
                    • CEO presented me with a request for a Network Referral Leakage report: % of procedures that were referred within vs out of the company.

                    • Akin to vertical integration, keeping referrals in-house resulted in lower costs for patients and payers. This would have a massive impact on the bottom line.
            ''',
            'action': '''
                    • Built first data warehouse using AWS Redshift, provided CEO with medical group's referral patterns.

                    • Equipped Board of Directors with data to go to underperforming doctors and implement change.
            ''',
            'result': '''
                • Network referral leakage rates plummeted, utilization costs decreased.
            ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Dimensional Modeling
                Technologies:\n
                    • AWS Redshift
                    • Tableau
            '''
        }
    },
    {
    # ACO Program Performance
        'summary':
        {
            'name': 'ACO Program Performance',
            'company': 'Michigan Healthcare Professionals',
            'period_start': '2018',
            'period_end': '2020',
            'high_level_overview': '''
    • Managed analytics for a 500+ provider Medicare ACO, administered Medicare MIPS program
    • Realized key to success was effectively documenting patient risk
    • Generated analytics, deliverables to enable providers to document more effectively
            '''
        },
        'details':
        {
            'context': '''
                    • Managed analytics for large, 500+ provider Accountable Care Organization (ACO)
            ''',
            'problem': '''
                    • Needed to ensure ACO performed successfully, unsure how to affect change.

                    • Wanted to understand how to improve ACO's performance
            ''',
            'action': '''
                    • Read thru Medicare ACO legislation, discovered key to success documenting patient risk.

                    • Used analytics to help doctors identify and close gaps in patient care. 
            ''',
            'result': '''
                    • Implemented analytics-driven workflow to improve patient documentation, increasing chance of ACO\'s success in the future
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Business Process Design
                Technologies:\n
                    • Tableau
                    • Python
                    • Excel
            '''
        }
    },

    {
    # $1M Drug Underpayment Recovery      
        'summary':
        {
            'name': '$1M Drug Underpayment Recovery',
            'company': 'Michigan Healthcare Professionals',
            'period_start': '2019',
            'period_end': '2019',
            'high_level_overview': '''
    • Wanted to apply profit equation to drug reimbursement
    • Discovered massive series of drug underpayments by payer
    • Negotiated, won a $1M check for underpayment, representing years' worth of back-pay
            '''
        },
        'details':
        {
            'context': '''
                    • Co-managed the purchasing and rebate contracting for chemotherapy drugs, amounting to over $100M annually.
            ''',
            'problem': '''
                    • Wanted to apply "profit = revenue - expenses" formula to Healthcare.

                    • Found it very difficult, as industry is extremely opaque
            ''',
            'action': '''
                    • Discovered that a payer had been systemically underpaying for years

                    • Notified payer of underpayment and its magnitude.

                    • Engaged in back-and-forth negotiation with payer.
            ''',
            'result': '''
                    • Negotiated, won a $1M check for underpayment, representing years' worth of back-pay
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Negotiating
                Technologies:\n
                    • AWS Redshift
                    • Tableau
            '''
        }
    },

    {
    # $100M Chemotherapy Purchasing & Rebates        
        'summary':
        {
            'name': '$100M Chemotherapy Purchasing & Rebates',
            'company': 'Michigan Healthcare Professionals',
            'period_start': '2019',
            'period_end': '2020',
            'high_level_overview': '''
    • Co-managed $100M oncology clinic drug purchasing; wanted more transparency around rebates, contract performance
    • Built web application to provide contract performance info to user
    • Pitched app to top executives at second largest drug wholesaler in the country
            '''
        },
        'details':
        {
            'context': '''
                    • Co-managed the purchasing and rebate contracting for chemotherapy drugs, amounting to over $100M annually.
            ''',
            'problem': '''
                    • Drug rebate process was extremely complicated.

                    • No clear way to monitor clinic’s contract performance, leading to unrealized discounts and rebates.
            ''',
            'action': '''
                    • Built a fully functional web application using Python Django allowing user to see real time drug contract performance

                    • Pitched web app to top executives of the second largest drug wholesaler in the country
            ''',
            'result': '''
                    • Pitched app to top executives at second largest drug wholesaler in the country
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Front end development
                    • Presenting
                Technologies:\n
                    • Python Django
            '''
        }
    },

    {
    # TRIARQ Denials
        'summary':
        {
            'name': 'TRIARQ Denials',
            'company': 'TRIARQ Health',
            'period_start': '2020',
            'period_end': '2021',
            'high_level_overview': '''
    • Lacked visibility into claims denials, resulting in delayed/lost revenue
    • Created analytics-driven workflow to intelligently, proactively address denials
    • Established new team, analytics, and workflows to address vital company function
            '''
        },
        'details':
        {
            'context': '''
                    • Analyst at TRIARQ Health in charge of analytics for RCM operations
            ''',
            'problem': '''
                    • Denied claims leads to delayed and/or lost revenue

                    • No quality analytics existed around claims denials
            ''',
            'action': '''
                    • Built series of dashboards enabling users to analyze denial trends and identify root cause

                    • Created denial worklist generator to operationalize insights
            ''',
            'result': '''
                    • One of the most important functions at the company now had an analytics product that drove a new operational workflow
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Operational Analytics
                    • Business Process Design
                Technologies:\n
                    • Tableau Server
            '''
        }
    },

    {
    # dbt Data Warehouse
        'summary':
        {
            'name': 'dbt Data Warehouse',
            'company': 'TRIARQ Health',
            'period_start': '2022',
            'period_end': '2023',
            'high_level_overview': '''
    • BI Analyst, I was frustrated with not having any control over unreliable/inaccurate data being sourced to me.
    • Pitched dbt-based data warehouse project plan to CEO.
    • Executed on project to within 1 week, built enterprise data warehouse, reduced data refresh time by >95%.
            '''
        },
        'details':
        {
            'context': '''
                    • A data analyst at TRIARQ Health with ~2 years at the company, liaison between the data engineers and the business users.
            ''',
            'problem': '''
                    • Found that data was often inaccurate and unreliable.

                    • Realized that I was at the mercy of the data engineers - I had no ability to personally guarantee the quality of my analytics
            ''',
            'action': '''
                    • Executed on 6 month project timeline to within 1 week.

                    • Learned dbt, built out data warehouse in Google BigQuery. 

                    • Reduced data refresh time from >10hrs to <30min (95%)
            ''',
            'result': '''
                    • Built analytics platform that formed foundation of company's analytics
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • Project Planning/Management
                    • Dimensional Modeling
                Technologies:\n
                    • dbt
                    • Google BigQuery
            '''
        }
    },

    {
    # Tableau Product Adoption
        'summary':
        {
            'name': 'Tableau Product Adoption',
            'company': 'TRIARQ Health',
            'period_start': '2022',
            'period_end': '2023',
            'high_level_overview': '''
    • Wanted to increase internal usage of Tableau Server
    • Gathered user feedback, requirements, analyzed usage patterns
    • Increased user count by over 5x
            '''
        },
        'details':
        {
            'context': '''
                    • Tableau Server Admin managing company’s internal analytics
            ''',
            'problem': '''
                    • Wanted to increase internal usage of Tableau and ensure insight led to action

                    • Company wanted higher quality alternative to proprietary analytics product
            ''',
            'action': '''
                    • Analyzed usage patterns, discovered disproportionate \% of time spent was on 3 dashboards.

                    • Realized dashboards were perceived as complex, created standing meetings to teach the group.
            ''',
            'result': '''
                    • Increased user count by over 5x, established new team, meeting cadence around Tableau
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • “Lean startup” methodology
                    • Requirements gathering
                    • Dashboard design
                Technologies:\n
                    • Tableau Server
            '''
        }
    },

    {
    # RCM Metric Monitoring
        'summary':
        {
            'name': 'RCM Metric Monitoring',
            'company': 'TRIARQ Health',
            'period_start': '2022',
            'period_end': '2023',
            'high_level_overview': '''
    • Wanted to gain visibility into company metrics, and alert to underperformance.
    • Created a "metrics layer" containing a series of metrics and KPIs to track customer performance.
    • New team was formed around these analytics, specifically tasked with identifying underperforming customers & metrics, and intervening proactively.
            '''
        },
        'details':
        {
            'context': '''
                    • Built a TB scale, dimensionally modeled data warehouse.
            ''',
            'problem': '''
                    • Wanted to gain visibility into company metrics, and alert to underperformance.

                    • Company had been blindsided by underperforming metrics, often leading to unhappy clients and constant firefighting.  
            ''',
            'action': '''
                    • Created a "metrics layer" containing a series of metrics and KPIs to track customer performance.

                    • Set up weekly meetings with management to look at underperforming customers/metrics.

                    • Developed a routine of first identifying issue, then discussing root cause, and finally producing plan for intervention.
            ''',
            'result': '''
                    • Every week, underperforming metrics and clients were identified proactively, and significant issues were prevented.
                    ''',
            'skills_and_technologies': '''
                Skills: \n
                    • KPI Development
                    • Statistical Process Control (SPC)
                    • Product design
                Technologies:\n
                    • dbt Semantic Layer
                    • Tableau Server
            '''
        }
    }
]



project_list = [p['summary']['name'] for p in profile_projects]
project_list.insert(0,'Overview')
icon_list = ['assignment' for i in enumerate(project_list)]

with st.sidebar:
    tabs = on_hover_tabs(tabName=project_list,iconName=icon_list, default_choice=0)


if tabs =='Overview':
    page_col1,page_col2,page_col3 = st.columns(3)
    page_col2.image('assets/profile_pic.JPG',caption='This is a profile made by Michael Douglas',width=250)


    st.title('Welcome to my career highlights portfolio!')
    st.subheader('Created by Michael Douglas | email: mdb529@gmail.com')
    st.write('I built this web app to showcase some of the projects I\'ve worked on so far in my career. These are just the handful of projects and outcomes that I\'m most proud of.')
    st.write('Click on a project in the sidebar menu to get some info about the project, its context, and the outcome.')
    
else:
    page_col1,page_col2,page_col3 = st.columns(3)
    page_col1.image('assets/profile_pic.JPG',caption='Made by Michael Douglas',width=200)

    for p in profile_projects:
        summary = p['summary']
        details = p['details']

        project = Project(summary,details)

        # summary_df = project.create_summary_df()
        details_df = project.create_details_df()

        if tabs == project.name:
            st.title(f"{project.name}")

            st.subheader(f"Company: {project.company}")
            st.subheader(f"Period: {project.period_start} to {project.period_end}")
            st.subheader(f"Overview: {project.high_level_overview}")

            exp_col1,exp_col2,exp_col3,exp_col4,exp_col5 = st.columns(5)
            
            expander1 = exp_col1.expander(label='Context:')
            expander1.write(f"{project.context}")

            expander2 = exp_col2.expander(label='Problem:')
            expander2.write(f"{project.problem}")

            expander3 = exp_col3.expander(label='Action:')
            expander3.write(f"{project.action}")

            expander4 = exp_col4.expander(label='Result:')
            expander4.write(f"{project.result}")

            expander5 = exp_col5.expander(label='Skills / Technologies:')
            expander5.write(f"{project.skills_and_technologies}")

            if project.name == 'ACO Network Referral Leakage Report':
                col1,col2 = st.columns(2)
                summary_report_image = Image.open('assets/Referral Leakage Summary Report.png')
                detail_report_image = Image.open('assets/Referral Leakage Detail Report.png')

                col1.image(summary_report_image, caption='Referral Leakage Summary Report')
                col2.image(detail_report_image, caption='Referral Leakage Detail Report')

            elif project.name == 'ACO Program Performance':
                col1,col2,col3 = st.columns(3)
                awv_report_image = Image.open('assets/annual_wellness_visit_report.png')
                coding_for_hccs_report_image = Image.open('assets/coding_for_hccs.png')
                hcc_opportunities_report_image = Image.open('assets/hcc_opportunitites_report.png')

                col1.image(awv_report_image, caption='Annual Wellness Visit Report')
                col2.image(coding_for_hccs_report_image, caption='Coding for HCCs')
                col3.image(hcc_opportunities_report_image, caption='HCC Opportunities Report')

            elif project.name == '$1M Drug Underpayment Recovery':

                asp_report_image = Image.open('assets/asp_comparison_analysis_report.png')

                st.image(asp_report_image, caption='Drug ASP Comparison Analysis Report')

            elif project.name == '$100M Chemotherapy Purchasing & Rebates':

                rebate_tracker_app = Image.open('assets/rebate_tracker_app.png')

                st.image(rebate_tracker_app, caption='Rebate tracker web application built in Python Django')

            elif project.name == 'dbt Data Warehouse':
                col1,col2 = st.columns(2)
                summary_report_image = Image.open('assets/triarq_data_platform.png')
                detail_report_image = Image.open('assets/triarq_star_schema.png')

                col1.image(summary_report_image, caption='TRIARQ Data Platform')
                col2.image(detail_report_image, caption='TRIARQ STAR Schema')

            elif project.name == 'RCM Metric Monitoring':
                metric_monitoring_report_image = Image.open('assets/rcm_metric_monitoring.png')

                st.image(metric_monitoring_report_image, caption='RCM Metric Monitoring Dashboard')
