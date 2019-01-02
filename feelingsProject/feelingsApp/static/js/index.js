const buttons = document.querySelectorAll('button')

buttons.forEach(item => {
    item.addEventListener('click', () => {
        console.log(item)
    })
})

