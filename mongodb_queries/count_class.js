/*
    script to count number of classes. 
*/

// Connect to the database ds_project
db = connect('mongodb://localhost/ds_project');

// Get the count of documents in each class
var classCounts = db.tweets.aggregate([
  { $group: { _id: "$target", count: { $sum: 1 } } },
  { $project: { target: "$_id",  count: 1, _id: 0 } }
]).toArray();

printjson(classCounts);



