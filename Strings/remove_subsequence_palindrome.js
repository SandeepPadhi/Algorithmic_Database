/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    if (s.length == 0) {
        return 0;

    }
    var left = 0,
        right = s.length - 1
    while (left <= right && s[left] == s[right]) {
        left += 1;
        right -= 1;
    }
    if (left > right) {
        return 1;
    }
    return 2;

};