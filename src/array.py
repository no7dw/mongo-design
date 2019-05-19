import json
import argparse
import config 
import re

def report(path, op_path):
    def volatility(op_path, arr):
        daily_vol = 0
        num_lines = 0
        regex = ''
        rate = 0 
        for a in arr:
            regex = regex + a + "|"

        with open(path, 'r',  encoding='utf-8',  errors='ignore') as f:
            for x in f:
                s = re.search(regex, x).start()
                if(s):
                    daily_vol += 1   
                    num_lines += 1    
        try:                                 
            rate = daily_vol/num_lines
        except ZeroDivisionError  :
            pass  
        return rate              

    arr = get_array(path)    
    vol_rate = volatility(op_path, arr) 
    if(vol_rate > config.volatility_rate):
        print("# Warning: Array {} volatility_rate too high ".format(str(arr)) )

    with open(path, 'r') as f:
        data = json.load(f)

        for di in data:
            if(di['lastValue'] == '[Array]' and di['mLength'] > config.max_array_length_allow):
                print("# Warning: key: {} Array too long, length: {}".format( di['_id']['key'] , str(di['mLength'])) )
        if(len(data) > config.max_fields_each_doc):
            print("# Warning: Fields too many, length: {}".format(  str(len(data) ) ))


def get_array(path):
    array_list = []
    with open(path, 'r') as f:
        data = json.load(f)
        for di in data:
            if(di['lastValue'] == '[Array]'):
                array_list.append(di['_id']['key'])
    return array_list


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        action='store_true',
        help='varity array')
    args = parser.parse_args()    
    return args
if __name__ == "__main__":
    # args = parse_args()
    path = "./sample-data/varity.result.json"
    oplog_path = "./sample-data/upsert.result"
    report(path, oplog_path)


