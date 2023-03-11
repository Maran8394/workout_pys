import os
import re
from ast import literal_eval
from datetime import datetime
from zipfile import ZipFile

import requests


def getFilename_fromCd(cd):
    s = cd.split(";")
    for fn in s:
        if "filename=" in fn:
            f = fn.strip()
            fName = re.findall(r'"([^"]*)"', f)
            return fName[0]


print(datetime.now().time())

CLIENT_ID = '3d501d91-7dcf-4c65-976b-3260be4dafcb'
CLIENT_SECRET = 'schF5LrpT8xvmWT7dywA7DxOYhnb5tkHIOUAiz4Ece4'
SCOPE = "content:*:* core:*:* datahub:*:* enrollment:*:* grades:*:* organizations:*:* quizzing:*:* reporting:*:* users:*:*"
da = {
    "username": "datahubuser",
    "password": "Manipal@123",
}

REDIRECT_URI = "https://localhost:3001/"
AUTHORIZE_URL = "https://auth.brightspace.com/oauth2/auth"
ACCESS_TOKEN_URL = "https://auth.brightspace.com/core/connect/token"

URL = '{}?response_type=code&client_id={}&redirect_uri={}&scope={}'.format(AUTHORIZE_URL, CLIENT_ID, REDIRECT_URI,
                                                                           SCOPE)
firstUrl = requests.get(URL)

splitted = str(firstUrl.url).split("/auth/")
th = splitted[0] + "/login?sessionExpired=0&target=d2l/auth/" + splitted[1]
hed = {"Referer": firstUrl.url}
secondRedirctUrl = requests.get(th, headers=hed)

loginUrl = "https://learn.manipalbfsi.com/d2l/lp/auth/login/login.d2l"
header2 = {
    "Origin": "https://acadlms.d2l-partners.brightspace.com",
    "Referer": secondRedirctUrl.url
}

postMethod = requests.post(loginUrl, headers=header2, data=da, allow_redirects=False)

header3 = {
    "Referer": secondRedirctUrl.url,
}
fifthUrl = requests.get(firstUrl.url, headers=header3, allow_redirects=False, cookies=postMethod.cookies)
fifthRedirctUrl = fifthUrl.headers.get("Location")

headerForSixthUrl = {
    "Referer": "https://learn.manipalbfsi.com/"
}
sixthGetMethod = requests.get(fifthRedirctUrl, headers=headerForSixthUrl, allow_redirects=False)
sixthRedirectUrl = sixthGetMethod.headers.get("Location")
code = sixthRedirectUrl.split("code=")[1]
body = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}

forFinalPost = requests.post(url=ACCESS_TOKEN_URL, data=body)
rep_body = forFinalPost.content.decode('utf-8')
bod = literal_eval(rep_body)


hhh = {"Authorization": f"Bearer {bod['access_token']}"}

k = [
    "1d6d722e-b572-456f-97c1-d526570daa6b",
    "07a9e561-e22f-4e82-8dd6-7bfb14c91776",
    "533f84c8-b2ad-4688-94dc-c839952e9c4f",
    "7e16311c-d302-45da-afd9-98af90706ccb",
    "51b028b4-d5ae-4784-b03e-18556b50e590",
    "30d67ca7-8c8b-4dde-93ef-becd2ac2e223",
    "0646bbe1-79af-48ef-89d9-91f677419259",
    "bce64f34-acee-415e-aceb-e3a38ddf476f",
    "d9923de9-de6a-41ea-a63e-e8fd771b7b93",
    "041dde83-3a29-4a37-97de-9ee615318111",
    "eef7ca81-86bb-430c-96ee-382b83f5c0f9",
    "f1623581-c5d7-4562-93fe-6ad16010c96b",
    "396e9578-04e3-49b2-bf89-c17757e501de"
]
downloadLink = "https://learn.manipalbfsi.com/d2l/api/lp/1.33/dataExport/bds/download/"
#
csvFilesList = []

for link in k:
    dl = apiReq = requests.get(f"{downloadLink}{link}", headers=hhh)
    names = dl.headers.get('content-disposition')
    fileName = getFilename_fromCd(dl.headers.get('content-disposition'))
    fi = open(fileName, 'wb').write(dl.content)
    zi = ZipFile(fileName)
    csvFilesList.extend(zi.namelist())
    zi.extractall(path="csvFiles/")
    zi.close()
    os.remove(fileName)
print(datetime.now().time())
