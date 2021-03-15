import requests
import datetime

import json

def test_api_post():

    data = {
        'audio_file_type': 'song',
        'metadata':
        {
            'title': 'rockstar',
            'duration': 100,
            'upload_time': "27-02-2020 01:08:51"
        }
    }
    resp = requests.post(url="http://127.0.0.1:1234/add/song", data=json.dumps(data), headers={'Content-Type': 'application/json'})
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)

def test_api_get():
    resp = requests.get("http://127.0.0.1:1234/song")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['Songs']:
        if record['id'] == 1:
            assert record['title'] == "rockstar",\
                "Data not matched! Expected : rockstar, but found : " + str(record['title'])
            assert record['duration'] == 100,\
                "Data not matched! Expected : 100, but found : " + str(record['duration'])


def test_api_get_by_id():
    resp = requests.get("http://127.0.0.1:1234/song/1")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json():
        if record['id'] == 1:
            assert record['title'] == "rockstar",\
                "Data not matched! Expected : rockstar, but found : " + str(record['title'])
            assert record['duration'] == 100,\
                "Data not matched! Expected : 100, but found : " + str(record['duration'])

def test_api_put():
    data = {
        "audio_file_type": "audiobook",
        "metadata":
        {
            "title": "Scary Stories",
            "author": "ruskin bond",
            "narrator": "naman tyagi",
            "upload_time": "27-02-2020 01:08:51",
            "duration": 100
        }
    }

    resp = requests.post(url="http://127.0.0.1:1234/add/audiobook", data=json.dumps(data), headers={'Content-Type': 'application/json'})
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)
    resp = requests.get("http://127.0.0.1:1234/audiobook")
    for record in resp.json()['Audiobooks']:
        assert record['narrator'] == "naman tyagi",\
            "Data not matched! Expected : naman tyagi, but found : " + str(record['title'])
    
    data = {
        "audio_file_type": "audiobook",
        "metadata":
        {
            "title": "Scary Stories",
            "author": "ruskin bond",
            "narrator": "vandan tyagi",
            "upload_time": "27-02-2020 01:08:51",
            "duration": 100
        }
    }

    resp = requests.put("http://127.0.0.1:1234/audiobook/1", data=json.dumps(data), headers={'Content-Type': 'application/json'})
    #print(resp.json()['Audiobooks'])
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)
    resp = requests.get("http://127.0.0.1:1234/audiobook")
    for record in resp.json()['Audiobooks']:
        assert record['narrator'] == "vandan tyagi",\
            "Data not matched! Expected : vandan tyagi, but found : " + str(record['narrator'])
    resp = requests.delete(url="http://127.0.0.1:1234/audiobook/1")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)


def test_api_delete():
    data = {
        "audio_file_type":"podcast",
        "metadata":
        {
            "title": "Tech Today",
            "host": "Mark Brown",
            "participants": ["naman","tyagi" ,"vandan", "gupta"],
            "upload_time": "27-02-2020 01:08:51",
            "duration": 100
        }
    }

    resp = requests.post(url="http://127.0.0.1:1234/add/podcast", data=json.dumps(data), headers={'Content-Type': 'application/json'})
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)
    resp = requests.delete(url="http://127.0.0.1:1234/podcast/1")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)
    resp = requests.get(url="http://127.0.0.1:1234/podcast/1")
    assert (resp.status_code == 400), "Status code is not 400. Rather found : "\
        + str(resp.status_code)