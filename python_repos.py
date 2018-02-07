'''API response'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# API and save
url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(url)
print("Status code:", r.status_code)

# save response as a varible
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# search repository info
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# learn from the repositories
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# visible
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Python_repos.svg')
