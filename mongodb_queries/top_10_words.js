/*
    script to find the top 10 most used words in the dictionary
*/

// Connect to the database ds_project
db = connect('mongodb://localhost/ds_project');

// Top 10 most used words in the dictionary
var top10Words = db.dictionary.aggregate([
    // Sort by count in descending order
    {$sort: {count: -1}},
    
    // Limit to the top 10 documents
    {$limit: 10},

    // Project only the word and count fields
    {$project: {_id: 0, words: 1, count: 1}}

]).toArray();

// Print the result
printjson(top10Words);