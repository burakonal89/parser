xl = pd.ExcelFile("GENEL_GUNLUK_ISLETME_NETICESI_2022-03-01.xlsx")
names = xl.sheet_names 

for name in names:
    skiprows = 2
    temp_df = pd.read_excel(
        "GENEL_GUNLUK_ISLETME_NETICESI_2022-03-01.xlsx",
        sheet_name=name,
        skiprows=skiprows)
    if temp_df.shape[0] == 0:
        continue
    count = np.array(["Unnamed" in x for x in temp_df.columns]).sum()        
    while count > 1:
        skiprows += 1 
        temp_df = pd.read_excel(
            "GENEL_GUNLUK_ISLETME_NETICESI_2022-03-01.xlsx",
            sheet_name=name,
            skiprows=skiprows)
        count = np.array(["Unnamed" in x for x in temp_df.columns]).sum()
    drop_cols = [x for x in temp_df.columns if "Unnamed" in x]
    if len(drop_cols) > 0:
        temp_df.drop(drop_cols, axis=1, inplace=True)
    print("{} parsed.".format(name))
    temp_df.to_json(
        "{}.json".format(name),
        orient="records",
        force_ascii=False)
    print("{}.json created.".format(name))