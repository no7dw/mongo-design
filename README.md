### mongodb embeded document advisor

the main idea of this project is base on the argument ***whether I should use embedded documents design or not when we design our model***

### demo video
   ![demo](https://raw.githubusercontent.com/no7dw/mongo-design/master/demo.gif)
### case study
As we know , MongoDB support flexible schema. When compare to model design in SQL database ,   an e-commerce system  is different in NoSQL way,for example:

look at collection : users ,  orders



users

```
{
    _id: Object("1aa4")
    phone: '123456',
    address: [
        'address1',
        'address2',
        'address3'
    ]
}
```

orders:

```
{
    _id: ObjectId("1234"),
    userId: ObjectId("1aa4"),
    pay_amount: 100.00,
    deliver_address: "NYC 101"
    product: {}
}
```

another option is create a new addressBook for user
users

```
{
    _id: Object("1aa4")
    phone: '123456'
}    
    
```

addressBook 

```
{
    userId:Object("1aa4")
    address: [
        {"NYC 101"},
        {"Washington DC 102"}
        {"San Francisco 103"}
    ]
}
```

the addressBook design seems a little bit ambiguous, so what's the better design ???  should I embeded the addressBook in users collection or use reference design 

### some practical design principle

    there is a guy write an [article](http://www.daprota.com/doc/m2/mongodb-data-modeling-adviser-expand.html) summary serveral principle 

    So I follow some idea he memtions:
        - embeded documents should not too large
        - embeded documents should not change too often
        - embeded documents should have the same change frequency with parent document
        - embeded documents should be dependent with other documents
        - ...
    and build some script tools

### projects explians 

this projects include [mtools](https://github.com/no7dw/mtools.git) and [variety](https://github.com/no7dw/variety.git) , both of two are folk, but I change the code according to my case usage.

#### how to use 
    $ cat bin/1.sh
    - 1 analyse mongodb.log using mlogfilter(from mtools)
    - 2 analyse documents data in collection using variety
    - 3 run analyst script for some design rule 
      

     
#### todo

 - [] export and import to altas
 - [] implement more rules

#### notes
    
   MongoDB Atlas account using : wdeng#kalengo.com (#->@)

