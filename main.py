import json
import shutil
import os
import subprocess

if __name__ == '__main__':
    directories = os.listdir('/Users/chris/Dropbox/songs')
    for directory in directories:
        print(directory)
        if directory != '.DS_Store':
            result = subprocess.run(["h5tojson", f"/Users/chris/Dropbox/songs/{directory}"], stdout=subprocess.PIPE)
            json_data = json.loads(result.stdout)
            with open(f'/Users/chris/Dropbox/songs_json/{directory.replace(".h5", ".json")}', 'a') as output:
                json.dump(json_data, output)


    songs = []
    song_json_files = os.listdir('/Users/chris/Dropbox/songs_json')

    for song_json_file in song_json_files:
        if song_json_file == 'TRBAWHU128EF3563C5.json':
            continue

        print(song_json_file)
        with open(f'/Users/chris/Dropbox/songs_json/{song_json_file}') as file:
            song_json = json.load(file)

        song_key = list(song_json["datasets"].keys())[20]
        song_details = song_json["datasets"][song_key]["type"]["fields"]
        song_dict = {}
        for detail_dict, value in zip(song_details, song_json["datasets"][song_key]["value"][0]):
            song_dict.update({detail_dict["name"]: value})

        songs.append(song_dict)


    with open('../songs.json', 'w') as output:
        json.dump(songs, output)
