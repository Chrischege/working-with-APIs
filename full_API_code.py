'''
This is an example of how an API can be used. This is an example of the github api being used to generate the number of python repositories that have the most stars
Having this in mind one can manipulate just about any API to collect data and visualize the data using other types of visualizers not necessarily pygal
Also there is a limit to the number of calls you can make to an API. be sure to check the limit each time you make a call.
Some APIs require one to have a key that they can use so you have to register for a your own key if you want to use an API indefinitely in an app or a website.
'''
from urllib import response
import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

#making an API call and store the response
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('status code:',r.status_code)

#store an API response in a variable
response_dict=r.json()

#process the results
print(response_dict.keys())
# because the response is status code 200, the request was successful

#WORKING WITH THE RESPONSE DICTIONARY
print('total repositories:', response_dict['total_count'])

#explore information about the repositories
repo_dicts=response_dict['items']
print('repositories returned:', len(repo_dicts))

#examine the first repository
repo_dict= repo_dicts[0]
print('\n keys:',len(repo_dict))
for key in sorted (repo_dict.keys()):
    print(key)

#pull out the values of some of the keys in repo_dict
print('\n selected information about first repository:')
print('name:', repo_dict['name'])
print('owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count']) 
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at']) 
print('Description:', repo_dict['description'])

#for visualization, we need more than one repo we can use a loop to print selected info about each of the repositories returned by the API call so we can include them
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

#monitoring the API limits
# some apis have limits hence you can check from their websites whether you have reached like api.github.com/rate_limit
# VISUALIZING REPOSITORIES WITH PYGAL
names, stars=[], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) 


#refining the pygal charts
my_config = pygal.Config()
my_config.x_label_rotation = 90 
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)

# Basically you can render the file to any format you want
chart.render_to_file('python_repos.svg')
