import re
import os

for show in os.listdir("processed/"):
    print(show)
    try:
        m = re.search('s\d\de\d\d', show)[0]
    except TypeError:
        continue
    m1 = m.replace('s', 'S')
    m1 = m1.replace('e', 'E')
    new_name = show.replace(m, m1)
    os.rename('processed/' + show, 'processed/' + new_name)