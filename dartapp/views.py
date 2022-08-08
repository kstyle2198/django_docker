from django.shortcuts import render
import requests
import pandas as pd
import numpy as np

api_key = "b97e634e4e12230038b3e1aa1e3563d230673251"
corp_code = '00344287'

base_info = {
    "corp_code" : '00344287',
    "target_year": '2021',
    "target_report" : '11011',  #"11013": "1분기보고서", "11012": "반기보고서","11014": "3분기보고서", "11011": "사업보고서"
    "report_type" : 'OFS',      #CFS:연결재무제표, OFS:재무제표
}


def divide_100(num):
    return int(np.around(float(num)/1000000))

def get_statement_info(request):
    r=requests.get(f"https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key={api_key}&corp_code={base_info['corp_code']}&bsns_year={base_info['target_year']}&reprt_code={base_info['target_report']}&fs_div={base_info['report_type']}").json()
    # print(r['list'])
    df = pd.DataFrame(r['list'])
    # print(df)
    df.to_excel('dart_df.xlsx', encoding='utf-8')
    df = df.loc[:, ['account_nm', 'thstrm_amount', 'frmtrm_amount', 'bfefrmtrm_amount']]
    df = df[df["account_nm"].isin(['유동자산','현금및현금성자산','매출채권', '미수금', '재고자산', '자산총계', '유동부채', '부채총계', '수익(매출액)', '매출액', '매출원가', '매출총이익', '영업이익', '영업이익(손실)', '총포괄이익', '총포괄이익(손실)'])]
    df = pd.DataFrame(df).fillna(0)
    df.columns = ["구분", "당기", "전기", "전전기"]
    df["당기"] = df["당기"].apply(divide_100)
    df["전기"] = df["전기"].apply(divide_100)
    df["전전기"] = df["전전기"].apply(divide_100)
    df.set_index('구분', drop=True, append=False, inplace=True)
    dict_data = df.to_dict()
    dict_data.update({"base" : base_info})
    return render(request, 'dart.html', {'context' : dict_data})
    
if __name__ == "__main__":
    get_statement_info()
