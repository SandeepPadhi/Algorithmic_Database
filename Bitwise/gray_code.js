/*
Date9/03/2021
The following program is solved using bit maniplation and recursion
*/


/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {

        var gray = new Set();
        var Ans = [0];

        function find(n, gray, Ans) {
            tmp = Ans[Ans.length - 1]
            gray.add(0);
            var i = 0;
            while (i < n) {
                if (!gray.has(tmp ^ (1 << i))) {
                    gray.add(tmp ^ (1 << i));
                    Ans.push(tmp ^ (1 << i));
                    find(n, gray, Ans);
                    return;

                }
                i += 1;

            }



        }
        find(n, gray, Ans);

        return Ans;