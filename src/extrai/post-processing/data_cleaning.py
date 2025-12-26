import re
import json
import pandas as pd

with open("./src/extrai/results/deepseek-r1:8b_result.json", "r") as file:
    dpk_result = json.load(file)

dpk_result
dpk_result_list = list()
for result in dpk_result:
    # result = dpk_result[2]
    clean = re.sub(
        r"<think>.*?</think>", "", result.get("result"), flags=re.DOTALL
    ).strip()
    clean = re.sub(r"^```json\s*|\s*```$", "", clean, flags=re.DOTALL).strip()
    clean = json.loads(clean)
    if isinstance(clean, list):
        [dpk_result_list.append(siniestro) for siniestro in clean]
    elif "siniestros" in clean.keys():
        [dpk_result_list.append(siniestro) for siniestro in clean.get("siniestros")]
    else:
        dpk_result_list.append(clean)


df = pd.DataFrame(dpk_result_list)

df.columns

df.to_csv("./result_deepseek-r1:8b_clean.csv", sep=";")
