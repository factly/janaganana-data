from lxml import html
import requests
import os
import sys


BASE_URL = "http://www.censusindia.gov.in/2011census/C-series/C-14.html"


def get_links_from_webpage():
    page = requests.get(BASE_URL)
    tree = html.fromstring(page.content)
    excel_links = []
    for elem in tree.xpath('//a[@href]'):
        href_attr = elem.get('href')
        if href_attr is not None and href_attr.endswith(('14.xls')):
            prepend_str='http://www.censusindia.gov.in/2011census/C-series/'
            # http://www.censusindia.gov.in/2011census/C-series/c-14/DDW-0000C-14.xls
            excel_links.append(prepend_str+href_attr)
    return excel_links


def download_census_excel_files():
    for link in get_links_from_webpage():
        dir_name = link.split('/')[-2]
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

        file_name = os.path.join(dir_name, link.split('/')[-1])
        with open(file_name, 'wb') as f:
            resp = requests.get(link)
            if resp.ok:
                f.write(resp.content)


def main():
    download_census_excel_files()

if __name__ == "__main__":
    sys.exit(main())
