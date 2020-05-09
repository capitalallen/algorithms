var getRow = function(rowIndex) {
    var t = [];
    for (var r=0;r<=rowIndex;r++){
        var row = new Array(r+1);
        row[0] = 1;
        row[row.length-1]=1;
        for (var i=1;i<row.length-1;i++){
            row[i] = t[r-1][i-1]+t[r-1][i];
        }
        t.push(row);
    }
    return t[rowIndex];
};

var generate2 = function(numRows) {
    
    if (numRows === 0) {
        return [];
    }
    
    if (numRows === 1) {
        return [[1]];
    }
    
    
    const rows = generate(numRows - 1);
    const parentRow = rows[rows.length - 1];        

    const newRow = [1];
    
    for (let i=1; i<parentRow.length; i++) {
        newRow.push(parentRow[i - 1] + parentRow[i]);
    }
    
    newRow.push(1);

    rows.push(newRow);
    return rows;
};