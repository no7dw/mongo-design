import json
import argparse
config = {
    "max_array_length_allow" : 10
}

def report(path):
    print(path)
    with open(path, 'r') as f:
        data = json.load(f)
        for di in data:
            if(di['lastValue'] == '[Array]' and di['mLength'] > config['max_array_length_allow']):
                print("# Warning: key: {} Array too Long, length: {}".format( di['_id']['key'] , str(di['mLength'])) )
        

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
    # report(args.path)
    report("./sample-data/varity.result.json")
