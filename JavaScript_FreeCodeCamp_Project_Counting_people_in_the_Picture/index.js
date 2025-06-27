
let countEl = document.getElementById("count-el")
// console.log(countEl)

let count = 0
// 1. Grab the save-el paragrpah and store it in a variable saveEl

let saveEl = document.getElementById("save-el")
//entries = '' 

function increment(){
    count += 1
    countEl.innerText = count
    // console.log(count)
}

function save(){
    // 2. Create a variable that contains the count and the 
    // dash seperator, i.e 12 _ 23 _ 
    let numbers_string = count + ' - '
    
    // entries += numbers_string

    // Render the variable in the saveEl using innerText
    saveEl.textContent += numbers_string
    // NB : Make sure to not delete the existing content of the paragraph
    count  = 0
    countEl.textContent = count
}
    
