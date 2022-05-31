function deleteItem(element) {
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        element.parentElement.submit(this);
    }
}

/* 
document.querySelector("a[href='/products']").classList.add("active")
*/