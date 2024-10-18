const arr = [1,2,3,4,5,6,7,8]

for(let i=0; i<arr.length; i++) {
    const el = arr[i]
}

const newMappedArray = arr.map(function(element) {
    console.log(element);
    return 100;
})

console.log(arr, newMappedArray)
