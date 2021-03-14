import requests
import json


PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS']
GROUP = '1013'
ACTION = ['Added', 'Deleted', 'Updated']
TOKEN = ''


headers = {'Authorization': 'token ' + TOKEN}

def get_all_user_pr(userName = 'Sviat26', repos = 'python_au', state = 'open'):
    all_prs = requests.get("https://api.github.com/repos/{}/{}/pulls?state={}".format(userName, repos, state), headers = headers).json()
    return all_prs

def get_all_pr_commits(pr):    
    list_of_commits = requests.get(pr['commits_url'], headers = headers).json()
    return list_of_commits

def get_title(dictionary):
    return dictionary['commit']['message']

def check_prefixes(title):
    title = title.replace('-', ' ')
    parsed_title = title.split(' ')
    errors = list()
    if len(parsed_title) < 4:
        return ('Dude...it is not even in right format.')
    if parsed_title[0] not in PREFIX:
        errors.append('Where have you found such homework({})? It is not from {}.'.format(parsed_title[0], PREFIX))
    if parsed_title[1] not in GROUP:
        errors.append('There is only one group({}), how could you make mistake here? So, it is definetly not {}.'.format(parsed_title[1], GROUP))
    if parsed_title[2] not in ACTION:
        errors.append('Wait...What did you do({})? It is not from {}.'.format(parsed_title[2], ACTION))
    if len(errors) == 0:
      return 'Wow, you are good boy, all is fine'
    else:
      title_errors = '\n'.join(errors)
    return title_errors

def create_pr_comment(title, title_errors):
    return('Hello! \n I am here to help you with making your pr title looks better. Now it is: \n {} \n Mistakes: \n {} '.format(title, title_errors))

def send_pr_comment(pr, comment):
    data = {'body': comment,
            'path': requests.get(pr['url']+'/files', headers=headers).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(pr['url']+'/comments', headers=headers, json=data)
    print(r.json())

def bully_your_pull_request(pr):
    commits = get_all_pr_commits(pr)
    for commit in commits:
        title = get_title(commit)
        title_errors = check_prefixes(title)
        comment = create_pr_comment(title, title_errors)
        send_pr_comment(pr, comment)

def main():
    for pr in get_all_user_pr(userName = 'Sviat26'):
      bully_your_pull_request(pr)

if __name__ == '__main__':
    main()
