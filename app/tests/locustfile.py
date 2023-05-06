import json

from locust import HttpUser, between, task
import requests




class ShorterClient(HttpUser):
    wait_time = between(1,3)
    
    

    def onstart():
        response = requests.post("http://localhost:7000/shrt/",
                        json=
                            {
                            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
                            }
            )
        return response.json()
    
    slug = onstart()

    @task(1)
    def put_url_link(self):
        self.client.post("/shrt/",
                         data=json.dumps(
            {
            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
            }
            ))

    @task(2)
    def read_url_link(self):
        self.client.get(f"/s/{self.slug['key']}")

    @task(3)
    def remove_link(self):
        response = requests.post("http://localhost:7000/shrt/",
                        json=
                            {
                            "url": "https://www.seznamzpravy.cz/clanek/domaci-politika-byvaly-ustavni-soudce-navrh-hnuti-ano-bude-formalne-odmitnut-kvuli-senatorum-230495#dop_ab_variant=0&dop_source_zone_name=zpravy.sznhp.box&dop_req_id=qkVtTBkLoUZ-202305051547&dop_id=230495&source=hp&seq_no=1&utm_campaign=abtest217_krokovy_redesign_feedu_varB&utm_medium=z-boxiku&utm_source=www.seznam.cz"
                            }
            )
        
        self.client.delete("/shrt/",
                           data=json.dumps({"hash": response.json()['key']}))
