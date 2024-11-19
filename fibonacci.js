// fibonacci sequence solution in js
function fibonacci(n) {
    // handle base case 
    if (n <= 0) return 0; // fibonacci(0) = 0
    if (n === 1) return 1; // fibonacci(1) = 1

    // initialize the first two fibonacci numbers
    let prev = 0, curr = 1;

    // loop to calculate fibonacci numbers up to n 
    for (let i = 2; i <= n; i++) {
        let temp = curr; // store current value temporarily
        curr = prev + curr; // calculate the next fibonacci number 
        prev = temp; // update previous value to current value
    }
 }