import urllib3
import re
import json
from colorama import Fore, init

# Class urlAutomationMachine
# Defines a urlAutomationMachine object which initiates the request in order to determine the status
# code of the url. If a file is passed, a regex will be processed on all lines in the file in order
# to pull out the urls and for each url, a network request attempt will occur.


class urlAutomationMachine:
    def __init__(self, input=None, isJson=False, ignore=None):
        self.input = input
        self.listOfUrls = []
        self.isJson = isJson
        self.http = urllib3.PoolManager()
        self.response_status = None
        self.ignore_list = []
        if ignore is not None:
            ignore_file = open(ignore, "r")

            self.ignore_list = re.findall(
                r"https?:[a-zA-Z0-9_.+-/#~]+", ignore_file.read()
            )

    def processUrl(self):
        if self.input is not None:
            if type(self.input) == str:
                try:
                    self.checkUrl()
                    self.makeRequest(self.input)
                except:
                    raise ValueError("Input was not a valid URL")
        else:
            raise AttributeError("Function requires a url that's a string")

    def processFile(self):
        if self.input is not None:
            if type(self.input) == str:
                fileToCheck = open(self.input, "r")
                self.listOfUrls = re.findall(r"https?:[a-zA-Z0-9_.+-/#~]+", fileToCheck.read())

                if self.listOfUrls == []:
                    pass

                for line in self.listOfUrls:
                    line = line.strip()
                    if line not in self.ignore_list:
                        self.makeRequest(line)

                fileToCheck.close()
            else:
                raise ValueError("Function requires a file to be inserted")
        else:
            raise AttributeError("A parameter is required")

    def makeRequest(self, url):
        init()
        try:
            r = self.http.request("HEAD", url)
            self.response_status = r
            self.printOutput(r, url)
        except urllib3.exceptions.MaxRetryError as e:  # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
            print("Url does not load fast enough")
            pass

    def printOutput(self, r, url):
        if self.isJson:
            jsonURL = {"url": url, "status_code": r.status}
            if r.status == 200:
                print(
                    Fore.GREEN
                    + f"[SUCCESS]: {jsonURL} passes automation. This url is working properly!"
                )
            elif r.status == 400 or r.status == 404:
                print(
                    Fore.RED
                    + f"[FAILURE]: {jsonURL} fails automation. This url is broken unfortunately!"
                )
            else:
                print(
                    Fore.WHITE
                    + f"[UNKNOWN] {jsonURL} gives off a warning. This url is fishy!"
                )
        else:
            if r.status == 200:
                print(
                    Fore.GREEN
                    + f"[SUCCESS]: {url} passes automation. This url is working properly!"
                )
            elif r.status == 400 or r.status == 404:
                print(
                    Fore.RED
                    + f"[FAILURE]: {url} fails automation. This url is broken unfortunately!"
                )
            else:
                print(
                    Fore.WHITE
                    + f"[UNKNOWN] {url} gives off a warning. This url is fishy!"
                )

    def getStatus(self) -> int:
        return self.response_status.status

    def processTelescope(self):
        telescopeURL = "http://localhost:3000/posts"  # Local host telescope url to grab data locally
        try:
            posts = self.http.request("GET", telescopeURL)
            posts = json.loads(posts.data)
            for post in posts:
                self.makeRequest(f"{telescopeURL}/{post['id']}")
        except urllib3.exceptions.MaxRetryError as e:  # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
            print(str(e))

    def checkUrl(self) -> str or None:
        valid_search = re.search(r"https?:[a-zA-Z0-9_.+-/#~]+", self.input)

        if valid_search is not None:
            return valid_search.string
        else:
            return None