import re
import os


def rename_file(startname):
    file_name = startname.replace('.', ' ')
    file_name = file_name.replace(' mp4', '.mp4')
    os.rename('processed/' + startname, "processed/" + file_name)
    return file_name


def move_file_to_season(file):
    season = re.search('S\d\d', file)[0]
    if season is not None:
        show_name = file[:file.index(season)-1]
        for folder in os.listdir('/home/henry/tvshows/'):
            if folder == show_name:
                show_season = re.search('S\d\d', file)[0]
                show_season = get_season(show_season)
                if os.path.isfile("/home/henry/tvshows/" + folder + "/" + show_season + '/') is not True:
                    try:
                        os.mkdir("/home/henry/tvshows/" + folder + "/" + show_season + '/')
                    except FileExistsError:
                        print('folder already exists')
                os.rename("processed/" + file, "/home/henry/tvshows/" + folder + "/" + show_season + "/" + file)
                print(file + " has been moved to " + "/home/henry/tvshows/" + folder + "/" + show_season + "/" + file)
                return

    else:
        os.rename('processed/' + file, '/home/henry/movies/' + file)


def get_season(regex):
    print(regex)
    if 'S01' in regex:
        return "Season 1"
    elif 'S02' in regex:
        return "Season 2"
    elif 'S03' in regex:
        return "Season 3"
    elif 'S04' in regex:
        return "Season 4"
    elif 'S05' in regex:
        return "Season 5"
    elif 'S06' in regex:
        return "Season 6"
    elif 'S07' in regex:
        return "Season 7"
    elif 'S08' in regex:
        return "Season 8"
    elif 'S09' in regex:
        return "Season 9"
    elif 'S10' in regex:
        return "Season 10"
    elif 'S11' in regex:
        return "Season 11"
    elif 'S12' in regex:
        return "Season 12"
    elif 'S13' in regex:
        return "Season 13"
    elif 'S14' in regex:
        return "Season 14"
    elif 'S015' in regex:
        return "Season 15"
    elif 'S016' in regex:
        return "Season 16"


for filename in os.listdir("processed/"):
    if filename.count('.') > 1:
        new_file_name = rename_file(filename)
        move_file_to_season(new_file_name)
    else:
        move_file_to_season(filename)