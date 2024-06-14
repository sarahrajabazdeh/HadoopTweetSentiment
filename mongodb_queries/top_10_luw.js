/*
    script to find the top 10 least used words in the dictionary with length > 4 and <= 7
*/

// Connect to the database ds_project
db = connect('mongodb://localhost/ds_project');

// Top 10 least used words in the dictionary with length > 4 and <= 7
var top10LUW = db.dictionary.aggregate([
    // Filter out words with length > 4 and <= 7
    {
        $match: { 
            $expr: 
            {
                $and: [
                    {$gt: [{$strLenCP: "$words"}, 4]},
                    {$lte: [{$strLenCP: "$words"}, 7]},
                ]
            }
        }
    },

    // Sort by count in ascending order
    {$sort: {count: 1}},
    
    // Limit to the top 10 documents
    {$limit: 10},

    // Project only the word and count fields
    {$project: {_id: 0, words: 1, count: 1}}

]).toArray();

// Print the result
printjson(top10LUW);