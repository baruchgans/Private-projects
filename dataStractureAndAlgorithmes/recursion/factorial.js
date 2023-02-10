// Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop
cacheing_factorial = {};

function findFactorialRecursive(number) {
    let startTime = performance.now()
    if ([1, 0].includes(number)) {
        let endTime = performance.now()
        console.log(`Call to ${arguments.callee.name} took ${endTime - startTime} milliseconds`)
        return 1
    }
    let res;
    if (cacheing_factorial[number]) {
        res = cacheing_factorial[number];
    } else {
        res = number * findFactorialRecursive(number - 1);
        cacheing_factorial[number] = res;
    }
    return res;
}

function findFactorialRecursiveWithoutMemoize(number) {
    let startTime = performance.now()
    if ([1, 0].includes(number)) {
        let endTime = performance.now()
        console.log(`Call to ${arguments.callee.name} took ${endTime - startTime} milliseconds`)
        return 1
    }
    return number * findFactorialRecursiveWithoutMemoize(number - 1)
}

function findFactorialIterative(number) {
    let startTime = performance.now()
    let res = 1;
    for (let i = 1; i <= number; i++) {
        res *= i
    }
    let endTime = performance.now()
    console.log(`Call to ${arguments.callee.name} took ${endTime - startTime} milliseconds`)
    return res;
}

let a = findFactorialIterative(100)
let b = findFactorialRecursive(100)
let c = findFactorialRecursiveWithoutMemoize(100)
