from flask import Flask, render_template,request
import requests

app = Flask(__name__)
wo = ["Full time working",
				"Housewife",
				"Part time working",
				"Retired",
				"Student",
				"Unemployed"]
zes = [0]*len(wo)
mp = dict()
for i,j in enumerate(wo):
    zes[i] = 1
    mp[j] = zes
    zes = [0]*len(wo)
wo = ["Central",
				"Harbour",
				"Western"]
zes = [0]*len(wo)
mp2 = dict()
for i,j in enumerate(wo):
    zes[i] = 1
    mp2[j] = zes
    zes = [0]*len(wo)
wo = ["Dish",
				"none",
				"local"]
zes = [0]*len(wo)
mp3 = dict()
for i,j in enumerate(wo):
    zes[i] = 1
    mp3[j] = zes
    zes = [0]*len(wo)
@app.route("/",methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        arr = []
        for x in request.form:
            if x == 'submit':
                break
            elif x == "age":
                val = float(request.form[x])
                arr.append(val)
            elif x =="ott_t":
                arr.append(float(request.form[x]))
            elif x == "tv_t":
                arr.append(float(request.form[x]))
            else:
                try:
                    arr.append(float(request.form[x]))
                except:
                    if x == "yes_no3":
                        if request.form[x] == "yes":
                            arr.append(0)
                        else:
                            arr.append(1)
                    elif "yes_no" in x:
                        if request.form[x] == "yes":
                            arr.append(1)
                        else:
                            arr.append(0)
                    else:
                        if x == "occupation":
                            for j in mp[request.form[x]]:
                                arr.append(j)
                        elif x == "living":
                            for j in  mp2[request.form[x]]:
                                arr.append(j)
                        # print(x)
                        elif x == "tv_type":
                            for j in mp3[request.form[x]]:
                                arr.append(j)
                        elif x == "mode":
                            if request.form[x] == "ott":
                                arr.append(1)
                            else:
                                arr.append(0)
        val = api(arr)
        print(val)
    return "<h1> You will watch {} </h1>".format(val[0][0])

def api(send):
    API_KEY = "o1cHn_3_u3apZhmlfa1zsnmFX-eOC5mNlFlNsKEIMSGo"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    payload_scoring = {"input_data": [{"fields": ["Age",
				"How much do you pay for OTT platforms on monthly basis ?",
				"How much do you pay for TV on monthly basis ?",
				"Time_Spent",
				"Time_Spent_TV",
				"OTT during Lockdown",
				"OTT wins TV",
				"Full time working",
				"Housewife",
				"Part time working",
				"Retired",
				"Student",
				"Unemployed",
				"Central",
				"Harbour",
				"Western",
				"Dish TV(Tata aky, Airtel, etc)",
				"Don't watch",
				"Local cable",
				"mode",
				"Affect"
			],
                                       "values": [send]}]}
    response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/use_this/predictions?version=2021-09-27&version=2021-09-27', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    return  response_scoring.json()['predictions'][0]['values']


if __name__ == '__main__':
    app.run()
