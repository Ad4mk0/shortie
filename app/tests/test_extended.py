import requests
import pytest


# @pytest.fixture
def test_ping():
    resp = requests.get("http://localhost:7000/ping")
    assert resp.json() == "pong"


def test_version():
    resp = requests.get("http://localhost:7000/version")
    assert resp.json() != None


def test_status():
    resp = requests.get("http://localhost:7000/status")
    assert resp.json() == "Im fine"


def test_shorting():
    resp = requests.post("http://localhost:7000/shrt/",
        json=
            {
            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
            }
            )

    assert resp.status_code == 200


def test_create_remove():
    resp = requests.post("http://localhost:7000/shrt/",
        json=
            {
            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
            }
            )

    assert resp.status_code == 200
    key =  resp.json()['key']
    resp = requests.delete("http://localhost:7000/shrt/",
                           json={"hash": key})
    
    assert resp.status_code == 200


def test_all():
    """Function checks if new url gets to db"""
    resp = requests.post("http://localhost:7000/shrt/",
        json=
            {
            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
            }
            )
    
    assert resp.status_code == 200
    # url seems to be hashed allright

    original_key =  resp.json()['key']

    resp = requests.get("http://localhost:7000/shrt/all")

    keys = []
    for dictionary in resp.json():
        for key in dictionary.keys():
            if key not in keys:
                keys.append(key)

    # lets try to find it!
    assert original_key in keys


def test_redirect():
    resp = requests.get("http://localhost:7000/shrt/all")

    urls = []
    for dictionary in resp.json():
        for value in dictionary.values():
            if value not in urls:
                urls.append(value)

    for value in urls:
        if requests.get(value).status_code != 200:
            assert False

    assert True

def test_register():
    resp = requests.post("http://localhost:7000/profile/register", json = {
        "username": "string",
        "email": "string",
        "profileSlug": "string"
    })

    assert resp.status_code == 200


def test_login():
    resp = requests.post("http://localhost:7000/profile/login", json = {
        "username": "string",
        "password": "string"
    })

    assert resp.status_code == 200


def test_profile_page():
    resp = requests.get("http://localhost:7000/profile/p/string")
    assert resp.status_code == 200



