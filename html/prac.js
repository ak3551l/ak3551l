let evenNumbers = [];
let oddNumbers = [];
for (let i=0; i<=20; i++) {
    if (i % 2 === 0) {
        evenNumbers.push(i);
    } else {
        oddNumbers.push(i);
    }
}

console.log(evenNumbers);
console.log(oddNumbers);
