// Given a number N return the index value of the Fibonacci sequence, where the sequence is:

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
// the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

//For example: fibonacciRecursive(6) should return 8

function fibonacciIterative(n) {
    let ans = 1
    let prev = 1
    for (let i = 3; i <= n; i++) {
        let temp = ans
        ans = prev + ans
        prev = temp
    }
    return ans;
}

let a = fibonacciIterative(8);

function fibonacciRecursive(n) {
    return n < 2 ? n : fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

let b = fibonacciRecursive(8)
