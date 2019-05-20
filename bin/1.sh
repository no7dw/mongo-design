#!/bin/bash
# db cashLoan 
# collection users , loans
#1
#generate upsert.result
cd ../../mtools/
mlogfilter mongod01.log --operation update > upsert.result
#2
#genreate varity.result
cd ../variety
mongo cashLoan --eval "var collection = 'users', lastValue = true, outputFormat='json'" variety.js > variety0.users.result.json
#3 remove head 22 line
tail -n +23 variety0.users.result.json > variety.users.result.json 

#repeat
mongo cashLoan --eval "var collection = 'loans', lastValue = true, outputFormat='json'" variety.js  > variety0.loans.result.json
tail -n +23 variety0.loans.result.json > variety.loans.result.json 

mv variety.loans.result.json ../mongo-design/sample-data/
cd ./mongo-design
python src/array.py 
