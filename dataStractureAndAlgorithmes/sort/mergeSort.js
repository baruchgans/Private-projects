const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function mergeSort(array) {
    if (array.length === 1) {
        return array
    }
    let mid = Math.floor(array.length / 2);
    let left = array.slice(0, mid)
    let right = array.slice(mid)

    return merge(mergeSort(left), mergeSort(right))
}

function merge(left, right) {
    let res = []
    let currLeft = 0
    let currRight = 0
    while (currLeft < left.length && currRight < right.length) {
        if (left[currLeft] < right[currRight]) {
            res.push(left[currLeft])
            currLeft++;
        } else {
            res.push(right[currRight])
            currRight++;
        }
    }

    return res.concat(left.slice(currLeft)).concat(right.slice(currRight))
}


const answer = mergeSort(numbers);
console.log(answer);
