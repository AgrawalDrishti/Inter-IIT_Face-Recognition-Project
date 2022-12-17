const forms = document.querySelector(".forms"),
      pwShowhide = document.querySelectorAll(".eye-icon");
      

pwShowhide.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click",()=>{
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");

        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type="text";
                eyeIcon.classList.replace("bx-hide","bx-show");
                return;
            }

            password.type = "password";
            eyeIcon.classList.replace("bx-show","bx-hide");
        })
    })
})
