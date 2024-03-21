function btn(btn_num,k,btn_reset){
    for (let i = 0; i < btn_num.length; i++) {
        k.push(btn_num[i].innerText)
        btn_num[i].addEventListener("click", function () {
            var b = parseInt(btn_num[i].innerText) - 1
            btn_num[i].innerText = b
            if (b == 0) {
                b = 0;
                btn_num[i].innerText = b;
                btn_num[i].setAttribute("disabled","");
            }
        });
        btn_reset[i].addEventListener("click", function () {
            btn_num[i].innerText = k[i];
            btn_num[i].removeAttribute("disabled");
        });
        
    }
}