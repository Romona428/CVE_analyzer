import requests
import json

url = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=3"
response = requests.get(url)
data = response.json()

# 格式化輸出 JSON 結構
print(json.dumps(data, indent=2))
