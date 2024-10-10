function spinWords(string){
  //TODO Have fun :)
  return string.split(' ') // Split the string into words
  .map(word => {
    // Reverse the word if its length is greater than 4, else leave it as it is
      return word.length > 4 ? word.split('').reverse().join('') : word;
  })
  .join(' '); // Join the words back into a sentence

}


// Test cases
console.log(spinWords("Hey fellow warriors"));  // Output: "Hey wollef sroirraw"
console.log(spinWords("This is a test"));       // Output: "This is a test"
console.log(spinWords("This is another test")); // Output: "This is rehtona test"
