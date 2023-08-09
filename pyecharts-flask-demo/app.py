from random import randrange

from flask.json import jsonify
from flask import Flask, render_template, request
from markupsafe import Markup
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar
from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.faker import Faker
from pyecharts.globals import CurrentConfig
import pandas
from requests_html import HTMLSession
import json
import pandas as pd
# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

def get_data(job_name,city_name):
    import pandas
    from requests_html import HTMLSession
    import json
    import pandas as pd
    import requests
    用户输入职位 = job_name
    用户输入城市 = city_name
    城市编码 = {
    '北京':'010',
    '上海':'020',
    '广州':'050020',
    '深圳':'050090',

}
    url = "https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
    payload = {
    "data": {
        "mainSearchPcConditionForm": {
            "city": 城市编码[用户输入城市],
            "dq": 城市编码[用户输入城市],
            "pubTime": "",
            "currentPage": 0,
            "pageSize": 40,
            "key": str(用户输入职位),
            "suggestTag": "",
            "workYearCode": "0",
            "compId": "",
            "compName": "",
            "compTag": "",
            "industry": "",
            "salary": "",
            "jobKind": "",
            "compScale": "",
            "compKind": "",
            "compStage": "",
            "eduLevel": ""
        },
        "passThroughForm": {
            "scene": "input",
            "skId": "",
            "fkId": "",
            "ckId": "h2c8pxojavrmo1w785z7ueih2ybfpux8",
            "suggest": None
        }
    }
}
    session = HTMLSession()
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "399",
        "Content-Type": "application/json;charset=UTF-8;",
        "Cookie": "__gc_id=ba575649f262440b97583f40312082aa; __uuid=1680367209983.58; _ga=GA1.1.1780140015.1681902728; need_bind_tel=false; new_user=false; c_flag=fd8e161021d62dd50e5032f3c60a147a; imClientId=40be7e37d455d9dca12bac537377bfad; imId=40be7e37d455d9dc3e4f5f0f695234e5; imClientId_0=40be7e37d455d9dca12bac537377bfad; imId_0=40be7e37d455d9dc3e4f5f0f695234e5; __tlog=1687443932879.32%7C00000000%7C00000000%7Cs_00_t00%7Cs_00_t00; XSRF-TOKEN=BA5R7LlfSFWBEKpGQU4sjA; UniqueKey=fe87a9f3258ac642a9dba665e9526a14; liepin_login_valid=0; lt_auth=v75fP3QMxlXw4XfcjTcLtacfj9%2BsU2yYpnhehk8FhoK5W6Ll4P%2FgSwuCq7gH%2FioIqxJyd%2FQzMLb2Muz6ynpN6kIQ%2FFGnlZ6utf6k1XweTudmHuyflMXuqsjQQJgirXo6ykpgn2si0HU%3D; inited_user=0b40e95258783b742e53b3c4507c0e74; user_roles=0; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E6%B2%88%E8%BF%9E%E6%9D%B0; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1685585264,1686135762,1687265958,1687443970; acw_tc=2760828616874439713004529effda973c1160959fc97168d2e9d8205f5aa9; imApp_0=1; __session_seq=6; __uv_seq=6; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1687444361; fe_im_socketSequence_new_0=5_5_5; fe_im_opened_pages=; fe_im_connectJson_0=%7B%220_fe87a9f3258ac642a9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; _ga_54YTJKWN86=GS1.1.1687443982.16.1.1687444379.0.0.0",
        "Host": "api-c.liepin.com",
        "Origin": "https://www.liepin.com",
        "Referer": "https://www.liepin.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Client-Type": "web",
        "X-Fscp-Bi-Stat": "{\"location\":\"https://www.liepin.com/zhaopin/?inputFrom=head_navigation&scene=init&workYearCode=1&ckId=nnmmdmzewpti6x0d4ae802fd32me5s68\"}",
        "X-Fscp-Fe-Version": "",
        "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
        "X-Fscp-Trace-Id": "228c7100-8348-4c80-8eac-de9afa28e241",
        "X-Fscp-Version": "1.1",
        "X-Requested-With": "XMLHttpRequest",
        "X-Xsrf-Token": "BA5R7LlfSFWBEKpGQU4sjA"
    }
    r = session.post(url, data=json.dumps(payload), headers=headers)
    response_data = r.json()
    page = response_data['data']['pagination']['totalPage']
    response_df = []
    for i in range(page): # 需要判断页面的数据有多少页
        payload['data']['mainSearchPcConditionForm']['currentPage']=i
        # send a POST request with headers
        r = requests.post(url, data=json.dumps(payload), headers=headers)
    response_data = r.json()
    print(response_data)
    df = pd.json_normalize(response_data['data']['data']['jobCardList'])
    response_df.append(df)
    df = pd.concat(response_df)
    key = payload['data']['mainSearchPcConditionForm']['key']
    df.to_excel('liepin2.xlsx')
    df = pd.read_excel('liepin2.xlsx')
    df

    df_PM_gz =  df[['job.labels','job.refreshTime','job.title','job.salary','job.dq','job.topJob','job.requireWorkYears','job.requireEduLevel','comp.compStage','comp.compName','comp.compIndustry','comp.compScale']]
    df_PM_gz

    df_PM_gz['job.dq'].value_counts()
    地区 = [ df_PM_gz['job.dq'].value_counts().index.tolist()[i].split('-')[1]\
             for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if '-' in v]
    地区
    岗位个数 = [ df_PM_gz['job.dq'].value_counts().values.tolist()[i] for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if "-" in v]
    岗位个数
    return 地区,岗位个数


from pyecharts.charts import Map
def map_chart(地区,岗位个数) -> Map:
    city_name = request.form.get('city_name')
    job_name = request.form.get('job_name')
    c = (
        Map()
        .add(city_name, [list(z) for z in zip(地区, 岗位个数)], city_name)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=city_name+job_name+"岗位地区分布"), visualmap_opts=opts.VisualMapOpts()
        )
    )

    return c
@app.route("/")
def index_boot():
    return render_template("index_bootstrap.html")
@app.route('/results', methods=['POST'])
def results():
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    from markupsafe import Markup
    地区, 岗位个数 = get_data(job_name, city_name)
    print(地区, 岗位个数)
    c = map_chart(地区, 岗位个数)
    return Markup(c.render_embed())

#@app.route('/index')
#def index():
 #   from markupsafe import Markup
 #   地区,岗位个数 = get_data("产品经理", "广州")
  #  print(地区,岗位个数)
 #   c = map_chart(地区, 岗位个数)
 #   return Markup(c.render_embed())



# @app.route("/mapchart")
# def indexxx():
#     c = map_chart()
#     return c.dump_options_with_quotes()

# @app.route("/results")
# def results():
   # return render_template("results.html")

# idx = 9


# @app.route("/lineDynamicData")
# def update_line_data():
#     global idx
#     idx = idx + 1
#     return jsonify({"name": idx, "value": randrange(50, 80)})


if __name__ == "__main__":
    app.run()