import pandas as pd

class Project:
    def __init__(self,summary,details):
        self.summary = summary
        self.details = details

        self.name = summary['name']
        self.company = summary['company']
        self.period_start = summary['period_start']
        self.period_end = summary['period_end']
        self.high_level_overview = summary['high_level_overview']

        self.context = details['context']
        self.problem = details['problem']
        self.action = details['action']
        self.result = details['result']
        self.skills_and_technologies = details['skills_and_technologies']


    def create_summary_df(self):
        summary_df = pd.DataFrame(self.summary,index=[0])
        return summary_df

    def create_details_df(self):
        details_df = pd.DataFrame(self.details,index=[0])
        return details_df