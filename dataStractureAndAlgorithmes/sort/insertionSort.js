const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function moveAllNumbersRight(curr, firstIdxToMove, array) {
    let temp = array[curr]
    for (let j = curr; j > firstIdxToMove; j--) {
        array[j] = array[j - 1]
    }
    array[firstIdxToMove] = temp
}

function insertionSort(array) {
    if (array.length < 2) {
        return array
    }
    for (let curr = 1; curr < array.length; curr++) {
        for (let i = curr - 1; i >= -1; i--) {
            if (i === -1 || array[i] < array[curr]) {
                moveAllNumbersRight(curr, i + 1, array);
                break
            }
        }
    }
}

insertionSort(numbers);
console.log(numbers);

