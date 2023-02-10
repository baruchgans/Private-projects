//Implement a function that reverses a string using iteration...and then recursion!
function reverseStringIteratively(str) {
    let reversedStr = ''
    for (let i = str.length - 1; i >= 0; i--) {
        reversedStr += str[i]
    }
    return reversedStr;
}


function reverseStringRecursion(str) {
    if (str.length === 2) {
        return str[1] + str[0]
    }
    if (str.length === 1) {
        return str
    }
    return str[str.length - 1] + reverseStringRecursion(str.substring(1, str.length - 1)) + str[0]
}

console.log(reverseStringIteratively('yoyo mastery'))
console.log(reverseStringRecursion('yoyo mastery'))

//should return: 'yretsam oyoy'
