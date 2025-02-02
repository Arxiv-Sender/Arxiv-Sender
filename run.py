import os
import arxiv
import datetime
import argparse
from github import Github
from arxiv import Result, Search
import yaml


token = os.getenv("token")
search_limitation = int(os.getenv("search_limitation"))
send_limitation = int(os.getenv("send_limitation"))
send_term = int(os.getenv("send_term")) + 1
try:
    org = os.getenv("organization")
except:
    org = None
repo = os.getenv("repository")
abstract = os.getenv("abstract")
if abstract.lower() == 'false':
    abstract = False
else:
    abstract = True

today = datetime.datetime.now().date()

def generate_one_paper(r:Result, index:int):
    res = '(' + str(index) + ')' + ' ['+ str(r.title) + ']' + '(' + str(r.links[0].href) +'), ' + str(r.published.date()) + '\n'
    if abstract:
        res += "<details>\n<summary>Abstract : </summary>\n" + str(r.summary) + '\n</details>'
    res += '\n\n\n\n'
    return res

def generate_paper_list(search:Search, limitation:int, term:int):
    client = arxiv.Client()
    res = "# Today's Arxiv Papers\n\n"
    
    for i,r in enumerate(client.results(search)):
        if r.published.date() < today - datetime.timedelta(days=term) or i+1 > limitation:
            if i==0:
                res += "There is no newly uploaded paper :(\n\n"
            break
        res += generate_one_paper(r, i+1)
    return res

def generate_keywords(keywords):
    query, repr_keywords = "", ""
    for k in keywords:
        query += '("' + k + '")' + ' OR '
        repr_keywords += k + ', '
    return query[:-4], repr_keywords[:-2]

if __name__ == "__main__":
    g = Github(token)
    try:
        repo = g.get_organization(org).get_repo(repo)
    except:
        repo = g.get_user().get_repo(repo)

    with open('keywords.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    keywords = config['keywords']
    query, keywords = generate_keywords(keywords)

    search = arxiv.Search(
        query = query,
        max_results = search_limitation,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    title = str(today) + ", Papers for " + keywords
    body = generate_paper_list(search, send_limitation, send_term)
    repo.create_issue(title=title, body=body)
