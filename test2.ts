// This solution is O(N/2) for time and O(1) for space 🤷

/**
 * This solution is based on the following observations:
 *
 * * A ^ A = 0, this implies that any number that appears an even amount of times in a set of
 *   XOR operations will always yield 0
 * * A ^ 0 = A
 * * If the input set is composed of an even amount of numbers, each number will appear an even
 *   amount of times
 * * If the input set is composed of an odd amount of numbers, numbers in odd positions will
 *   appear an odd amount of times, while numbers in even positions will appear an even amount of
 *   times
 *
 * From the above we can see that if N is even, the result will be 0. If N is odd we can
 * calculate f(X) as X0 ^ X2 ^ X4 ^ ... ^ XN, e.g. XOR between all odd-indexed numbers of X
 */

// Sample input
const input = [1, 2, 3, 4, 5];

// If N is even, all its elements will appear an even amount of times, thus f(X) = 0
if (input.length % 2 === 0) {
    console.log(`result is 0`);
    return 0;
}

// Else, go on and XOR all odd positions
let result = input[0]; // Start from the first number
for (let i = 2; i < input.length; i += 2) {
    result ^= input[i]; // XOR each odd-indexed number
}

console.log(`result is ${result}`);
return result;
