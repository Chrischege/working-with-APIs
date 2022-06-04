import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# we store the name and the stars which are the data that are going to be used in dictionaries so that pygal can unpack them.
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
