import requests

class GetMaskData:
    def get_gov_mask_data(self):
        """
        source:https://data.gov.tw/dataset/116285
        """
        url = "https://quality.data.gov.tw/dq_download_json.php"

        querystring = {"nid":"116285","md5_url":"2150b333756e64325bdbc4a5fd45fad1"}

        headers = {
            'cache-control': "no-cache",
            'postman-token': "79184746-b170-a0a4-da74-a99ad77c052b"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    
get_mask_data = GetMaskData()