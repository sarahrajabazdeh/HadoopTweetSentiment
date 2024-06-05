/*
    script to count number of classes. 
*/

// Connect to the database ds_project
db = connect('mongodb://localhost/ds_project');

var classCounts = db.tweets.aggregate([
  { $group: { _id: "$target", count: { $sum: 1 } } }
]).toArray();

printjson(classCounts);

printjson(classCounts.length);
printjson(disctionary.length);  
