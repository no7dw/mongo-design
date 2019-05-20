#we has copied mongodb.log from mongodb log path
#step1 analyse mongodb.log using mlogfilter(from mtools)
  # now we can see only upsert ops in this file 


#step2 analyse documents data in collection using variety
  # now we can see document key and its datatype and if it's an  array type ,
  # and it's the longest array length of the array type 
  # as we now see : a field name contactinfo has an array type , 
  # and longest length of data is 2047

#step3 run analyst script for some design rule of the above collection
  # now the script output some  the design advice 
  # some rules are implemented such as :
     # max_array_length_allow
     # max_fields_each_doc 
     # volatility_rate
     # in this case , the data pass the rule:volatility_rate
     # parameter is config in config.py

  # that's the analyst result for one collections
   
#step4 we can repeat the same of other collections
