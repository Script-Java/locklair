window.onload = ()=> {
    // Grabing the Elements through javascript by ID
    var add_btn = document.getElementById('add_btn');
    var delete_btn = document.getElementById("delete_btn");
    add_btn.addEventListener("click", add_word)
    delete_btn.addEventListener("click", delete_word)

}

function add_word() { 
    var word_container = document.getElementById("word_container");
    var input = document.getElementById("input");
    // Here we are creating the new HTML elements
    const new_list_item = document.createElement("li");
    const new_delete_btn = document.createElement("button");
    // here we are adding classes to these elements
    new_list_item.classList.add("list-group-item","word_list")
    new_delete_btn.classList.add("btn","btn-danger")
    // here we are adding the ID of "delete_btn" so that we can use it in our function
    new_delete_btn.setAttribute("id", "delete_btn");
    // here we added the input value to the inner text of the new li element
    new_list_item.innerHTML = input.value;
    new_delete_btn.innerHTML = "x"
    // here we adding the delete button to li element
    new_list_item.appendChild(new_delete_btn);
    word_container.appendChild(new_list_item)
}


var delete_btn = document.getElementById("delete_btn");
delete_btn.addEventListener("click", ()=> {
    parent = delete_btn.parentNode;
    parent.remove();
})
