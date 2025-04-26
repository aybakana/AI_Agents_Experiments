# source: https://www.gettingstarted.ai/crewai-beginner-tutorial/
# pip install crewai[tools]
from crewai import Agent

extractor = Agent(
    role='Content Retriever',
    goal='Given a URL you will retrieve the content.',
    backstory='''As an expert at retrieving complete and accurate
    information, you are responsible for presenting the content of webpages
    that will be used to create engaging content for twitter and a newsletter.
    ''',
    verbose=True
)


writer = Agent(
    role='Content Writer',
    goal='You are responsible to transforming long text into engaging content ready for promotion on different channels.',
    backstory="""
        You are an excellent communications specialist, known for your
        exceptional skill of transforming complex subject into easy to
        understand stories that attract people.
        """,
    verbose=True
)

from crewai import Task

# Define the task for extracting content from a webpage
fetch = Task(
    description=f'''
        Given a URL, retrieve the content of the webpage.
        It is important that you do not miss any information.
        
        Make sure that:
         - The content does not include html, css, or javascript.
         - The content is complete and accurate.
         - You do not include headers, footers, or sidebars.
    ''',
    agent=extractor, 
    expected_output='''
        Title: [The title of the article]
        Author: [The author of the article]
        Date: [The date the article was published]
        Content: [The content of the article]
    '''
)

twitterize = Task(
    description='''
        Given a long text, transform it into engaging content ready for promotion on Twitter.
        Make sure that:
         - The content is engaging and informative.
         - The content is less than 280 characters.
         - The content includes relevant hashtags - Limit to one.
    ''',
    agent=writer,
    expected_output='''
        Title: [Engaging catchy title for the tweet]
        Content: [Engaging content for the tweet]
    '''
)

from crewai import Crew

crew = Crew(
    agents=[extractor, writer],
    tasks=[fetch, twitterize, newsletterize],
    Process=Process.sequential
)

result = crew.kickoff()

print("#### USAGE ####")
print (crew.usage_metrics) # <-- Optional

print("#### RESULT ####")
print(result)