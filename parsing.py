# import packages
import re
import colorama
from requests_html import HTMLSession
from itertools import groupby
# import our sites list
from sites_list import list

# colorization terminal log
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX

# declaring an array of raw emails
raw_emails = []
sites_arr = list

# regular expression for finding emails
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# starting a cycle for site indices in sites_arr
for i in range(len(sites_arr)):
    # formatting raw sites list for https connection
    url = f"https://{sites_arr[i]}/"
    count = len(sites_arr)
    try:
        sesh = HTMLSession()
        resp = sesh.get(url)
        # resp.html.render()
        for re_match in re.finditer(EMAIL_REGEX, resp.html.raw_html.decode()):
            email = re_match.group()
            raw_emails.append(email)
            # clearing email matches
            to_clean_emails = raw_emails
            done_emails = [el for el, _ in groupby(to_clean_emails)]
            with open("emails.md", "w") as file:
                # writing an emails to markdown file
                print("\n".join(map(str, done_emails)), file=file)
    except:
        continue
    else:
        # informating us in terminal
        percent = round(((i/count) * 100.0), 1)
        print(
            f"{GRAY}Parsed {GREEN} {i + 1} {GRAY}of {GREEN} {count} {GRAY}, done {GREEN} {percent}%")
