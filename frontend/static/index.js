document.addEventListener('DOMContentLoaded', async function () {
    send_btn = document.querySelector(".send")
    input = document.querySelector("#textbox")
    screen = document.querySelector(".screen")

    send_btn.addEventListener('click', async function () {
        let message = input.value;

        if (message) {
            add_consequently("user", message);
            let ai_response = await sendResponse(message);
            input.value = "";
            console.log(ai_response)
            add_consequently("ai",ai_response)
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

async function sendResponse(user_message){
    try {
        let response = await fetch('/api/get_res_from_ai',{
            method : 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({'user_message':user_message})
        })

        if(response.ok){
            let data = await response.json()
            console.log(data.ai_response)
            return data.ai_response
        }
        
    } catch (error) {
        alert(error)
    }
}









