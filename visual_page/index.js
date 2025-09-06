document.addEventListener('DOMContentLoaded', async function () {
    send_btn = document.querySelector(".send")
    input = document.querySelector("#textbox")
    screen = document.querySelector(".screen")

    send_btn.addEventListener('click', async function () {
        let message = input.value;

        if (message) {
            add_consequently("user", message);
            input.value = "";
        }
        else {
            add_consequently("ai", "Got empty message!")
        }

    })
})

async function add_consequently(className, message) {
    const new_div = document.createElement('div');
    new_div.classList.add(className, "msg-box");
    new_div.textContent = message;
    screen.appendChild(new_div);
}












