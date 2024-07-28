import pandas as pd

PATH = "Notebooks/Amazon Text Classification/data/"


def extract_to_pd(file_name: str, start: str):
    txt = open(f"{PATH}{file_name}.txt", "r", encoding="utf8")
    txt = txt.read()
    txt = txt.replace("\n\n", "")

    df = pd.DataFrame(txt.split("\n"), columns=["text"])
    df["label"] = 0
    s_i = df[df["text"] == start].index[0]
    e_i = df[df["text"] == "Add to cart"].index[-1]
    for i in range(s_i, e_i + 1):
        df.at[i, "label"] = 1
    df.to_csv(f"{PATH}{file_name}.csv", index=False)


extract_to_pd(
    "phones",
    "SAMSUNG GALAXY A15 5G A SERIES CELL PHONE, 128GB UNLOCKED ANDROID SMARTPHONE,",
)

extract_to_pd(
    "laptops",
    'ACER ASPIRE 3 A315-24P-R7VH SLIM LAPTOP | 15.6" FULL HD IPS DISPLAY | AMD RYZEN',
)
