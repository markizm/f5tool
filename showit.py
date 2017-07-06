import sys
import getpass
import bigsuds 
#from ltmstuff import * 
from flask import Flask, jsonify

ltm = "10.3.4.17"
pwd=getpass.getpass(prompt='enter your ltm password:  ') 
obj=bigsuds.BIGIP(hostname=ltm,username='<your uid>',password=pwd,debug=True)

app = Flask(__name__)

@app.route('/vs-stats')
def vs_stats():
    vs_stat=obj.LocalLB.VirtualServer.get_all_statistics()
    try:
        for stats in vs_stat['statistics']:
            return jsonify(stats['statistics'][8]['value']['low'])
    except Exception as e:
        return e

@app.route('/irules')
def i_rules():
    rule_list=obj.LocalLB.Rule.query_all_rules()
    try:
        return jsonify(rule_list)
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(host='0.0.0.0')
