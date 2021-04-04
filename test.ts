// This solution is O(N) both for space and time complexities

// LSB = Least Significant Bit
// MSB = Most Significant Bit

// inputs, bit arrays where position 0 is the LSB
const A = [1, 0, 0, 1, 1, 1]; // first binary number, smaller than B. its size is N.
const B = [0, 0, 1, 1, 1, 1, 1]; // second binary number, greater than A. its size is M.

/**
 * prepare a solution S, a zeroes array of size M
 */
const S = Array(B.length).fill(0);

// If B has more bits than A (and inputs are well formatted) than I will need to permute all bits
// in A to reach B, the solution is then 0.
if (B.length > A.length) {
    // return S;
    console.log(S);
}

// Add 0s to A until matches B's length, just for convenience
for (let j = 0; j < B.length - A.length; j++) {
    A.push(0);
}

/**
* Loop over B starting from its MSB (e.g. the last position of B, which is N-1) down to its LSB.
* The idea is that incrementing A's bits to reach B will permute all possible bits in A
* starting from its LSB up until they start to be the same in B; since permuting them will produce
* a 0 when `&` is performed between those bits I can scan A and B starting from MSB and keep
* the bits that are 1 in both; as soon as I detect a difference it means that from that point
* onwards all bits will be permuted and their logical AND will be 0. The solution is then
* a binary number whose bits are 1 for each bit that is 1 in both A and B starting from B's
* MSB.
*/
for (let i = B.length - 1; i >= 0; i--) {
    // if this bit is 1 for both A and B then it will be 1 in the solution as well, as it won't
    // be permutated while increasing A to reach B
    if (A[i] && B[i]) {
        S[i] = 1;
    } else {
        // If two bits are different it means that a permutation is needed, thus producing a 0 while
        // performing the & operator. But also means that I will also permute all other bits from this point
        // onwards and I can safely keep them at 0 and return.
        break;
    }
}

// return S;
console.log(`solution is`, S);