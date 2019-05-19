#!/bin/bash
# db cashLoan 
# collection users , loans
#generate upsert.result
mlogfilter mongod01.log --operation update >> updsert.result

#genreate varity.result
mongo cashLoan --eval "var collection = 'users', lastValue = true, outputFormat='json'" variety.js >> varity.users.result.json
mongo cashLoan --eval "var collection = 'loans', lastValue = true, outputFormat='json'" variety.js  >> varity.loans.result.json

